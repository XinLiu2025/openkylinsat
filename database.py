import json
import yaml
import pymongo
class Database:
    def __init__(self):
        pass
    def deleteallcollections(self):
        # 连接 MongoDB 服务器
        client = pymongo.MongoClient("mongodb://152.136.142.183:39002/")  # 请将 localhost 替换为您的实际 MongoDB 服务器地址

        # 选择要操作的数据库
        db = client["openkylinOS"]  # 将 your_database_name 替换为实际的数据库名称

        # 获取数据库中的所有集合名称
        collection_names = db.list_collection_names()

        # 循环删除每个集合
        for collection_name in collection_names:
            db[collection_name].drop()
    # 1基线检测
    def baseline(self):
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

    # 2基线检测修复
    def baselinerepair(self):
        # 连接到 MongoDB 数据库
        client = pymongo.MongoClient("mongodb://152.136.142.183:39002/")

        # 选择数据库
        db = client["openkylinOS"]

        # 读取 JSON 数据
        with open('/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result/recover_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 选择集合
        collection = db["baselinerepair"]

        # 插入数据到集合
        collection.insert_one(data)
        # 关闭连接
        client.close()

    # 3内核漏洞扫描
    def nbug(self):
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
    # 4内核漏洞修复
    def nbugrepair(self):
        # 连接到 MongoDB 数据库
        client = pymongo.MongoClient("mongodb://152.136.142.183:39002/")

        # 选择数据库
        db = client["openkylinOS"]

        # 读取 JSON 数据
        with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/result/内核漏洞检测修复报告.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 选择集合
        collection = db["nbugrepair"]

        # 逐个插入数据到集合
        for item in data:
            collection.insert_one(item)
        # 关闭连接
        client.close()
    # 5系统漏洞扫描
    def xbug(self):
        # 连接到 MongoDB 数据库
        client = pymongo.MongoClient("mongodb://152.136.142.183:39002/")

        # 选择数据库
        db = client["openkylinOS"]

        # 读取 JSON 数据
        with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/result/系统漏洞检测报告.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        # 选择集合
        collection = db["xbug"]

        # 逐个插入数据到集合
        for item in data:
            collection.insert_one(item)
        # 关闭连接
        client.close()
    # 6系统漏洞修复
    def xbugrepair(self):
        # 连接到 MongoDB 数据库
        client = pymongo.MongoClient("mongodb://152.136.142.183:39002/")

        # 选择数据库
        db = client["openkylinOS"]

        # 读取 JSON 数据
        with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/result/系统漏洞检测修复报告.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        # 选择集合
        collection = db["xbugrepair"]

        # 插入数据到集合
        # 逐个插入数据到集合
        for item in data:
            collection.insert_one(item)
        # 关闭连接
        client.close()
def info():
    print("\n所有数据一键上传完毕！！！")
# if __name__ == '__main__':
#     db = Database()
#     a = int(input('请输入一个数字（1 代表清空数据库，2 代表先清空后写入数据：）：'))
#     if a == 1:
#         db.deleteallcollections()
#     elif a == 2:
#         # 删除数据库当中的所有集合
#         db.deleteallcollections()
#         # 1、基线检测
#         db.baseline()
#         # 2、基线检测修复
#         db.baselinerepair()
#         # 3、内核漏洞扫描
#         db.nbug()
#         # 4、内核漏洞修复
#         db.nbugrepair()
#         # 5、系统漏洞检测
#         db.xbug()
#         # 6、系统漏洞修复
#         db.xbugrepair()
#     else:
#         print("无效输入！")
if __name__ == '__main__':
        db = Database()
        # 删除数据库当中的所有集合
        db.deleteallcollections()
        # 1、基线检测
        db.baseline()
        # 2、基线检测修复
        db.baselinerepair()
        # 3、内核漏洞扫描
        db.nbug()
        # 4、内核漏洞修复
        db.nbugrepair()
        # 5、系统漏洞检测
        db.xbug()
        # 6、系统漏洞修复
        db.xbugrepair()
        info()

