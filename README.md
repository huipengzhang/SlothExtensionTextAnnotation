# SlothExtensionTextAnnotation
**Special configuration file for annotation tool SLOTH: https://github.com/cvhciKIT/sloth**

**TextRectItem:** Extented RectItem. Add text annotation for text detection data preparation

**Author:** Yiye Lin 

**version:** 1.0

TOOL：SLOTH 
===
https://cvhci.anthropomatik.kit.edu/~baeuml/projects/a-universal-labeling-tool-for-computer-vision-sloth/

**Document:** http://sloth.readthedocs.org/en/latest/index.html

**Prerequisite:** python 2.7, Numpy

**Packages:** python-qt4, python-numpy
    
**Environment:** Linux

---
Usage: 
===
To add image
---
    sloth appendfiles “output_file_name_here”.json “image_file_path_here”/*.png
    
E.g.

    sloth appendfiles b.json ../video_shots/youtube_001/*.png
    
To add & edit annotation file
---
	Sloth -c “config_file_name_here”.py  “output_file_name_here”.json
E.g. 

    sloth -c textAnnoConfig.py b.json

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
