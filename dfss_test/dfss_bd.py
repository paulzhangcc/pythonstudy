from aip import AipOcr


def verifying_code(url='https://paulzhangcc.oss-cn-beijing.aliyuncs.com/1.png'):
    """ 你的 APPID AK SK """
    APP_ID = '11086206'
    API_KEY = 'YTDMZxqm63fokY7UTOxSVowX'
    SECRET_KEY = 'HkTXYq0BzQ85kkvTAxemQi4SVNwaNUDf'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    """ 如果有可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "false"
    options["detect_language"] = "true"
    options["language_type"] = "CHN_ENG"

    """ 带参数调用通用文字识别, 图片参数为远程url图片 """
    result = client.basicGeneralUrl(url, options)
    print("识别图片百度云返回的结果:",result)
    return result

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def verifying_code_from_file(pic_temp='/temp/1.png'):
    """ 你的 APPID AK SK """
    APP_ID = '11086206'
    API_KEY = 'YTDMZxqm63fokY7UTOxSVowX'
    SECRET_KEY = 'HkTXYq0BzQ85kkvTAxemQi4SVNwaNUDf'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = get_file_content(pic_temp)
    """ 如果有可选参数 """
    options = {}
    options["detect_direction"] = "false"
    options["language_type"] = "CHN_ENG"
    options["probability"] = "true"

    """ 带参数调用通用文字识别（高精度版） """
    return client.basicAccurate(image, options)

