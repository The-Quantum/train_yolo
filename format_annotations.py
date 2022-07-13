from inspect import Attribute
import os
import cv2
from tqdm import tqdm
import numpy as np

PRESENT_DIR  = os.path.dirname(os.path.realpath(__file__))

def convert(filename_wihtout_extension, coords):
    """ Transform Open Images Dataset bounding boxes
        XMin, YMin, XMax, YMax annotaton format into
        the normalized yolo format.

    input :
    -----
    filename_wihtout_extension : str()
        Image file path without .jpg extension. File by default available in Label/ subdir
    coords : np.array()
        OID coordinate of bounding boxes. 

    return :
    ------
    coords : np.array()
        New bounding boxes coordinate in YOLO formats.    
    """
    
    image = cv2.imread(filename_wihtout_extension + ".jpg")

    coords[2] -= coords[0]
    coords[3] -= coords[1]

    x_diff = int(coords[2]/2)
    y_diff = int(coords[3]/2)

    coords[0] = coords[0]+x_diff
    coords[1] = coords[1]+y_diff

    coords[0] /= int(image.shape[1])
    coords[1] /= int(image.shape[0])
    coords[2] /= int(image.shape[1])
    coords[3] /= int(image.shape[0])

    return coords

def format_annotation(file_path, new_file_path):
    """Open the OID annotation file from Label/ directory. 
      - Replace class string name with the corresponding class number 
      - Map all coordinates to np.array and convert them to YOLO format
      - Report class number and YOLO cordinates format to a list to return
    
    input :
    -----
    file_path : str()
            OID annotation file path. File by default available in Label/ subdir
    new_file_path : str()
            The path to exploit to open the corresponding image. 

    return :
    ------
    annotations : list()
            List of the formated annotations    
    """
    if file_path.endswith(".txt"):

        filename_wihtout_extension = str.split(new_file_path, ".")[0]

        annotations = []
        with open(file_path) as f:
            for line in f:
                for class_type in classes:
                    line = line.replace(class_type, 
                                str(classes[class_type]))

                labels = line.split()

                coords = np.asarray(
                    [float(labels[1]), float(labels[2]), 
                        float(labels[3]), float(labels[4])])

                coords = convert(filename_wihtout_extension, coords)

                labels[1], labels[2], labels[3], labels[4] = \
                    coords[0], coords[1], coords[2], coords[3]

                newline = str(labels[0]) + " " \
                    + str(labels[1]) + " " \
                    + str(labels[2]) + " " \
                    + str(labels[3]) + " " + str(labels[4])
                    
                line = line.replace(line, newline)
                annotations.append(line)
    return annotations

# Map each class name to a number for yolo compatibility
classes = {}
with open("classes.txt", "r") as myFile:
    for num, line in enumerate(myFile, 0):
        line = line.rstrip("\n")
        classes[line] = num

# step into dataset directory
DATA_DIR = os.path.join(PRESENT_DIR, "OID/Dataset")

for DIR in os.listdir(DATA_DIR):
    current_data_dir = os.path.join(DATA_DIR, DIR) # train or validation
    if os.path.isdir(current_data_dir):

       # for all class folders step into directory to change annotations
       for data_class in os.listdir(current_data_dir):
           current_class_dir = os.path.join(current_data_dir, data_class) #Orange or Vehicle plate ...
           if os.path.isdir(current_class_dir):
                Label_dir = os.path.join(current_class_dir, "Label")  # Label dir

                for filename in tqdm(os.listdir(Label_dir)):
                    file_path = os.path.join(Label_dir, filename)
                    
                    new_file_path = os.path.join(current_class_dir, filename)
                    annotations = format_annotation(file_path, new_file_path)

                    with open(new_file_path, "w") as outfile:
                        for line in annotations:
                            outfile.write(line)
                            outfile.write("\n")