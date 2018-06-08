import dfss_test.dfss_upload as upload
import dfss_test.dfss_ali  as ali_see
import dfss_test.dfss_bd   as bd_see

import time

def run():
    upload.upload_pic_to_oss_from_link("http://wsyc.603377.com.cn/validpng.aspx")
#    upload.upload_pic_to_oss_from_link("https://uac.10010.com/cust/verifyCode/verifyCode.action")
    temp_url = 'https://paulzhangcc.oss-cn-beijing.aliyuncs.com/1.png?d='+str(time.time())
    result_ali = ali_see.verifying_code(temp_url)
    result_bd = bd_see.verifying_code(temp_url)
    result_bd_file = bd_see.verifying_code_from_file()
    print("============================================")
    print("图片连接地址:", temp_url)
    print("aliyun:", result_ali)
    print("baidu:", result_bd)
    print("baidu_g:", result_bd_file)
if __name__ == '__main__':
    run()
