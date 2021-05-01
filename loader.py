# Barend Nieuwoudt, 2021

import yaml # pip install pyyaml
import json
from logger import Error
from logger import Warning

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