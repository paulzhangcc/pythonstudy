# coding=utf-8
# 同步图片检测服务接口, 会实时返回检测的结果

from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkgreen.request.v20170825 import ImageSyncScanRequest
import json
import uuid
import datetime

# 请替换成你自己的accessKeyId、accessKeySecret, 您可以类似的配置在配置文件里面，也可以直接明文替换
clt = client.AcsClient('LTAII8NOKvwoEvIF', 'd0iICqgwutXUMzTQ7uKwsezxTTq1AF', 'cn-shanghai')
region_provider.modify_point('Green', 'cn-shanghai', 'green.cn-shanghai.aliyuncs.com')
request = ImageSyncScanRequest.ImageSyncScanRequest()
request.set_accept_format('JSON')

# 同步现支持单张图片，即一个task
task1 = {"dataId": str(uuid.uuid1()),
         "url": "http://wsyc.603377.com.cn/validpng.aspx",
         "time": datetime.datetime.now().microsecond
         }

request.set_content(bytearray(json.dumps({"tasks": [task1], "scenes": ["porn"]}), "utf-8"))

response = clt.do_action_with_exception(request)
print(response)
result = json.loads(response)
if 200 == result["code"]:
    taskResults = result["data"]
    for taskResult in taskResults:
        if (200 == taskResult["code"]):
            sceneResults = taskResult["results"]

            for sceneResult in sceneResults:
                scene = sceneResult["scene"]
                suggestion = sceneResult["suggestion"]
                # 根据scene和suggetion做相关的处理
                # do something
