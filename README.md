# SlothExtensionTextAnnotation
**Special configuration file for annotation tool SLOTH: https://github.com/cvhciKIT/sloth**

**TextRectItem:** Extented RectItem. 

1. detectionconfig.py -- Annotation Configuration for text detection
2. textAnnoConfig.py  -- Annotation Configuration for text recognition

**Author:** Yiye Lin 

**version:** 1.1

TOOL：SLOTH 
===
https://cvhci.anthropomatik.kit.edu/~baeuml/projects/a-universal-labeling-tool-for-computer-vision-sloth/

**Document:** http://sloth.readthedocs.org/en/latest/index.html ***!Instructions for sloth GUI Here!***

**Prerequisite:** python 2.7, Numpy

**Packages:** python-qt4, python-numpy
    
**Environment:** Linux

---
#Content Table

1. **[Usage of sloth](#usage-of-sloth)**
2. **[Naming criterion of files](#naming-criterion-of-files)**
3. **[Usage of text detection config file](#usage-of-text-detection-config-file)**
4. **[Usage of json to clipped images script](#usage-of-json-to-clipped-images-script)**
5. **[Usage of text recognition config file](#usage-of-text-recognition-config-file)**

#Important Sections
1. **[Naming criterion of files](#naming-criterion-of-files)**
2. **[Description for bounding boxes' class](#classes-and-hotkeys)**

#Usage of sloth

a. Create an anotation file and add images
---
    sloth appendfiles “output_file_name_here”.json “image_file_path_here”/*.png
E.g.

    sloth appendfiles b.json ../video_shots/youtube_001/*.png
    
b.Edit annotation file
---
    Sloth -c “config_file_name_here”.py  “output_file_name_here”.json
E.g. 

    sloth -c textAnnoConfig.py b.json

#Naming criterion of files
original frames:

    [path]/[any name e.g. youtube]\_[3digits-video-number]/[frame-number].png

json files:

    [path]/[any name e.g. youtube]\_[3digits-video-number].json
    
lists[original image & json annotation]: 

    [path]/[any name e.g. youtube]\_[3digits-video-number].list
    
annotations\[per frame\] \(add new key pairs { "imgname" , [bounding box]} for section 4 below): 

    [path]/[any name e.g. youtube]\_[3digits-video-number]/youtube\_[video-number]\_[frame-number].json
images[per bounding box]: 

    [path]/[any name e.g. youtube]\_[3digits-video-number]/youtube\_[video-number]\_[frame-number]\_[annotation-number]\_[class].png



#Usage of text detection config file

###File name: detectionconfig.py

###a.To add an annotation
---
1. Choose a picture from “Annotations” section,
2. Click one of Button in “Labels” section (or press a hotkey),
3. Draw box and enter the text

###b.To edit an annotation

1. Choose a picture from “Annotations” section,
2. Choose a annotation of the picture in “Annotations” section,
3. If step b succeeded, the border of the annotation will became dash border
4. `To move the box`, push and drag using left button of mice
5. `To adjust the size of the box`, push and drag using right button of mice
6. `To only change the class of text`, press the "change-class-hotkeys"

###Classes and hotkeys
| Classes | Hotkeys  | "Change-class" hotkeys | Description                                                                     |
|:-------:|:--------:|:----------------------:| ------------------------------------------------------------------------------- |
|    0    | 1        | q -or- Q               | text hard to be clarified (low contrast ratio -or-  bad background )            |
|    1    | 2        | w -or- W               | text can be clarify (medium contrast ratio -or- background is not good enough ) |
|    2    | 3        | e -or- E               | text canbe esily clarify (high contrast ratio -and- good background)            |
|    do   | not      | annotate               | 0 low contrast ratio -or- extremely bad background                              |

###Remember to click save button after edition!!!!

###Output: json file

###Format example: 
```json
{
        "annotations": [
            {
                "class": "0",
                "height": 41.26544413225945,
                "width": 54.73987486932375,
                "x": 30.317469158394694,
                "y": 21.895949947729502,
            },
            {
                "class": "1",
                "height": 47.160507579725085,
                "width": 64.84569792212199,
                "x": 50.52911526399116,
                "y": 40.42329221119292
            }
        ],
        "class": "image",
        "filename": "..example"
    },
```
#Usage of json to clipped images script
### File name: 
### Usage
### output format


#Usage of text recognition config file

To add an annotation
---
1. Choose a picture from “Annotations” section,
2. Click one of Button in “Labels” section,
3. Draw box and enter the text

To edit an annotation
---
1. Choose a picture from “Annotations” section,
2. Choose a annotation of the picture in “Annotations” section,
3. If step b succeeded, the border of the annotation will became dash border
4. To move the box, push and drag using left button of mouse
5. To adjust the size of the box, push and drag using right button of mouse
6. To only change the text, just simply click the left/right button

Hotkeys
---
* DigitText: **1**
* Text: **2** 
* HasText: **3**

Remember to click save button after edition!!!!
---

Details:
===
Class: 
---
* DigitText
* Text
* HasText (does not require a text annotation)


Output: json file
---

Format example: 
---
```json
{
        "annotations": [
            {
                "class": "Text",
                "height": 41.26544413225945,
                "width": 54.73987486932375,
                "x": 30.317469158394694,
                "y": 21.895949947729502,
                "ztext": "x"
            },
            {
                "class": "HasText",
                "height": 47.160507579725085,
                "width": 64.84569792212199,
                "x": 50.52911526399116,
                "y": 40.42329221119292
            }
        ],
        "class": "image",
        "filename": "../video_shots/youtube_023/10.png"
    },
```
