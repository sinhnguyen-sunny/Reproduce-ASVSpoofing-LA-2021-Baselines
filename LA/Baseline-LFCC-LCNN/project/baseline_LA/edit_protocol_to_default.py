#import library
import os
import numpy as np

#initiate file path
dest_protocol_filepath = "/home/sinhnta/ASV/asv-2021-repo/asv/baselines/2021/eval-package/LA/package-stage-1/keys/CM/trial_metadata.txt"
output_file_path = "/home/sinhnta/ASV/Dataset/ASVspoof2021_LA_eval/LFCC_LCNN_ASVspoof2021.LA.cm.eval.trl.txt"

#read the original protocol file
temp_buffer = np.loadtxt(dest_protocol_filepath, dtype='str', usecols = (0,1,2,3,5))

#write to another file
np.savetxt(output_file_path, temp_buffer, fmt='%s')
