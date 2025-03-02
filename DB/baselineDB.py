import pymongo
import json


def deleteCollections():
    # 连接 MongoDB 服务器
    client = pymongo.MongoClient("mongodb://152.136.142.183:39002/")

    # 选择要操作的数据库
    db = client["openkylinOS"]  # 将 your_database_name 替换为实际的数据库名称
    db["baseline"].drop()

def baseline():
    # 连接到 MongoDB 数据库
    client = pymongo.MongoClient("mongodb://152.136.142.183:39002/")
    # 选择数据库
    db = client["openkylinOS"]
    # 读取 JSON 数据
    with open('/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 选择集合
    collection = db["baseline"]

    # 插入数据到集合
    collection.insert_one(data)
    # 关闭连接
    client.close()
def info():
    print("\n基线检测结果上传成功，结果保存在【 http://152.136.142.183:39010/baseline 】中 ")
deleteCollections()
baseline()
info()