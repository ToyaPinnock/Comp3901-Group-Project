import speech_recognition as SR
from flask import Flask, render_template, request, Response
import cv2 as cv

def speechRec():
    recognizer = SR.Recognizer()
    while True:
        try:
            with SR.Microphone() as mic:
                print('Say Something')
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio =recognizer.listen(mic)
                
                text= recognizer.recognize_google(audio)
                text=text.lower()
                print(f"Recognize {text}")
                return render_template( "SpeechReg.html", Words=text)
                
        except SR.UnknownValueError:
            return render_template( "SpeechReg.html", Error= "")
        except SR.RequestError as e:
            recognizer = SR.Recognizer()
camera= cv.VideoCapture(0)
def gen_frames():
    # while loop reads frames continuously
    while True:
        #read camera frame
        success, frame=camera.read()
        if not success:
            break
        else:
            #object_detection() Add object detection function here
            ret,buffer= cv.imencode('.jpg', frame)
            frame= buffer.tobytes()
            yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
@app.route("/video")
def video1():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/video2")
def video2():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
