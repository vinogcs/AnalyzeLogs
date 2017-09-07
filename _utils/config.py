import os.path
import sys
import simplejson

class Config:
	_file_name = "config.json"
	_config = {}
	_file_handle = None
	
	def __init__(self):
		filename=os.path.join(os.path.dirname(__file__),self._file_name)
		if os.path.isfile(filename):
			with open(filename,'r') as _file_handle:
				content = _file_handle.read()
				if not content == '':
					self._config = simplejson.loads(content)
		else:
			print('Error in opening CONFIG file..')
				
	def get(self,key):
		if key in self._config:
			return self.encodeEach(self._config[key])
		return None
	
	def set(self,key,value):
		self._config[key]=value
	
	def encodeEach(self,expr):
		return simplejson.dumps(expr,indent=4,skipkeys=True,sort_keys=True)
		
	def encode(self):
		return simplejson.dumps(self._config,indent=4,skipkeys=True,sort_keys=True)
	
	def save(self):
		filename=os.path.join(os.path.dirname(__file__),self._file_name)
		with open(filename,'w') as _file_handler:
			_file_handler.write(self.encode())
			