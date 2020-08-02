import sys
import cv2
import os
from Yolo import Yolo

type = sys.argv[1]
path = sys.argv[2]

detector = Yolo()

if type == "--VIDEO":
    cap = cv2.VideoCapture(path)
    print(path)
    if not cap.isOpened():
        print("Error opening video stream or file")

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    if not os.path.isdir("output"):
        os.mkdir("output")
    save_path = "output/" + path.split('/')[2].split('.')[0] + '.avi'

    out = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frame_height))

    r, frame = cap.read()
    while r:
        output = detector.detect(frame)
        print("FRAME NUMBER: ", cap.get(cv2.CAP_PROP_POS_FRAMES))
        out.write(output)
        # cv2.imshow("Output", output)
        # k = cv2.waitKey(1)
        # if k == 0xFF & ord("q"):
        #     break

        r, frame = cap.read()
    cap.release()
    out.release()
    # cv2.destroyAllWindows() 


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