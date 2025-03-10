from flask import Flask, jsonify
from flask_cors import CORS  # 导入 Flask-CORS
import pymongo
import yaml

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求

# 连接到 MongoDB 数据库，添加账号和密码

client = pymongo.MongoClient("mongodb://152.136.142.183:39002/")
db = client["openkylinOS"]
# 基线检测
baseline_collection = db["baseline"]
baselinerepair_collection = db["baselinerepair"]

# 内核漏洞
nbug_collection = db["nbug"]
nbugrepair_collection = db["nbugrepair"]

# 系统漏洞
xbug_collection = db["xbug"]
xbugrepair_collection = db["xbugrepair"]


# 基线检查
@app.route('/baseline', methods=['GET'])
def baseline():
    results = list(baseline_collection.find())
    for result in results:
        # 在这里根据需要处理数据格式
        result.pop('_id')  # 假设您不想将 MongoDB 的 _id 字段返回给前端
    return jsonify(results)
    
# 基线检测修复
@app.route('/baselinerepair', methods=['GET'])
def baselinerepair():
    results = list(baselinerepair_collection.find())
    for result in results:
        # 在这里根据需要处理数据格式
        result.pop('_id')  # 假设您不想将 MongoDB 的 _id 字段返回给前端
    return jsonify(results)
    
# 内核漏洞检测
@app.route('/nbug', methods=['GET'])
def nbug():
    results = list(nbug_collection.find())
    for result in results:
        # 在这里根据需要处理数据格式
        result.pop('_id')  # 假设您不想将 MongoDB 的 _id 字段返回给前端
    return jsonify(results)
    
    
# 内核漏洞修复
@app.route('/nbugrepair', methods=['GET'])
def nbugrepair():
    results = list(nbugrepair_collection.find())
    for result in results:
        # 在这里根据需要处理数据格式
        result.pop('_id')  # 假设您不想将 MongoDB 的 _id 字段返回给前端
    return jsonify(results)
    
    
# 系统漏洞检测
@app.route('/xbug', methods=['GET'])
def xbug():
    results = list(xbug_collection.find())
    for result in results:
        # 在这里根据需要处理数据格式
        result.pop('_id')  # 假设您不想将 MongoDB 的 _id 字段返回给前端
    return jsonify(results)
    
    
# 系统漏洞修复
@app.route('/xbugrepair', methods=['GET'])
def xbugrepair():
    results = list(xbugrepair_collection.find())
    for result in results:
        # 在这里根据需要处理数据格式
        result.pop('_id')  # 假设您不想将 MongoDB 的 _id 字段返回给前端
    return jsonify(results)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=39010)