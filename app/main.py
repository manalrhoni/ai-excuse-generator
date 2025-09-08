from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import json

# Create the FastAPI app
app = FastAPI(title="AI Excuse Generator")

# This allows our frontend to talk to our backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for development only)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# This defines the data we expect from the frontend
class ExcuseRequest(BaseModel):
    situation: str
    mode: str = "professional"  # Add mode field with default


# This is the main endpoint that generates excuses
@app.post("/excuse")
async def generate_excuse(request: ExcuseRequest):
    # Define mode instructions
    mode_instructions = {
        "professional": "Generate a convincing, professional, and believable excuse",
        "serious": "Generate a serious, straightforward, and credible excuse",
        "funny": "Generate a humorous, witty, and entertaining excuse",
        "creative": "Generate a creative, unexpected, and imaginative excuse",
        "formal": "Generate a formal, official, and properly structured excuse",
        "casual": "Generate a casual, relaxed, and friendly excuse",
        "dramatic": "Generate a dramatic, exaggerated, and theatrical excuse"
    }

    # The prompt we send to Ollama
    prompt = f"""
    {mode_instructions.get(request.mode, "Generate a convincing excuse")} for why someone is {request.situation}.

    **CRITICAL INSTRUCTIONS:**
    1. Provide ONLY the excuse itself - no explanations, no introductions, no conclusions
    2. Do NOT start with "Sure, here is" or "I'd suggest" or any similar phrases
    3. Do NOT add any commentary or analysis
    4. The response should be exactly 1-2 sentences maximum
    5. Make it sound genuine and reasonable

    Excuse:
    """

    # The data to send to Ollama's API
    payload = {
        "model": "llama2",
        "prompt": prompt,
        "stream": False
    }

    try:
        # Send the request to Ollama
        response = requests.post("http://host.docker.internal:11434/api/generate",
                                 data=json.dumps(payload),
                                 headers={"Content-Type": "application/json"})
        response.raise_for_status()  # Check for errors

        # Parse the response from Ollama
        result = response.json()
        excuse = result.get("response", "Sorry, I couldn't think of an excuse!").strip()

        # Clean up the response to remove any unwanted explanations
        if "Sure, here is" in excuse:
            excuse = excuse.split("Sure, here is")[-1].strip()
        if "I'd suggest" in excuse:
            excuse = excuse.split("I'd suggest")[-1].strip()
        if ":" in excuse and len(excuse.split(":")) > 1:
            excuse = excuse.split(":", 1)[1].strip()
        if excuse.startswith('"') and excuse.endswith('"'):
            excuse = excuse[1:-1].strip()

        # Return the excuse to the frontend
        return {"excuse": excuse}

    except requests.exceptions.RequestException as e:
        # Handle errors (e.g., Ollama not running)
        return {"excuse": f"Error: Could not connect to Ollama. Is it running? Details: {e}"}


# Root endpoint - just for testing
@app.get("/")
async def root():
    return {"message": "AI Excuse Generator API is running!"}