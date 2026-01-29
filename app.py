from flask import Flask, request, jsonify
from googletrans import Translator
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

translator = Translator()

@app.route("/")
def home():
    return "English to Kannada Translator is running 🚀"

@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.json
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    translated = translator.translate(text, dest="kn")
    translated_text = translated.text

    filename = f"{uuid.uuid4()}.mp3"
    tts = gTTS(translated_text, lang="kn")
    tts.save(filename)

    return jsonify({
        "english": text,
        "kannada": translated_text,
        "audio_file": filename
    })
