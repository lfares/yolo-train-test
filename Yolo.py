import os
import cv2
from pydarknet import Detector, Image

class Yolo():

    def __init__(self, weights_file='yolov3-2obj_final', darknet_files_path="darknet_files"):
        self.pinga_color = (6, 145, 55) # green
        self.emily_color = (156, 81, 6) # blue

        # Initialize Yolo
        self.net = Detector(bytes(os.path.join(darknet_files_path,"yolov3-2obj.cfg"), encoding="utf-8"), 
                            bytes(os.path.join(darknet_files_path, weights_file+".weights"), encoding="utf-8"), 0, 
                            bytes(os.path.join(darknet_files_path,"obj.data"), encoding="utf-8"))

    def detect (self, frame):
        image_output = Image(frame)
        results = self.net.detect(image_output, thresh=0.85,nms=0.15)
        del image_output

        for cat, score, bounds in results:
            x, y, w, h = bounds
            if cat.decode("utf-8") == "pinga":
                cv2.rectangle(frame, (int(x-w/2),int(y-h/2)),(int(x+w/2),int(y+h/2)), self.pinga_color, 8)
                self.text_with_background(frame, self.pinga_color, "pinga", bounds)
            elif cat.decode("utf-8") == "emily":
                cv2.rectangle(frame, (int(x-w/2),int(y-h/2)),(int(x+w/2),int(y+h/2)), self.emily_color, 8)
                self.text_with_background(frame, self.emily_color, "emily", bounds)
        

        return frame

    def text_with_background(self, img, rectangle_bgr, text, bounds):
        font = cv2.FONT_HERSHEY_SIMPLEX 
        font_scale = 3
        x, y, w, h = bounds
        # get the width and height of the text box
        (text_width, text_height) = cv2.getTextSize(text, font, font_scale, thickness=4)[0]
        # set the text start position
        text_offset_x = int(x-w/2) 
        text_offset_y = int(y-h/2)
        # make the coords of the box with a small padding of two pixels
        box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width + 50, text_offset_y - text_height - 50))
        cv2.rectangle(img, box_coords[0], box_coords[1], rectangle_bgr, cv2.FILLED)
        cv2.putText(img, text, (text_offset_x+25, text_offset_y-25), font, font_scale, color=(255, 255, 255), thickness=3)