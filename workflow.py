import json
import os
from google import genai

class ChatWorkflow:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        
    def get_response(self, user_message):
        try:
            with open('chatbot_config.json', 'r') as f:
                config = json.load(f)
            
            # Simple keyword matching
            msg = user_message.lower()
            if "hello" in msg or "hi" in msg:
                return config['welcome_message']
            
            # AI Fallback
            prompt = f"Context: {json.dumps(config)}. User asked: {user_message}. Reply as the business bot."
            response = self.client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=prompt
            )
            return response.text
        except Exception as e:
            return "I'm having a bit of trouble. Please try again later."