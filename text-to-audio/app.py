from flask import Flask, request, render_template, send_file
from gtts import gTTS
from googletrans import Translator

app = Flask(__name__)
translator = Translator()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert_text_to_audio():
    text = request.form['text']
    lang = request.form.get('language', 'en')

    # Translate Hungarian text to English
    if lang == 'hu':
        translation = translator.translate(text, src='hu', dest='en')
        english_text = translation.text
    else:
        english_text = text

    # Convert text to speech using gTTS
    tts = gTTS(text=english_text, lang='en')
    output_filename = "output.mp3"
    tts.save(output_filename)

    # Send the file back to the user
    return send_file(output_filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
