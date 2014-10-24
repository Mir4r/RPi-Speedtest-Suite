#The module, that will do the periodic speedtesting with speedtest-cli (github.com/sivel/speedtest-cli)
#2014, K Schweiger

import os
import sys
import speedtestcli.speedtest_cli as stcli
import configreader

# os.system("vlc -q --one-instance "+str(self.entrys[entryid].getSpec("PATH"))+" 2> /dev/null &") 


def writeresult():
    charset = sys.getfilesystemencoding()
    with open('results.dat', 'w+') as data:
        print "Test"
        #First i must figure out, was will be saved.


def downtest(interval, serverlist):
    stcli.downloadSpeed()
    
def findserver(serverlist):
    #get speedtest server
    cliconf = stcli.getConfig()
    servers = stcli.closestServers(cliconf['client'],True)
    #find the in the config given ones
    slist = []
    prefname = ""
    sflag = False #used, when more than one server existst for a given location
    for server in servers:
        name = ('%(name)s' % server)
        if prefname == name:
            sflag = True
        else:
            sflag = False
        for element in serverlist:
            if element == name:
                if sflag == False:
                    sid = ('%(id)4s' % server)
                    sinfo = [sid, name]
                    slist.append(sinfo)
                else:
                    print "The location -"+name+"- provides more then one server. Only the nearest will be used."
        prefname = name
    return slist        

def main():
    #Code for testing:
    #conifg: 0: Dl flag, 1: Ul flag, 2: Interval, 3:: Servers
    config = configreader.main()
    #print config
    serverlist = findserver(config[3::]) #each element of serverlist contains a the id and the name of a server
    #print serverlist
    if config[0] == 1:
        print downtest(config[2],config[3::])

if __name__ == '__main__':
    main()
