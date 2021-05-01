# Barend Nieuwoudt, 2021

import sys, re
import generator as gen
from logger import Warning, Error, Info
from loader import Yaml, Template

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

# Load the template file, from the provided or default path	
def loadTemplate():
	if Template.TEMPLATE in paramaters:
		return str(Template.load(paramaters[Template.TEMPLATE]))
	else:
		return str(Template.load(Template.DEFAULT))

# ==================================================================================
		
# Sanitize the string, remove special characters
def sanitizeString(value):
	return re.sub(r'/', '_', value)

# ==================================================================================

if __name__ == "__main__":
	
	setParameters(sys.argv)
	
	template = loadTemplate()
	
	data = {}
	
	if Yaml.YAML in paramaters:
		# a yaml file was specified
		Info.log(f"Performing {Yaml.YAML} load")
		data = loadSpec(Yaml.YAML)
	
		# TODO: Test Code
		paths = gen.getPaths(data)
		
		# Replace the summary for each path in the template, and print the testcase
		for path in paths:
			methods = gen.getMethodsForPath(data, path)
			for method in methods:
				tempDict = {}
				tempDict['method'] = method
				tempDict['path'] = sanitizeString(path)
				tempDict['summary'] = str(gen.getSummary(methods.get(method)))
				tempDict['description'] = str(gen.findNodeByName(methods.get(method), 'description'))
				print(str(gen.replaceInTemplate(template, tempDict)))
		
	if data == {}:
		# Nothing was loaded
		Error.log("No Data Loaded.")