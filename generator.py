import re

# ==================================================================================

# Utility methods for the common objects

def getPaths(dictObject):
	return findNodeByName(dictObject, 'paths')
	
def getMethodsForPath(dictObject, path):
	return findNodeByName(findNodeByName(dictObject, 'paths'), path)
	
def getSummary(dictObject):
	return findNodeByName(dictObject, 'summary')

# ==================================================================================

# Given a dictionary, find the value of an object, by the object's name
# This will return the value for the first matching object
def findNodeByName(dictObject, objName):
	
	if type(dictObject) is dict:
	
		for key in dictObject:
		
			if key == objName:
				return dictObject.get(key)
				
			elif type(dictObject.get(key)) is dict:
				# The value of this key is another dictionary, search it
				found = findNodeByName(dictObject.get(key), objName)
				
				# if the object was found searching this branch, return in
				if not found is None:
					return found
	
	# Nothing was found
	return None

# ==================================================================================

# Replace template's placeholder with given values. As long as the keys in the 
# replacements dictionary match {variables} in the template the values will be
# replaced, and the updated template will be returned.
def replaceInTemplate(template, replacements):

	for key in replacements:
		regex = re.compile('{' + f'{key}' + '}')
		template = re.sub(regex, str(replacements.get(key)), template)
		
	return template
	
# ==================================================================================
	