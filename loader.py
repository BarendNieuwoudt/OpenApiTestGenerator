# Barend Nieuwoudt, 2021

import yaml # pip install pyyaml
import json
from logger import Error, Warning, Info

class Yaml:

	YAML = 'yaml'

	# Load a .yml/.yaml file into a dictionary
	def load(path):
		try:
			with open(str(path)) as file:
				return yaml.load(file, Loader=yaml.FullLoader)
		except:
			Error.log(f"Could not load file {path}")
		
class Json:

	JSON = 'json'

	# Load a .json file into a dictionary
	def load(path):
		try:
			with open(str(path)) as file:
				return json.load(file)
		except:
			Error.log(f"Could not load file {path}")
			
class Template:

	TEMPLATE = 'template'
	DEFAULT = 'template.txt'

	# Load a .txt template file
	def load(path):
		try:
			with open(str(path)) as file:
				return file.read()
		except:
			Error.log(f"Could not load file {path}")