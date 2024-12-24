from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Il messaggio non può essere vuoto"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Sei un assistente AI."},
            {"role": "user", "content": user_message}
        ]
    )
    return jsonify({"response": response['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
