from PIL import Image
from PIL import ImageDraw
from io import BytesIO
import requests
import matplotlib.pyplot as plt


sourceFileName = "c:/zjf.jpg"
# image = Image.new('RGB', (500, 500), (255, 255, 255))
# image.save(sourceFileName)

avatar = Image.open(sourceFileName)
drawAvatar = ImageDraw.Draw(avatar)
xSize, ySize = avatar.size
# 1:
# drawAvatar.line([0,0, xSize, 0.33 * ySize], fill=(255, 100, 0), width=3)
# del drawAvatar
# avatar.show()
# 2:
# drawAvatar.arc([0, 0, 100, 100], 0, 360, fill=(255, 100, 255))
# del drawAvatar
# avatar.show()
