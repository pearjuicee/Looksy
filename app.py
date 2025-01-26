# app.py
from flask import Flask, render_template, Response
from camera import generate_frames

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/wardrobe')
def wardrobe():
    return render_template('wardrobe.html')

if __name__ == '__main__':
    app.run(debug=True)