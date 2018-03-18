
import subprocess
from subprocess import Popen, PIPE
import numpy as np
import pylab as pl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.ticker as ticker


pl.rc('xtick', labelsize=50)    # fontsize of the tick labels
pl.rc('ytick', labelsize=50)
pl.rc('figure',titlesize = 50)

plistvol = []
plisttvol = []
plistevolf = []
plistivolt = []
plistvoli = []
fig = pl.figure()
ydegreelist=[]
for i in range (0,11):
    degree=i*10
    ydegreelist.append(degree)
swlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250]
plist = []
try:
    with open('vol1024.txt') as inf:
        for line in inf:
            parts = line.split("\t") # split line into parts
            for y in parts:
                
                plistvol.append(float(y))
except ValueError,e:
        print "error",e,"on line",y
with open('voli1024.txt') as inf:
  for line in inf:
    parts = line.split("\t") # split line into parts
    for y in parts:
        plistvoli.append(float(y))
with open('tvol1024.txt') as inf:
  for line in inf:
    parts = line.split("\t") # split line into parts
    for y in parts:
        plisttvol.append(float(y))
        
with open('ivolt1024.txt') as inf:
  for line in inf:
    parts = line.split("\t") # split line into parts
    for y in parts:
        plistivolt.append(float(y))
        
with open('evolf1024.txt') as inf:
  for line in inf:
    parts = line.split("\t") # split line into parts
    for y in parts:
        plistevolf.append(float(y))
        


    
pl.plot(swlist, plistvol, '-g', label = 'Vlan VOL',linewidth=3.0)
pl.plot(swlist, plisttvol, '-k', label = 'Vlan tVOL',linewidth=3.0)
pl.plot(swlist, plistevolf, '-b', label = 'Vlan tVOLe',linewidth=3.0)
pl.plot(swlist, plistivolt, '-m', label = 'Vlan tVOLi',linewidth=3.0)
pl.plot(swlist, plistvoli, '-r', label = 'Vlan VOLi',linewidth=3.0)
pl.xlim(0, 260)
#pl.xticks(xdegreelist, fontsize=8)
pl.yticks(ydegreelist)
pl.ylim(0, 101)
pl.ylabel('SDN Port Coverage(%)',size=50)
pl.xlabel('Number of Switches',size=50)
pl.title("Various Strategies on VLAN 1024",size=50)
pl.legend(loc='lower right',prop={'size': 30})
pl.show()