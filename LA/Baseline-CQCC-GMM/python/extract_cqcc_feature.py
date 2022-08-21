from CQCC.cqcc import cqcc
import scipy.io.wavfile as wav
import soundfile as sf
import os
import numpy as np

def extract_cqcc_feature(x, fs):
	# INPUT SIGNAL
	x = x.reshape(x.shape[0], 1)  # for one-channel signal 
	# print(x.shape)
	# fs: 16000
	# x: (64244,)
	# PARAMETERS
	B = 96
	fmax = fs/2
	fmin = fmax/2**9
	d = 16
	cf = 19
	ZsdD = 'ZsdD'
	# COMPUTE CQCC FEATURES
	CQcc, LogP_absCQT, TimeVec, FreqVec, Ures_LogP_absCQT, Ures_FreqVec, absCQT = cqcc(x, fs, B, fmax, fmin, d, cf, ZsdD)
	return CQcc, fmax, fmin