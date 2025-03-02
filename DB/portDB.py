import pymongo
import json
def portAuto():
    # 建立与 MongoDB 的连接
    client = pymongo.MongoClient("mongodb://152.136.142.183:39002/")  # 请根据实际情况修改连接字符串

    # 选择数据库和集合
    db = client["openkylinOS"]  # 替换为您的数据库名称
    collection = db["portAuto"]  # 替换为您的集合名称

    # 读取文件
    with open("/home/nuc/桌面/NUC_openkylin/接口自动化/security_check_log.txt", "r") as file:
        lines = file.readlines()

    # 处理每一行数据并插入到 MongoDB
    for line in lines:
        # 去除换行符并将每行数据转换为字典
        data = json.loads(line.strip())
        collection.insert_one(data)
def info():
    print("\n接口自动化检测上传成功，结果保存在【 http://152.136.142.183:39010/portAuto 】中 ")

portAuto()
info()
