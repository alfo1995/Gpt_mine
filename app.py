from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Aggiungi la tua chiave API di OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")  # Assicurati che la variabile d'ambiente sia correttamente configurata

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Ricevi il messaggio dal corpo della richiesta
        data = request.json
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "Il messaggio non può essere vuoto"}), 400

        # Invia la richiesta a OpenAI utilizzando il nuovo formato
        response = openai.Completion.create(
            model="text-davinci-003",  # Usa un modello come text-davinci-003
            prompt=user_message,
            max_tokens=150
        )

        return jsonify({"response": response.choices[0].text.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
