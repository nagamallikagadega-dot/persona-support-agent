import os
import json
from google import genai
from google.genai import types

def classify_customer_persona(user_message: str) -> dict:
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY", ""))
    
    system_instruction = (
        "You are a classification engine. Classify the user message into exactly one of three personas:\n"
        "1. 'Technical Expert': Uses jargon, asks about APIs/code/configs.\n"
        "2. 'Frustrated User': Uses emotional language, exclamation marks, or mentions urgency.\n"
        "3. 'Business Executive': Focuses on business impact, ROI, timelines.\n"
        "Provide your evaluation strictly in the requested JSON structure."
    )
    
    response_schema = {
        "type": "OBJECT",
        "properties": {
            "persona": {"type": "STRING", "enum": ["Technical Expert", "Frustrated User", "Business Executive"]},
            "confidence": {"type": "NUMBER"},
            "reasoning": {"type": "STRING"}
        },
        "required": ["persona", "confidence", "reasoning"]
    }
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash-preview-05-20',
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json",
                response_schema=response_schema,
                temperature=0.1
            )
        )
        return json.loads(response.text)
    except:
        return {"persona": "Frustrated User", "confidence": 0.5, "reasoning": "Default"}
