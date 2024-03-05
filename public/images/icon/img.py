import cv2
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

img = cv2.imread(os.path.join(current_dir, 'logo.png'))
if img is None:
    print('Image load failed!')
    exit()

# resize image 32*32 48*48 72*72 128*128 144*144 180*180 192*192 256*256 512*512
for i in [32, 48, 72, 96, 128, 144, 180, 192, 256, 512]:
    img1 = cv2.resize(img, (i, i), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(os.path.join(current_dir, f'{i}.png'), img1)

