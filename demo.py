import sys
import cv2
import os
from Yolo import Yolo

type = sys.argv[1]
path = sys.argv[2]

detector = Yolo()

if type == "--VIDEO":
    cap = cv2.VideoCapture(path)
    r, frame = cap.read()
    while r:
        output = detector.detect(frame)
        cv2.imshow("Output", output)
        k = cv2.waitKey(1)
        if k == 0xFF & ord("q"):
            break

        r, frame = cap.read()

elif type == "--IMAGE":
    image_input = cv2.imread(path)
    image_output = detector.detect(image_input)

    if not os.path.isdir("output"):
        os.mkdir("output")
    save_path = "output/" + path.split('/')[2]
    cv2.imwrite(save_path, image_output)

    cv2.imshow("Output", image_output)
    cv2.waitKey(0)

else:
    print("Type invalid, choose --VIDEO or --IMAGE.")