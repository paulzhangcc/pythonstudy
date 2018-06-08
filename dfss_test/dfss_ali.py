# coding=utf-8
# 同步图片检测服务接口, 会实时返回检测的结果

from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkgreen.request.v20170825 import ImageSyncScanRequest
import json
import uuid
import datetime
import oss2
import requests
from io import BytesIO
from PIL import Image
import time
import random
from dfss_test.dfss_upload import upload_pic_to_oss_from_link

requests.packages.urllib3.disable_warnings()


def verifying_code(url='https://paulzhangcc.oss-cn-beijing.aliyuncs.com/1.png'):
    # 请替换成你自己的accessKeyId、accessKeySecret, 您可以类似的配置在配置文件里面，也可以直接明文替换
    clt = client.AcsClient('LTAII8NOKvwoEvIF', 'd0iICqgwutXUMzTQ7uKwsezxTTq1AF', 'cn-shanghai')
    region_provider.modify_point('Green', 'cn-shanghai', 'green.cn-shanghai.aliyuncs.com')
    request = ImageSyncScanRequest.ImageSyncScanRequest()
    request.set_accept_format('JSON')

    # 同步现支持单张图片，即一个task
    task1 = {"dataId": str(uuid.uuid1()),
             "url": url,
             "time": datetime.datetime.now().microsecond
             }

    request.set_content(bytearray(json.dumps({"tasks": [task1], "scenes": ["ocr"]}), "utf-8"))

    response = clt.do_action_with_exception(request)
    result = json.loads(response)
    print("识别图片阿里云返回的结果:", result)
    if 200 == result["code"]:
        taskResults = result["data"]
        for taskResult in taskResults:
            if (200 == taskResult["code"]):
                print(taskResult['results'][0])
            if (taskResult['results'][0]['label'] == 'ocr'):
                return taskResult['results'][0]['ocrData'][0]
    return ''


def get_success_pic_code(img_link='http://wsyc.603377.com.cn/validpng.aspx'):
    upload_pic_to_oss_from_link(img_link)
    code = verifying_code()
    while (True):
        if (len(code) != 4):
            time.sleep(random.randint(2, 4))
            upload_pic_to_oss_from_link(img_link)
            time.sleep(random.randint(1, 3))
            code = verifying_code()
            print('====================================')
        else:
            break
    print("成功识别的图形验证码:", code, ',识别图片的连接:', 'https://paulzhangcc.oss-cn-beijing.aliyuncs.com/1.png')
    return code


if __name__ == '__main__':
    get_success_pic_code()
