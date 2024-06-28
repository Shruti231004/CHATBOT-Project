from flask import Flask, render_template, request, jsonify, g
from flask_cors import CORS
from nltk.tokenize import word_tokenize
from chat import get_response
import os
import threading

app = Flask(__name__)
CORS(app)

shutdown_trigger = False

@app.route("/", methods=["GET"])
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    global shutdown_trigger
    text = request.get_json().get("message")
    if text.lower() == "bye":
        response = {"answer": "Goodbye! The server is shutting down."}
        shutdown_trigger = True
        threading.Thread(target=shutdown_server).start()
        return jsonify(response)
    else:
        response = get_response(text)
        message = {"answer": response}
        return jsonify(message)

def shutdown_server():
    # Delay to ensure the response is sent
    import time
    time.sleep(1)
    os._exit(0)

if __name__ == "__main__":
    app.run(debug=True)




