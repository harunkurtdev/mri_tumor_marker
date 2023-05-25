from flask import Flask, Response
from flask_ngrok import run_with_ngrok
import cv2

from pyngrok import ngrok

app = Flask(__name__)
# run_with_ngrok(app)

# video_path = "/content/video.mp4"

video = cv2.VideoCapture(0)
# video.set(cv2.CAP_PROP_FPS, 25) 
    
def gen(video):
    while True:
        success, image = video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
@app.route('/')
def index():
    global video
    return Response(gen(video), mimetype='multipart/x-mixed-replace; boundary=frame')

        
@app.route('/hello')
def hello():
    return "Hello"

if __name__ == '__main__':
    public_url = ngrok.connect(8081).public_url
    print(public_url)
    app.run(host='0.0.0.0', port=8081)