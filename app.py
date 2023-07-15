from flask import Flask,request,send_file
import os,openai,base64,io
import dotenv

app = Flask(__name__)

dotenv.load_dotenv()

@app.post('/generateImage')
def imageGeneration():
    if (request.method == 'POST'):
        body = request.json
        text = body['text']
        # get OPENAI_SECRET from env
        openai.api_key = os.environ.get('OPENAI_SECRET')
        # generating api using openai api
        response = openai.Image.create(
        prompt=text,
        n=1,
        size="256x256",
        response_format= 'b64_json'
        )
        b64_image = response['data'][0]['b64_json']
        # decoding th base64 image
        image = base64.b64decode(b64_image)
        return send_file(io.BytesIO(image),mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)