English → Kannada translator with Text-to-Speech

Requirements

- Python 3.8+
- Install dependencies:

```bash
pip install -r requirements.txt
```

Usage

- Interactive:

```bash
python translate_tts.py
```

- One-liner:

```bash
python translate_tts.py "Hello, how are you?"
```

What it does

- Translates provided English text to Kannada using `googletrans`.
- Generates Kannada speech using `gTTS` and saves an MP3 file, then attempts to open it with the system default player.

Notes

- `googletrans` is an unofficial client that may occasionally be rate-limited or break; for production use consider an official translation API (Google Cloud Translate, Microsoft Translator, etc.).
- The script uses the system default player: `os.startfile` on Windows, `open` on macOS, and `xdg-open` on Linux.
# English_to_Kannada_Translator