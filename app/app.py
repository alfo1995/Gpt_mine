from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import json
import os

app = Flask(__name__)
# Allow requests from your frontend domain
CORS(app, origins=["https://my-project-5kd2qw4pg-alfo1995s-projects.vercel.app"])


api_key = os.getenv("OPENAI_API_KEY")
organization = os.getenv("ORGANIZATION_ID")
project = os.getenv("PROJECT_ID")

# Verifica se la chiave è correttamente impostata
try:
    client = OpenAI(api_key=api_key, organization=organization, project=project)
except KeyError:
    print("The env variables were not found.")
    
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Ricevi il messaggio dal corpo della richiesta
        data = request.json
        prompt = data.get('prompt', '')

        if not prompt:
            return jsonify({"error": "Il messaggio non può essere vuoto"}), 400

        # Invia la richiesta a OpenAI utilizzando il nuovo formato corretto
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250,
            temperature=0.6
        )

        # Estrarre il contenuto generato
        generated_text = response.choices[0].message.content

        return jsonify({"success": True, "response": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
