from flask import Flask, Response
# Raspberry Pi camera module (requires picamera package, developed by Miguel Grinberg) i.e. camera_pi file
from camera_pi import Camera
app = Flask(__name__)

def gen(camera):
    #Vedio Streaming generating function
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/video_feed')
def video_feed():

    #Vedio straming route put this on your img tag Ex: <img src="ip_adress/vedio_feed"
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port =5000, debug=True, threaded=True)
