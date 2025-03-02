import pymongo
import json

def deleteCollections():
    # 连接 MongoDB 服务器
    client = pymongo.MongoClient("mongodb://152.136.142.183:39002/")

    # 选择要操作的数据库
    db = client["openkylinOS"]  # 将 your_database_name 替换为实际的数据库名称
    db["nbug"].drop()
def nbug():
    # 连接到 MongoDB 数据库
    client = pymongo.MongoClient("mongodb://152.136.142.183:39002/")

    # 选择数据库
    db = client["openkylinOS"]

    # 读取 JSON 数据
    with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/result/内核漏洞检测报告.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    # 选择集合
    collection = db["nbug"]

    # 逐个插入数据到集合
    for item in data:
        collection.insert_one(item)
    # 关闭连接
    client.close()
def info():
    print("\n内核漏洞扫描结果上传成功，结果保存在【 http://152.136.142.183:39010/nbug 】中 ")
deleteCollections()
nbug()
info()