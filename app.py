from flask import Flask,request,render_template,jsonify
import os
from flask_cors import CORS,cross_origin
from chicken_disease_classifier.pipeline.predict import PredictionPipeline
from chicken_disease_classifier.utils.common import decodeImage


os.putenv("LANG","en_US.UTF-8")
os.putenv("LC_ALL","en_US.UTF-8")

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self) -> None:
        self.filename = "inputimage.jpg"
        self.classifier = PredictionPipeline(self.filename)

@app.route("/",methods = ['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train",methods = ['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training Done Successfully"

@app.route("/predict",methods = ["POST"])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0",port=80)
