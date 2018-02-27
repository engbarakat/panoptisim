import subprocess
from subprocess import Popen, PIPE
import numpy as np
import pylab as pl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.ticker as ticker


def runcmd(strnumber, vlannumber):
    output = subprocess.Popen('python panoptisim.py --pickle new --seedmapping 1 --seednextswitch 1 '
                    '--tmsf max-50 --epsf 1 --epp 10 --tm 2004 --switchstrategy VOLI '
                    '--portstrategy default --maxvlans ' + str(vlannumber) +
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
    plist256 = []
    plist512 = []
    plist1024 = []
    swlist=[]
    i=3
    vlans=[256,512,1024]
    for j in range (len(vlans)):
        j =int (vlans[j])
        print(j)
        for k in range (1,i+1):
            output = runcmd(i, j)
            # print output[1]
            output = output[1]
            string1 = "Iteration ["+str(k)+"] done."
            index = output.find(string1)
            tempStr = output[index+20:]
            string2 = "SDN Ports"
            ports = tempStr[:tempStr.find(string2)].strip()
            # print ports
        # test = "[276/2591]"
            test= ports
            test = test.replace("[", "")
            test = test.replace("]", "")
            data = test.split("/")
            #print data[0]
            #print data[1]
            for temp in data:
            #print temp
                Division =float (data[0]) / float (data[1])
                percentage= Division  * 100
            #print percentage

            if  j==256:
                plist256.append(percentage)
            elif j==512:
                plist512.append(percentage)
            elif j==1024:
                 plist1024.append(percentage)

        print plist256
        print plist512
        print plist1024
    for m in range(1, i+1):
        swlist.append(m)
    print swlist

    # zipped = zip(plist256,plist512,plist1024)
    # print zipped
    fig = pl.figure()
    pl.plot(swlist,plist256,'-r',label='Vlan 256')
    pl.plot(swlist, plist512,'-g',label='Vlan 512')
    pl.plot(swlist, plist1024, '-b',label='Vlan 1024')
    pl.xlim(0, 260)
    pl.xticks(xdegreelist)
    pl.yticks(ydegreelist)
    pl.ylim(0, 101.)
    pl.ylabel('SDN port Coverage')
    pl.xlabel('Number of switches')
    pl.title("VOL strategy")
    pl.legend(loc='upper left')
    # pl.show()
    fig.savefig('plot.png')
    fig.savefig('plot.pdf')