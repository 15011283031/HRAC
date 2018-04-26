import json  # json数据格式，用于写入数据库链接配置信息


def get_base_dir():
    with open('/usr/bin/assforhr.json') as connFile:
        readConnDict = json.load(connFile)
        base_dir = readConnDict['BASE_DIR']
    return base_dir