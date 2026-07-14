import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from generator import BotGenerator
from workflow import ChatWorkflow
from chatbot import WhatsAppClient

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'botbuilder-secret-key-123'

# Initialize modules
generator = BotGenerator(os.getenv("GEMINI_API_KEY"))
workflow = ChatWorkflow(os.getenv("GEMINI_API_KEY"))
wa_client = WhatsAppClient()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/preview')
def preview():
    return render_template('preview.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/api/generate', methods=['POST'])
def generate_bot():
    data = request.json
    try:
        config = generator.generate_config(data)
        return jsonify({"status": "success", "data": config})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if mode == 'subscribe' and token == os.getenv("VERIFY_TOKEN"):
            return challenge, 200
        return 'Forbidden', 403

    if request.method == 'POST':
        data = request.json
        try:
            # Extract WhatsApp message details
            message = data['entry'][0]['changes'][0]['value']['messages'][0]
            from_number = message['from']
            text = message['text']['body']
            
            reply = workflow.get_response(text)
            wa_client.send_message(from_number, reply)
        except:
            pass
        return 'EVENT_RECEIVED', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)