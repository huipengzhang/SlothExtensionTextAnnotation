#!lfs1/yiyelin/anaconda2/bin
#-*- coding:utf-8 -*-
import math
import json
import sys
from pprint import pprint
from cv2 import cv as cv

#print sys.argv[1]
if sys.argv[1] == "help":
	print"1: jsonfile's name; 2: output jsonfile's path; 3:output images' path\n"
	quit()
json_name = sys.argv[1]
div_json_path = sys.argv[2]
pics_path = sys.argv[3]

json_file = open(json_name, 'r')
all_text = json_file.read().encode('utf-8')
js = json.loads(all_text)
lst = open(json_name.split(".")[0] + ".list", "w")
for anno in js:
	#print len(anno)
	path = anno["filename"]
	folder = path.split("/")[-2]
	name = path.split("/")[-1].split(".")[0]
	#printlist (image, annotations)
	lst.write(path + " " + div_json_path + "/" + folder + "_" + name + ".json\n")
	#dividepics
	#print json for every image
	out = open(div_json_path + "/" + folder + "_" + name + ".json", 'w')
	img = cv.LoadImage(path)
	count = 0
	for group in anno["annotations"]:
		count = count + 1
		_x = int(math.floor(group["x"]))
		_y = int(math.floor(group["y"]))
		_width = int(math.ceil(group["width"]))
		_height = int(math.ceil(group["height"]))
		_class = group["class"].encode()
		cv.SetImageROI(img,(_x, _y, _width, _height))
#		print pics_path + "/" + folder + "_" + name + "_" + str(count) + "_" + _class + ".png"
		group.clear()
		group["x"] = _x
		group["y"] = _y
		group["width"] = _width
		group["height"] = _height
		group["class"] = _class
		string = pics_path + "/" + folder + "_" + name + "_" + str(count) + "_" + _class + ".png"
		group["imgname"] = string.encode()
		cv.SaveImage(string, img)
	out.write(json.dumps(anno))
	#print anno
		



	

