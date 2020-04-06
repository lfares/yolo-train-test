import os
import cv2 as cv
from pydarknet import Detector, Image

class Yolo():

    def __init__(self, weights_file='yolov3-2obj_final', darknet_files_path="darknet_files"):
        self.pinga_color = (55, 145, 6) # green
        self.emily_color = (6, 81, 156) # blue

        # Initialize Yolo
        self.net = Detector(bytes(os.path.join(darknet_files_path,"yolov3-2obj.cfg"), encoding="utf-8"), 
                            bytes(os.path.join(darknet_files_path, weights_file+".weights"), encoding="utf-8"), 0, 
                            bytes(os.path.join(darknet_files_path,"obj.data"), encoding="utf-8"))

    def detect (self, frame):
        image_output = Image(frame)
        results = self.net.detect(image_output, thresh=0.85,nms=0.15)

        for cat, score, bounds in results:
            x, y, w, h = bounds
            if cat.decode("utf-8") == "pinga":
                cv.rectangle(image_output, (int(x-w/2), int(y-h/2)), (int(x+w/2), int(y+h/2)), 
                    self.pinga_color, thickness=3)
            elif cat.decode("utf-8") == "emily":
                cv.rectangle(image_output, (int(x-w/2), int(y-h/2)), (int(x+w/2), int(y+h/2)), 
                    self.emily_color, thickness=3)
            cv.putText(image_output, str(cat.decode("utf-8")), (int(x),int(y)),
                        cv.FONT_HERSHEY_COMPLEX, 2, (255,255,255))
