# Training and Testing Yolo 

This project has the porpouse of training a neural network to detect two different classes (Emily and Pinga) using Yolo. 

Now it is only working with images using the file demo.py

## Training the classes

The images used for training are on the folder darknet_files, as well as the files needed for a new training.

A tutorial for how to use them can be found at [AlexyAB repo](https://github.com/AlexeyAB/darknet).

## Testing

To test it is necessary to have both OpenCV and [Yolo3-4-Py](https://github.com/madhawav/YOLO3-4-Py) installed.

Then just run:

    python3 demo.py --IMAGE [path_to_image]

Here are two examples of the output:

![Emily picture](/output/emily41.jpg)

![Pinga picture](/output/pinga57.jpg)


