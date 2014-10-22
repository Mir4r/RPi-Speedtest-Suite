#The module, that will do the periodic speedtesting with speedtest-cli (github.com/sivel/speedtest-cli)
#2014, K Schweiger

import os
import sys

# os.system("vlc -q --one-instance "+str(self.entrys[entryid].getSpec("PATH"))+" 2> /dev/null &") 



#Read Config:
def readConfig():
    #open file
    charset = sys.getfilesystemencoding()
    lines = []
    #read config and test if it exists
    try:
        open('speedtest.cfg', 'r')
    except IOError:
        print "No Config"
        return False
    with open(os.path.join('speedtest.cfg'), 'r') as cfg:
        inputfile = cfg.read()
    #after this you have one sting with all lines seperatet by \n
    #so split it! -> lines is a list with the lines from the read file
    lines = inputfile.split("\n")
    config = []
    for line in lines:
        #ignore Lines beginning with # or nothing in it
        if len(line) > 0 and line[0] != "#":
            if line[0:8] == "servers=":
                serverlist = line[8::].split(",")
            if line[0:9] == "interval=":
                interval = line[9::]
    #write the intervel and the servers in a list that is returned
    config.append(interval)
    config = config + serverlist
    return config

def writeresult():
    charset = sys.getfilesystemencoding()
#    with open(os.path.j


def main():
    config = readConfig()
    print config

if __name__ == '__main__':
    main()
