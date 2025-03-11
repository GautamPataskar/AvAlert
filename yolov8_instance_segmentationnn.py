# -*- coding: utf-8 -*-
"""Copy of yolov8_instance_segmentationt.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SXe8dYbqazbWo_7Bn9PYd-pPUgdICK0-
"""

from google.colab import drive
drive.mount('/content/drive')

!nvidia-smi

import os
HOME = os.getcwd()
print(HOME)

# Pip install method (recommended)

!pip install ultralytics==8.0.28

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()

# Git clone method (for development)

# %cd {HOME}
# !git clone github.com/ultralytics/ultralytics
# %cd {HOME}/ultralytics
# !pip install -qe ultralytics

# from IPython import display
# display.clear_output()

# import ultralytics
# ultralytics.checks()

from ultralytics import YOLO

from IPython.display import display, Image

"""## CLI Basics

If you want to train, validate or run inference on models and don't need to make any modifications to the code, using YOLO command line interface is the easiest way to get started. Read more about CLI in [Ultralytics YOLO Docs](https://v8docs.ultralytics.com/cli/).

```
yolo task=detect    mode=train    model=yolov8n.yaml      args...
          classify       predict        yolov8n-cls.yaml  args...
          segment        val            yolov8n-seg.yaml  args...
                         export         yolov8n.pt        format=onnx  args...
```
"""

!pip install fastapi kaleido python-multipart uvicorn

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="ljPIedYa18jbN3o0BXDi")
project = rf.workspace("shreyas-aher").project("yolov9-dyyt0")
version = project.version(1)
dataset = version.download("yolov8")

ROOT_PATH = "/content/Yolov9-1"

!pwd

# Commented out IPython magic to ensure Python compatibility.
# %cd "/content/Yolov9-1"

!pwd

!ls

"""## Custom Training"""

!yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=25 save=true imgsz=640

!ls runs/segment/train2/

Image(filename=f'runs/segment/train2/confusion_matrix.png', width=600)

Image(filename=f'runs/segment/train2/results.png', width=1200)

Image(filename=f'runs/segment/train2/val_batch0_pred.jpg', width=1200)

"""## Validate Custom Model"""

!yolo task=segment mode=val model=runs/segment/train2/weights/best.pt data=data.yaml

!yolo task=segment mode=predict model=runs/segment/train2/weights/best.pt conf=0.25 source=test/images save=true

import glob
from IPython.display import Image, display

for image_path in glob.glob(f'runs/segment/predict/*.jpg')[:3]:
      display(Image(filename=image_path, height=600))
      print("\n")

