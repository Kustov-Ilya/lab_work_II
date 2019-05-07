import os
from net import HopfieldNet
from util import printshape
from parse import parse, parse_shape

SHAPE_SIDE_HEIGHT = 5
SHAPE_SIDE_WIDHT = 3

knows_shapes_dir = "known_shapes"
modified_shape_path = "modified_shapes/modified.txt"


def main():
    shapes = parse(knows_shapes_dir)
    shape = parse_shape(modified_shape_path)

    print("Known Shapes:")
    for o in shapes:
        printshape(o, SHAPE_SIDE_HEIGHT, SHAPE_SIDE_WIDHT)

    print("Teaching...")
    hopfield = HopfieldNet(SHAPE_SIDE_HEIGHT, SHAPE_SIDE_WIDHT)
    for o in shapes:
        hopfield.teach(o)

    print("Modified shape:") 
    printshape(shape, SHAPE_SIDE_HEIGHT, SHAPE_SIDE_WIDHT)

    print("Shape recognizing...")
    rezult, reshare = hopfield.recognize(shape)
    print(rezult)
    printshape(reshare, SHAPE_SIDE_HEIGHT, SHAPE_SIDE_WIDHT)


if __name__ == '__main__':
    main()
    os.system("pause")

