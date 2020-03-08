import sys
import configparser
import webbrowser
import os
import subprocess

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

# User passed group of sites to open
configGroup = sys.argv[1]

# Read list of extensions marked as executable on system
config = configparser.ConfigParser()
config.read('executable.ini')
executableList = getExecutableList(config)

# read items to launch to match passed arguments
config.read('open.ini')
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

