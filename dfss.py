import requests
import time
import json
requests.packages.urllib3.disable_warnings()


loginheader = {
'Accept-Encoding': 'gzip',
'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10)',
'Content-Type': 'application/json; charset=utf-8',
'ApiChecksum': '9d594e4ebe72593c2739c4eb8ec20dac',
'ApiKey': '708522cecbed4a0eb2dc3cff8afd6512',
'AppOwnerId': '1',
'ClientVersion': '2.3.3',
'ClientVersionCode': '45',
'DeviceId': '6f43f8ed3c6c45eaabea2c4eb231559e',
'DeviceModel': 'HUAWEI,HUAWEI,EVA-AL10',
'DeviceSystem': 'android 7.0',
'Noncestr': '641063',
'PushClientId':'' ,
'TimeStamp': '1523436633'
}
header = {
    'Accept-Encoding': 'gzip',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10)',
    'ApiChecksum': 'd7e045445228036a6ef6497549d75c16',
    'ApiKey': '708522cecbed4a0eb2dc3cff8afd6512',
    'AppOwnerId': '1',
    'AuthToken': 'c1b36e5a45e74735bcabcb31ac9f8a2e',
    'ClientVersion': '2.3.3',
    'ClientVersionCode': '45',
    'DeviceId': 'ccdc046230684678bebb1df6eae50153',
    'DeviceModel': 'HUAWEI,HUAWEI,EVA-AL10',
    'DeviceSystem': 'android 7.0',
    'Noncestr': '590127',
    'PushClientId': '140fe1da9e8bfac5c74',
    'TimeStamp': '1523522269',
    'Content-Type': 'application/json; charset=utf-8'
}
loginparam = {"trainingTimeSlotId":"06","datingCarDate":"2018-04-14","lessonId":"001"}
def login():
    return requests.post(
        'https://api.dfssclub.cn/api/v2/User/MixedLogin',data = json.dumps(loginparam),
        headers=header, timeout=10).json()

if __name__ == '__main__':
    print(login())
