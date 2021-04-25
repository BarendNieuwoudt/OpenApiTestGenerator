# Barend Nieuwoudt, 2021

import yaml # pip install pyyaml
from logger import Error

class LoadType:
	
	YAML = 'yaml'
	XML = 'xml'
	JSON = 'json'

class Yaml:

	def load(path):
		try:
			with open(str(path)) as file:
				return yaml.load(file, Loader=yaml.FullLoader)
		except:
			Error.log(f"Could not load file {path}")
			
# Future improvements could be made to also read JSON, XML, and other standardized formats