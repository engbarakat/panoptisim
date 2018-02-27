import subprocess
from subprocess import Popen, PIPE
import numpy as np
import pylab as pl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.ticker as ticker


def runcmd(strnumber, strategy):
    output = subprocess.Popen('python panoptisim.py --pickle new --seedmapping 1 --seednextswitch 1'
                    ' --tmsf max-50 --epsf 1 --epp 10 --tm 2004 --switchstrategy ' + str(strategy) +
                    ' --portstrategy default --maxvlans 256'
                    ' --maxft 100000 --toupgrade ' + str(strnumber), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )

    return (output.communicate())

xdegreelist=[]
for i in range (0,18):
    degree=i*15
    xdegreelist.append(degree)

ydegreelist=[]
for i in range (0,26):
    degree=i*4
    ydegreelist.append(degree)

if __name__ == '__main__':
    plistdeg = []
    plistvol = []
    plisttvol = []
    plistevolf = []
    plistivolt = []
    plistvoli = []
    plistrand = []
    swlist = []
    stra = ["DEG", "VOL", "TVOL", "EVOLF", "IVOLT", "VOLI", "RAND"]
    vlans = [256, 512, 1024]
    i = 250
    for j in range (len(stra)):
        j =str (stra[j])
        print(j)
        output = runcmd(i, j)
        output = output[1]
        for k in range (1, i+1):
            string1 = "Iteration [" +str(k)+ "] done."
            index = output.find(string1)
            tempStr = output[index + 20:]
            string2 = "SDN Ports"
            ports = tempStr[:tempStr.find(string2)].strip()
            # print ports
            # test = "[276/2591]"
            test = ports
            if ". " in test:
                test = test.replace(". ", "")
            test = test.replace("[", "")
            test = test.replace("]", "")
            data = test.split("/")
            #print data[0]
            #print data[1]
            for temp in data:
            #print temp
                Division = float (data[0]) / float (data[1])
                percentage = Division  * 100
            #print percentage

            if j == "DEG":
                plistdeg.append(percentage)
            elif j == "VOL":
                plistvol.append(percentage)
            elif j == "TVOL":
                plisttvol.append(percentage)
            elif j == "EVOLF":
                plistevolf.append(percentage)
            elif j == "IVOLT":
                plistivolt.append(percentage)
            elif j == "VOLI":
                plistvoli.append(percentage)
            elif j == "RAND":
                plistrand.append(percentage)

    for m in range(1, i+1):
        swlist.append(m)
    print swlist

    # zipped = zip(plist256,plist512,plist1024)
    # print zipped
    fig = pl.figure()
    pl.plot(swlist, plistdeg, '-r', label = 'Vlan DEG')
    pl.plot(swlist, plistvol, '-g', label = 'Vlan VOL')
    pl.plot(swlist, plisttvol, '-b', label = 'Vlan TVOL')
    pl.plot(swlist, plistevolf, '-c', label = 'Vlan EVOLF')
    pl.plot(swlist, plistivolt, '-m', label = 'Vlan IVOLT')
    pl.plot(swlist, plistvoli, '-y', label = 'Vlan VOLI')
    pl.plot(swlist, plistrand, '-k', label = 'Vlan RAND')
    pl.xlim(0, 260)
    pl.xticks(xdegreelist)
    pl.yticks(ydegreelist)
    pl.ylim(0, 101)
    pl.ylabel('SDN Port Coverage')
    pl.xlabel('Number of Switches')
    pl.title("Various Strategies on VLAN 256")
    pl.legend(loc='lower right')
    # pl.show()
    fig.savefig('plot.png')
    fig.savefig('plot.pdf')