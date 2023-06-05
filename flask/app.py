from flask import Flask, request,render_template
from kafka import KafkaConsumer
import json
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

@app.route('/<hotspotname>/<service>',methods=['GET'])
def service(hotspotname,service):
    template_path = f"map/{service}/{hotspotname}.html"
    return render_template(template_path)
    
    
    
    
if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True)

