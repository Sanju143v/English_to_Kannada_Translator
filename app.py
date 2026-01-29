from flask import Flask, render_template, request, jsonify, send_file
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import time
import uuid

app = Flask(__name__)
translator = GoogleTranslator(source='auto', target='kn')

# Ensure static folder exists for audio
AUDIO_DIR = os.path.join("static", "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        # Translate
        kn_text = translator.translate(text)
        
        # Generate Audio
        tts = gTTS(text=kn_text, lang='kn')
        filename = f"{uuid.uuid4()}.mp3"
        filepath = os.path.join(AUDIO_DIR, filename)
        tts.save(filepath)
        
        # Clean up old files (optional, simple strategy)
        cleanup_old_files()

        return jsonify({
            'original': text,
            'translated': kn_text,
            'audio_url': f"/static/audio/{filename}"
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

def cleanup_old_files():
    # Keep only last 10 files to avoid clutter
    files = sorted(
        [os.path.join(AUDIO_DIR, f) for f in os.listdir(AUDIO_DIR)],
        key=os.path.getmtime
    )
    if len(files) > 10:
        for f in files[:-10]:
            try:
                os.remove(f)
            except:
                pass

if __name__ == '__main__':
    # Hosting on 0.0.0.0 to be accessible via IP
    app.run(host='0.0.0.0', port=5000, debug=True)
