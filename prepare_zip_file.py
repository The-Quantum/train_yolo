import os
from zipfile import ZipFile

PRESENT_DIR  = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(PRESENT_DIR, "OID/Dataset")

for data_set_dir in os.listdir(DATA_DIR):
    if data_set_dir == "train" :
        zip_file_name = "obj.zip"
    elif data_set_dir == "validation":
        zip_file_name = "test.zip"
   
    data_set_type_path = os.path.join(DATA_DIR, data_set_dir)
    zip_file_name = os.path.join(PRESENT_DIR, zip_file_name)

    with ZipFile(zip_file_name, "w") as zip_obj:

        for data_class_dir in os.listdir(data_set_type_path):
            data_class_dir_path = os.path.join(data_set_type_path, data_class_dir)
            print(data_class_dir_path)

            if os.path.isdir(data_class_dir_path):
                os.chdir(data_class_dir_path)

                #onlyfiles = [f for f in os.listdir(data_class_dir_path) 
                #            if os.path.isfile(os.path.join(data_class_dir_path, f))]
                for f in os.listdir(os.getcwd()):
                    if f.endswith(".txt") or f.endswith(".jpg"):
                        zip_obj.write(f)
            
            os.chdir(PRESENT_DIR)
