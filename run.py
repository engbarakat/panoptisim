import subprocess
from subprocess import Popen, PIPE
import numpy as np
import pylab as pl


def runcmd(strnumber, vlannumber):
    output = subprocess.Popen('python panoptisim.py --pickle new --seedmapping 1 --seednextswitch 1 '
                    '--tmsf max-50 --epsf 1 --epp 10 --tm 2004 --switchstrategy VOLI '
                    '--portstrategy default --maxvlans ' + str(vlannumber) +
                    ' --maxft 100000 --toupgrade ' + str(strnumber), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )

    return (output.communicate())


if __name__ == '__main__':
    plist256 = []
    plist512 = []
    plist1024 = []
    swlist=[1,2]
    vlans=[256,512,1024]
    for j in range (len(vlans)):
        j =int (vlans[j])
        print(j)
        for i in range(1,3):
            output = runcmd(i,j)
            # print output[1]
            output = output[1]
            string1 = "Iteration ["+str(i)+"] done."
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

    zipped = zip(plist256,plist512,plist1024)
    print zipped

    pl.plot(swlist,plist256,'r')
    pl.plot(swlist, plist512,'g')
    pl.plot(swlist, plist1024, 'b')
    pl.xlim(0.0, 10)
    pl.ylim(0.0, 30.)
    pl.show()
