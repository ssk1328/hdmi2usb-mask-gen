from PIL import Image

col = Image.open("d1.jpg")
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
bw.save("d2.jpg")