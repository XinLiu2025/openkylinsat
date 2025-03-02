import pymongo


def deleteallcollections():
    # 连接 MongoDB 服务器
    client = pymongo.MongoClient("mongodb://152.136.142.183:39002/")  # 请将 localhost 替换为您的实际 MongoDB 服务器地址

    # 选择要操作的数据库
    db = client["openkylinOS"]  # 将 your_database_name 替换为实际的数据库名称

    # 获取数据库中的所有集合名称
    collection_names = db.list_collection_names()

    # 循环删除每个集合
    for collection_name in collection_names:
        db[collection_name].drop()
def info():
    print("\n已全部清空！！！")
deleteallcollections()
info()