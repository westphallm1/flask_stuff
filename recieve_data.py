from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/pose')
def get_pose():
    data = request.args.get('data')
    print(json.loads(data))

app.run(host='localhost',port=8000)
