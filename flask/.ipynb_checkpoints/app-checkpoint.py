from flask import Flask, request
from kafka import KafkaConsumer
import json
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

@app.route('/<hotspotname>/<service>',methods=['GET'])
def service(hotspotname,service):
    
if __name__ == '__main__':
    app.run(debug=True)

