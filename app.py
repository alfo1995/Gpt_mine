from flask import Flask, request, jsonify
from openai import OpenAI
import json
import os

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")
organization = os.getenv("ORGANIZATION_ID")
organization = os.getenv("PROJECT_ID")

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
        max_tokens = data.get('max_tokens', 200)
        model = data.get('model', 'gpt-3.5-turbo')

        if not prompt:
            return jsonify({"error": "Il messaggio non può essere vuoto"}), 400

        # Invia la richiesta a OpenAI utilizzando il nuovo formato corretto
        response = client.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.6
        )

        # Estrarre il contenuto generato
        generated_text = response['choices'][0]['message']['content']

        return jsonify({"success": True, "response": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
