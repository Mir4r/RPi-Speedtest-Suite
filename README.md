RPi-Speedtest-Suite
===================

Some modules for automated speedtesting your internet connection with a Raspberry Pi. In general none of the modules will be restricted to the RPi.

For the speedtest speedtest-cli (https://github.com/sivel/speedtest-cli) is used.

The analysis of the taken data will be realized with ROOT (http://root.cern.ch/drupal/).

The testing module will test the speed of the internet connection peridocally and write the results in a file. In the config the tested servers an the time intervall can be chosen.

Installation:

 * After cloning this repo clone the speedtest-cli repo in this repos folder.
 * Create the empty file __init__.py inside the speedtest-cli directory and rename the directory to speedtestcli
   (Python does not like the '-', when importing the the skript als a module)
 * Change the config file to fit your needs
 
