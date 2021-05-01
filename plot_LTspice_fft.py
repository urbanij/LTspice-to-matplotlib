#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:17:20 2018

@author: francescourbani
"""

import sys
import math
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = sys.argv[1]
# FILE_NAME = "../Draft2.fft.txt"

with open(FILE_NAME, "r") as f:
	first_row = f.readline()

TITLE = first_row.split('\t')[1][:-1]

_f  = []
_re = []
_im = []

with open(FILE_NAME, "r") as f:
	next(f) # skip header
	for line in f:
		_f.append(float(line.split('\t')[0]))
		_re.append(float(line.split('\t')[1].split(',')[0]))
		_im.append(float(line.split('\t')[1].split(',')[1][:-1]))	

_f = np.array(_f)
fft_ = np.array(_re) + 1j * np.array(_im)


# plotting
plt.figure()

plt.subplot(211)
plt.title(TITLE)


# plt.yscale('log')

plt.xscale('log')
plt.grid(True)

# plt.ylabel("|"+TITLE+"| " + "$(dB)$")
plt.ylabel("$(dB)$")

plt.plot(_f,np.abs(fft_), label="|"+TITLE+"|")
plt.legend()


plt.subplot(212)
plt.xscale('log')
plt.grid(True)
plt.xlabel("f $(Hz)$")

# plt.ylabel("$\measuredangle$" + TITLE + " $(deg)$")
plt.ylabel("$(deg)$")

plt.plot(_f,np.degrees(np.angle(fft_)), label="$\measuredangle "+TITLE+"$")
plt.legend()
plt.savefig(f"{FILE_NAME.split('/')[-1]}.svg", format='svg')
plt.show()
