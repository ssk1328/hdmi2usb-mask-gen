from PIL import Image

col = Image.open("b1.jpg")
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
bw.save("b2.jpg")