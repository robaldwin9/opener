import sys
import configparser
import webbrowser

# User passed group of sites or files to open
configGroup = sys.argv[1]

config = configparser.ConfigParser()
config.read('open.ini')
foundItem = False

for group in config:
	if group == configGroup:
		foundItem = True
		for item in config[group]:
			webbrowser.open_new(config[str(group)][str(item)])

if not foundItem:
	print("Item not found")
	

