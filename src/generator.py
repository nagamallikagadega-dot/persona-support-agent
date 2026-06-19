import os
from google import genai
from google.genai import types

def generate_response(user_message: str, persona: str) -> str:
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY", ""))
    
    persona_prompts = {
        "Technical Expert": "You are a technical support expert. Use technical jargon, provide code examples, detailed parameters, and step-by-step technical solutions.",
        "Frustrated User": "You are an empathetic support agent. Acknowledge the user's frustration first, then provide simple, clear, step-by-step solutions. Be warm and reassuring.",
        "Business Executive": "You are a professional business support agent. Be concise, focus on business impact, provide timelines and ROI-focused solutions. Keep it brief and professional."
    }
    
    system_instruction = persona_prompts.get(persona, persona_prompts["Frustrated User"])
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash-preview-05-20',
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7,
                max_output_tokens=500
            )
        )
        return response.text
    except Exception as e:
        return f"I apologize, I'm unable to process your request right now. Please try again. Error: {str(e)}"
