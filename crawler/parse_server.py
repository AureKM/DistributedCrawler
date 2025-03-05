# 模拟数据解析模块

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/parse_data', methods=['POST'])
def parse_data():
    data = request.json
    print(f"📡 解析模块收到数据: {data}")
    return jsonify({"status": "success", "data": data})

app.run(port=5001)