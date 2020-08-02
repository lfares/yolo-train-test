# Training and Testing Yolo 

This project has the porpouse of training a neural network to detect two different classes (Emily and Pinga) using Yolo. 

## Training the classes

The images used for training are on the folder darknet_files, as well as the files needed for a new training.

A tutorial on how to use them can be found at [AlexyAB repo](https://github.com/AlexeyAB/darknet).

## Testing

To test it is necessary to have both OpenCV and [Yolo3-4-Py](https://github.com/madhawav/YOLO3-4-Py) installed.

Besides that, download the weights file [here](https://drive.google.com/file/d/1-xAbcH3EV6xCiuRk1tljXR4LicnGtQ4o/view?usp=sharing) and put on the darknet_files folder or change the path on the Yolo file.

### Images
To test the output for images use the '--IMAGE' before the path to the image:

    python3 demo.py --IMAGE [path_to_image]

### Videos

The test for videos follow the same thing using '--VIDEO' before the path to the video:

    python3 demo.py --VIDEO [path_to_video]

Here are two examples of the output:

![Emily picture](/output/emily41.jpg)

![Pinga picture](/output/pinga57.jpg)


