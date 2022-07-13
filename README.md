# Training yolo on custum dataset
 This tutorail focuses on the training ```yolov4``` on custum dataset on google colab in order to benefite from free GPU. For this purpose, we choose the retrain ```yolov4``` to detect vehicle registration plate which is a class of dataset present on [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html). 

 ## 1. Data preparation
  [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html) is an online open source dataset provided by google that consist of ~9 millions images annotated labels, object bounding boxes, object segmentation masks and more. Interestingly, is containts up to 600 objects classes which is quite interesting for developping different type of computer vision models.

  ### 1.1 Download the interested dataset
  Differents modules were proposed including [oidv6](https://pypi.org/project/oidv6/) and [OIDv4_ToolKit](https://github.com/EscVM/OIDv4_ToolKit) to interact with [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html) and download single or multiple dataset classes. For this tutorial, we incorporated the ```main.py``` file and ```modules``` from [OIDv4_ToolKit](https://github.com/EscVM/OIDv4_ToolKit) as it was enough to download the needed dataset. The data class we are interested in is known on [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html)as ```Vehicle registration plate```. 

   To download, move into the main directory where there is the ```main.py``` and run the following line of code.
    ```bash
     python main.py downloader --classes "Vehicle registration plate" --type_csv train --limit 1000
    ```
   This will create ```OID``` directory where where the downloaded dataset is store.
   Next, run again the same line of code while stting the argument ```--type_csv``` to ```validation``` and ```--limit``` to 100. This will download 100 images of the the validation set.  
        ```bash
        python3 main.py downloader --classes "Vehicle registration plate" --type_csv validation --limit 100
        ```
   For more detail regarding this code we suggest to refer to [OIDv4_ToolKit](https://github.com/EscVM/OIDv4_ToolKit) repository.  

   ### 1.2 adapt the annotations to the yolo formate   
   At this step, the first action consist of editing the ```classes.txt``` to make sure it contains the right name of the data class we are interested in. In this case it should contain ```Vehicle registration plate```.

    Next, run the folowing line of code.
    ```bash
     python format_annotations.py 
    ```
  ### 1.3 Prepare zip files
  The training is to be conducted on google colab is practical to compress the training and test sets as well as the corresponding annotations into a ```obj.zip``` and ```test.zip``` files respectively. 
    
   #### Manual mode
   Both trainset and testset to zip correspond to the output generated after executing ```python format_annotations.py```. The process is as simple as navigating manuallyt into ```OID/Dataset/train``` and ```OID/Dataset/validation``` subdirs. In principle, one is expected to find a single class dir  name ```Vehicle registration plate``` en each of both train and validation subdirs. Hence, remane ```Vehicle registration plate``` from train subdir to ```obj/``` and remane ```Vehicle registration plate``` from validation subdir to ```test/```. Then navigate into both ```obj/``` and ```test/``` and delete the ```Label/``` subdir. Next, manually zip both ```obj/``` and ```test/``` directories to ```obj.zip``` and ```test.zip``` file.

   #### Preferable mode
   To compress both train and test sets, simply run the following line of code.
        ```bash
            python prepare_zip_file.py
        ```
   This will generate both ```obj.zip``` and ```test.zip``` files into ```train_yolo/``` root directory.

 ## 2. Training procedure on google colab
  First, open your google drive session. Create in ```My Drive/``` a directrory name ```train_yolo``` and upload into it both ```obj.zip``` and ```test.zip``` files. The name of ```train_yolo``` is not of much important here. It can be any other name as fare as one remenber it when refering into during training.

  Now, open your `google colab` session and upload the ```train_yolo.ipynb``` notebook file and start following the instructions.