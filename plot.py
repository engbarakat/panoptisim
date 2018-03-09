
import subprocess
from subprocess import Popen, PIPE
import numpy as np
import pylab as pl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.ticker as ticker


pl.rc('xtick', labelsize=30)    # fontsize of the tick labels
pl.rc('ytick', labelsize=30)
pl.rc('figure',titlesize = 30)


with open('JournalGavel%sslice.txt' %topologyname) as inf:
        for line in inf:


    fig = pl.figure()
    #pl.plot(swlist, plistvol, '-g', label = 'Vlan VOL')
    pl.plot(swlist, plisttvol, '-b', label = 'Vlan tVOL')
    #pl.plot(swlist, plistevolf, '-c', label = 'Vlan tVOLe')
    #pl.plot(swlist, plistivolt, '-m', label = 'Vlan tVOLi')
    #pl.plot(swlist, plistvoli, '-y', label = 'Vlan VOLi')
    pl.xlim(0, 260)
    #pl.xticks(xdegreelist, fontsize=8)
    pl.yticks(ydegreelist)
    pl.ylim(0, 101)
    pl.ylabel('SDN Port Coverage')
    pl.xlabel('Number of Switches')
    pl.title("Various Strategies on VLAN 1024")
    pl.legend(loc='lower right')
    pl.show()