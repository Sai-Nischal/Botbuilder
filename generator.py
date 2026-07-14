import os
import json
from google import genai
from google.genai import types

class BotGenerator:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def generate_config(self, business_data):
        prompt = f"""
        Generate a professional WhatsApp Chatbot configuration for this business:
        {json.dumps(business_data)}

        Return ONLY a JSON object with the following structure:
        {{
            "config": {{
                "business_name": "", "welcome_message": "", "goodbye_message": "",
                "faq": [ {{"question": "", "answer": ""}} ],
                "quick_replies": ["Service 1", "Pricing", "Contact"]
            }},
            "workflow": [
                {{"step": "welcome", "message": "...", "options": []}},
                {{"step": "services", "message": "...", "options": []}}
            ]
        }}
        """
        
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            ),
            contents=prompt
        )
        
        data = json.loads(response.text)
        
        # Save to local storage
        with open('chatbot_config.json', 'w') as f:
            json.dump(data['config'], f, indent=4)
        with open('workflow.json', 'w') as f:
            json.dump(data['workflow'], f, indent=4)
            
        return data