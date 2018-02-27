import subprocess
from subprocess import Popen, PIPE
import numpy as np
import pylab as pl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.ticker as ticker
import json
from pprint import pprint

xdegreelist=[]
for i in range (0,18):
    degree=i*15
    xdegreelist.append(degree)

ydegreelist=[]
for i in range (0,26):
    degree=i*4
    ydegreelist.append(degree)

if __name__ == '__main__':
    i = 250
    plistrand = []
    plistivolt = []
    plisttvol = []
    plistvol = []
    plistevolf = []
    plistvoli = []
    plistdeg = []
    swlist = []
    with open('1024/Sasan.2104.1504345427.08.final.json') as data_file:
    	data = json.load(data_file)
    for j in range(0, i):
    	plistrand.append(data[j]["max_stretch2"])

    with open('1024/Sasan.6848.1504315245.17.final.json') as data_file:
    	data = json.load(data_file)
    for j in range(0, i):
    	plistivolt.append(data[j]["max_stretch2"])

    with open('1024/Sasan.7236.1504286910.57.final.json') as data_file:
    	data = json.load(data_file)
    for j in range(0, i):
    	plisttvol.append(data[j]["max_stretch2"])

    with open('1024/Sasan.7580.1504271248.78.final.json') as data_file:
    	data = json.load(data_file)
    for j in range(0, i):
    	plistvol.append(data[j]["max_stretch2"])

    with open('1024/Sasan.8560.1504306886.75.final.json') as data_file:
    	data = json.load(data_file)
    for j in range(0, i):
    	plistevolf.append(data[j]["max_stretch2"])

    with open('1024/Sasan.12248.1504329965.75.final.json') as data_file:
    	data = json.load(data_file)
    for j in range(0, i):
    	plistvoli.append(data[j]["max_stretch2"])

	with open('1024/Sasan.15356.1504261418.28.final.json') as data_file:
		data = json.load(data_file)
    for j in range(0, i):
    	plistdeg.append(data[j]["max_stretch2"])

    for m in range(1, i+1):
        swlist.append(m)

    fig = pl.figure()
    pl.plot(swlist, plistrand, '-r', label='RAND')
    pl.plot(swlist, plistivolt, '-g', label='IVOLT')
    pl.plot(swlist, plisttvol, '-b', label='TVOL')
    pl.plot(swlist, plistvol, '-c', label='VOL')
    pl.plot(swlist, plistevolf, '-m', label='EVOLF')
    pl.plot(swlist, plistvoli, '-y', label='VOLI')
    pl.plot(swlist, plistdeg, '-k', label='DEG')
    pl.xlim(0, 260)
    pl.xticks(xdegreelist)
    pl.yticks(ydegreelist)
    pl.ylim(0, 101)
    pl.ylabel('Max Stretch')
    pl.xlabel('Number of Switches')
    pl.title("Max Stretch for Various Strategies")
    pl.legend(loc='upper right')
    fig.savefig('plot.png')
    fig.savefig('plot.pdf')