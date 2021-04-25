# Barend Nieuwoudt, 2021

import sys
from logger import Warning, Error, Info
from loader import Yaml, LoadType

paramaters = {}

# ==================================================================================

# Set the run paramaters from the command line arguments
def setParameters(args):

	global paramaters

	# args[0] will always be 'generate.py'
	i = 1
	
	while i < len(args):
		
		# All parameters specified like '-parameter'
		if args[i].startswith('-'):
		
			if args[i] in paramaters:
				Warning.log('Duplicate Paramater specified: ' + str(args[i]))
			
			i += 1
			
			if i in range(len(args)):
				# A value follows the parameter
				paramaters[args[i-1][1:]] = args[i]
			else:
				Warning.log('No value specified for ' + str(args[i-1]))
		else:
			Warning.log('Unexpected value: ' + str(args[i]))

		i += 1

# ==================================================================================

# Load the specification
def loadSpec(type):

	if type == LoadType.YAML:
		return Yaml.load(paramaters[LoadType.YAML])
		
	# This could be improved with other load types

# ==================================================================================

if __name__ == "__main__":
	print('Running Generator')
	
	setParameters(sys.argv)
	
	data = {}
	
	if LoadType.YAML in paramaters:
		# a yaml file was specified
		Info.log(f"Performing {LoadType.YAML} load")
		data = loadSpec(LoadType.YAML)
		
	if data == {}:
		# Nothing was loaded
		Error.log("No Data Loaded.")