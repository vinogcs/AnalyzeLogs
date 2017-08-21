import os,sys,re
from _utils import Data
import datetime

class baseFile:
	_file_name = ""
	_last_modified = None
	_latest_changes = None
	_data = Data.Data()
	_file_handle = None
	
	# Aaaah... my favourite..
	# THE CONSTRUCTOR
	def __init__(self,filename):
		if not self._data.exists(filename):
			raise Exception('fatal',"Invalid log file provided")
		self._file_name=filename
		self._last_modified = self._data.get(filename)
		self._file_handle=open(self._file_name,'r')
		
	# Read the next line from the bottom.
	# Starting from the last line and it goes up..
	# WEIRD isn't it? 
	# I don't have choice as I need to save resources
	# So that it wont drag time on processing unwanted data for
	# Zillion seconds!
	def readLine(self,buffer=0x20000):
		self._file_handle.seek(0, os.SEEK_END)
		size = self._file_handle.tell()
		lines = ['']
		rem = size % buffer
		pos = max(0, (size // buffer - 1) * buffer)
		while pos >= 0:
			self._file_handle.seek(pos, os.SEEK_SET)
			data = self._file_handle.read(rem + buffer) + lines[0]
			rem = 0
			lines = re.findall('[^\n]*\n?', data)
			ix = len(lines) - 2
			while ix > 0:
				yield lines[ix]
				ix -= 1
			pos -= buffer
		else:
			yield lines[0]
	
	# Closing the File Handle pointer
	def close(self):
		self._file_handle.close()
	
	# Just update the JSON for last updated data
	def modified(self):
		self._data.modified(self._file_name,self._last_log_at)
		self._last_modified=self._data.get(self._file_name)
		
		# Should we save Data? We'll come back to this later
		self._data.save() 