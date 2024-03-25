# Import dependencies

import cv2
import uuid
import os
import time

# Define Images to Collect

labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']
number_imgs = 5

# Setup Folders

IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')

# if not os.path.exists(IMAGES_PATH):
#     os.makedirs(IMAGES_PATH)
# for label in labels:
#     path = os.path.join(IMAGES_PATH, label)
#     if not os.path.exists(path):
#         os.makedirs(path)

# Capture Images

for label in labels:
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()