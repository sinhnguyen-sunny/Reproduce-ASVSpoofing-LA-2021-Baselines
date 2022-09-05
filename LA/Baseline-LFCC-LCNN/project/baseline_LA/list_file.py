#import library
import os

a = open("/home/sinhnta/ASV/Dataset/LA/LA/ASVspoof2019_LA_train/list_file.lst", "w")
for path, subdirs, files in os.walk('/home/sinhnta/ASV/Dataset/LA/LA/ASVspoof2019_LA_train/flac'):
	for filename in files:
	 f = filename.split(".")[0]
	 a.write(str(f) + os.linesep) 

#or use command line
#cd to the folder want to list
# use commnad
# 'printf '%s\n' * > ../list_file.lst'