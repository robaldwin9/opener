import sys
import configparser
import webbrowser
import os
import subprocess
import argparse

# Check if String contains and executable extension from list
def isExecutable(item, executableList):
	executable = False
	for executableExtension in executableList:
		if executableExtension in item:
			executable = True
	return executable

# Add each item to list, and return list
def getExecutableList(config):
	executableList = []
	for executable in config["executables"]:
		executableList.append(config["executables"][executable])
	return executableList

def launchItems(config, configGroup):
	foundItem = False
	# Launch user specified group 
	for group in config:
		if group == configGroup:
			foundItem = True
			for item in config[group]:
				if isExecutable(config[group][item], executableList): 
					print("launching: " + item)
					subprocess.Popen(config[group][item].split(" "))
				else:
					webbrowser.open_new(config[group][item])

	# Let user know the passed invalid arg
	if not foundItem:
		print("Item not found")

# User passed group of sites to open
parser = argparse.ArgumentParser(prog="opener", description='Open files, Programs, and webpages in batches')
parser.add_argument('GROUP', help='group name that exists in open.ini\n Each item underneath a group is launched automatically')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()
configGroup = args.GROUP

# Read list of extensions marked as executable on system
config = configparser.ConfigParser()
config.read('executable.ini')
executableList = getExecutableList(config)

# read items to launch to match passed arguments
config.read('open.ini')
launchItems(config, args.GROUP)


