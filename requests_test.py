import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

response = requests.get("https://api.github.com/events")
print(response.text)
print(response.encoding)
print(response.json())

response = requests.get("https://www.meme2c.com/static/app/2.0.0/images/newlogo.png")
img = Image.open(BytesIO(response.content))
plt.figure("dog")
plt.imshow(img)
# plt.axis('off')
plt.show()

print(img.size)
print(img.mode)
ext = img.format.lower()
img.save("c:/logo" + "." + ext)

img = Image.open(BytesIO(requests.get('http://wsyc.603377.com.cn/validpng.aspx').content))
width, height = img.size
new_img=img.resize((width*3, height*3))
new_img.save("/1.png")
