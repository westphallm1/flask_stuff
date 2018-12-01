from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/pose',methods=['POST'])
def get_pose():
    data = request.data.decode('ascii')
    print(json.loads(data)[0]['score'])
    return '',200

app.run(host='localhost',port=8000)
