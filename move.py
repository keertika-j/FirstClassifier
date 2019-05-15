import os
import sys
import shutil
from imutils import paths
import argparse
ap=argparse.ArgumentParser()
ap.add_argument("-i","--F",required=True,help="path to  directory ")
args = vars(ap.parse_args())
i=1
for g in os.listdir(args["F"]):
	print(i)
	src=os.path.join(args["F"],g)
	print(src)
	if(i<=284):
		print(".")
		shutil.move(src,"Train/FaceImages")
	i+=1
		