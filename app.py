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
        response = openai.chat.Completion.create(
                    model="gpt-3.5-turbo", 
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt},
                    ],
                    max_tokens=200,  # Puoi aumentare il numero di token se necessario
                    temperature=0.5
                )

        return jsonify({"response": response.choices[0].text.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
