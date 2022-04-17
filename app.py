from flask import Flask, render_template, request, Response
import cv2 as cv


app= Flask(__name__)


@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/homeMode")
def homemode():
    
    return render_template("homeMode.html")

@app.route("/cashMode")
def cashMode():
    
    return render_template("cashMode.html")

@app.route("/SpeechRecognition", methods=["GET","POST"])
def SpeechReg():
    if request.method == "POST":
        results=request.form
        print (results)
        for key, value in results.items():
            print(key,value)
        message = "python says hello"
        return message
    return render_template("SpeechReg.html")

@app.route("/VideoStream", methods=["GET","POST"])
def video():
    print("activated")
    if request.method == "POST":
        results=request.form
        for key, value in results.items():
            # initialize camera
            cap = cv.VideoCapture(value)
            print(key,value)  
        message = "video capture"
        return message
    return render_template("SpeechReg.html")

    

            


            




if __name__ == '__main__':
    app.run(debug=True)