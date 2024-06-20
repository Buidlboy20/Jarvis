from flask import Flask, request, make_response, send_file
from io import BytesIO
import speech_recognition as sr
app = Flask(__name__)
source = sr.Microphone()
recognizer = sr.Recognizer()
def generate_wav_file(output_buffer, audio_data):
    audio_data = recognizer.listen(source).get_raw_data()
    output_buffer.write(audio_data)

@app.route('/upload', methods=['POST'])
def upload_wav():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    audio_data = file.read() 
    buffer = BytesIO()
    generate_wav_file(buffer, audio_data)

    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'audio/wav'
    response.headers['Content-Disposition'] = 'attachment; filename=sound.wav'
    return response


path_to_file = "/path/to/your/other.wav"

@app.route('/download', methods=['GET'])
def download_wav():
    return send_file(path_to_file, mimetype="audio/wav", as_attachment=True, attachment_filename="other.wav")

if __name__ == '__main__':
    app.run(debug=True)
