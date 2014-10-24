import os
import sys

#def readConfig():
def main():
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
    #print lines
    config = []
    for line in lines:
        #ignore Lines beginning with # or nothing in it
        if len(line) > 0 and line[0] != "#":
            if line[0:8] == "servers=":
                serverlist = line[8::].split(",")
            if line[0:9] == "interval=":
                config.append(int(line[9::]))
            if line[0:3] == "dl=":
                config.append(int(line[3::]))
            if line[0:3] == "ul=":
                config.append(int(line[3::]))
    config = config + serverlist
    return config

#def main():
#    print "Not that use!"

if __name__ == '__main__':
    main()
