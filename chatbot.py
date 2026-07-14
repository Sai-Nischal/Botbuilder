import requests
import json
import os

class WhatsAppClient:
    def __init__(self):
        self.token = os.getenv("WHATSAPP_TOKEN")
        self.phone_id = os.getenv("PHONE_NUMBER_ID")
        self.url = f"https://graph.facebook.com/v17.0/{self.phone_id}/messages"

    def send_message(self, recipient_number, text):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "messaging_product": "whatsapp",
            "to": recipient_number,
            "type": "text",
            "text": {"body": text}
        }
        return requests.post(self.url, headers=headers, json=data)

    def send_template(self, recipient_number, template_name):
        # Implementation for template messages
        pass