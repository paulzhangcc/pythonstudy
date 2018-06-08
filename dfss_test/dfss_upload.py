import oss2
import requests
from io import BytesIO
from PIL import Image
import os


def upload_pic_to_oss_from_link(img_link, pic_temp='/temp/1.png'):
    print("获取图片的连接:", img_link)
    pic_name = '1.png'
    auth = oss2.Auth('LTAII8NOKvwoEvIF', 'd0iICqgwutXUMzTQ7uKwsezxTTq1AF')
    bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'paulzhangcc')
    exist = bucket.object_exists(pic_name)
    if exist:
        bucket.delete_object(pic_name)
        print('oss远程图片存在,执行删除操作ok')
    temp_img_save = pic_temp
    if os.path.exists(temp_img_save):
        # 删除文件，可使用以下两种方法。
        os.remove(temp_img_save)
    # img_link = 'https://www.meme2c.com/jcaptcha/register'
    img = Image.open(BytesIO(requests.get(img_link, verify=False).content))
    width, height = img.size
    new_img = img.resize((width * 2, height * 2))
    new_img.save(temp_img_save)
    result_ali_yun = bucket.put_object_from_file(pic_name, temp_img_save)
    print('上传oss图片响应结果:', result_ali_yun.status)
