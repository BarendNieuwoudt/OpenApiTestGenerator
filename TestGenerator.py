# Barend Nieuwoudt, 2021

import sys
import generator as gen
from logger import Warning, Error, Info
from loader import Yaml

paramaters = {}

# ==================================================================================

# Set the run paramaters from the command line arguments
def setParameters(args):

	global paramaters

	# args[0] will always be 'TestGenerator.py'
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

	if type == Yaml.YAML:
		return Yaml.load(paramaters[Yaml.YAML])
		
	if type == Json.JSON:
		return Json.load(paramaters[Json.JSON])

# ==================================================================================

if __name__ == "__main__":
	
	setParameters(sys.argv)
	
	data = {}
	
	if Yaml.YAML in paramaters:
		# a yaml file was specified
		Info.log(f"Performing {Yaml.YAML} load")
		data = loadSpec(Yaml.YAML)
	
		# Test Code: Find a dictionary, and then find a value in that dictionary
		paths = gen.getPaths(data)
		
		for path in paths:
			print(str(gen.getSummary(paths.get(path))))
		
	if data == {}:
		# Nothing was loaded
		Error.log("No Data Loaded.")