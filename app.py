from flask import Flask, request
from plivo import plivoxml
import openai

app = Flask(__name__)

# Initialize the OpenAI API client with your API key
openai.api_key = "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"

@app.route('/incoming_sms', methods=['POST'])
def handle_incoming_sms():
    # Extract the incoming message details from the request
    message = request.form['Body']
    sender = request.form['From']
    recipient = request.form['To']

    # Use the OpenAI API to generate a response to the incoming message
    prompt = message
    response = openai.Completion.create(
        engine="text-davinci-002", prompt=prompt, max_tokens=50
    )

    # Extract the generated response from the OpenAI API response object
    generated_text = response.choices[0].text.strip()

    # Send the generated text as a response to the incoming message
    plivo_response = plivoxml.Response()
    plivo_response.addMessage(generated_text)

    return str(plivo_response)

if __name__ == '__main__':
    app.run(debug=True)
