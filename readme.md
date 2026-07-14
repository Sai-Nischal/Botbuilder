# BotBuilder AI

An AI-powered SaaS platform to generate and deploy WhatsApp Chatbots for small businesses using Google Gemini.

## Features
- AI Generation of Chatbot Logic.
- Real-time WhatsApp UI Preview.
- WhatsApp Cloud API Webhook integration.
- JSON-based modular workflow.

## Deployment to Render
1. Create a new Web Service on Render.
2. Connect your GitHub repository.
3. Select Environment: `Python`.
4. Build Command: `pip install -r requirements.txt`.
5. Start Command: `gunicorn app:app`.
6. Add Environment Variables from `.env.example`.