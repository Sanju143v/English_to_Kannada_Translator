import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import time
import subprocess
from googletrans import Translator
from gtts import gTTS

def play_file(path):
    try:
        if os.name == 'nt':
            os.startfile(path)
        elif sys.platform == 'darwin':
            subprocess.call(['open', path])
        else:
            subprocess.call(['xdg-open', path])
    except Exception:
        pass


def main():
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = input('Enter English text to translate to Kannada: ').strip()
        if not text:
            print('No text provided. Exiting.')
            return

    print('Translating...')
    translator = Translator()
    try:
        translated = translator.translate(text, dest='kn')
        kn_text = translated.text
    except Exception as e:
        print('Translation failed:', e)
        return

    print('Kannada translation:')
    print(kn_text)

    print('Generating speech (Kannada)...')
    try:
        tts = gTTS(text=kn_text, lang='kn')
        filename = f'translation_{int(time.time())}.mp3'
        tts.save(filename)
        print(f'Saved TTS to {filename}')
        play_file(filename)
    except Exception as e:
        print('TTS generation failed:', e)


if __name__ == '__main__':
    main()
