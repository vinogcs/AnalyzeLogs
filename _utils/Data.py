import os.path
import simplejson
import json
from time import gmtime, strftime

class Data:
	_file = "data.json"
	_list = "_utils/logs"
	_data = {};
	_is_updated = False
	
	# Just a comment to show that this is the COMMENT!! 
	# hehe... leave it.. this is just a constructor
	def __init__(self):
		# Read existing data from JSON
		self.readData()
		
		# Read the list file to get any new paths added
		if self.validateWithNewList():
			# Write complete data to JSON if any new item had been added to list
			self.writeData()
		
	# Just get me JSON encoded string
	def encode(self):
		return simplejson.dumps(self._data,indent=4,skipkeys=True,sort_keys=True)

	# Read the lists file.
	# List of Log files to analyze
	def readList(self):
		lists=[];
		with open(Data._list) as fileList:
			lists=fileList.readlines()
		lists=[x.strip() for x in lists]
		return lists
	
	# Validate all entries from json file and list file
	# Add new entries to json file and
	# Delete removed entries from json file
	def validateWithNewList(self):
		lists=self.readList()
		isUpdated = False
		dataKeys=Data._data.keys()
		for item in lists:
			if not item in Data._data:
				isUpdated=True
				Data._data[item]=''

		pathsToDelete=[];
		for itemIndex in dataKeys:
			if not itemIndex in lists:
				pathsToDelete.append(itemIndex);		
		if len(pathsToDelete)>0:
			isUpdated = True
		for pathToDelete in pathsToDelete:
			print("Deleting {}".format(pathToDelete))
			Data._data.pop(pathToDelete)
		return isUpdated;
	
	# Reading Data from json file
	def readData(self):
		if os.path.isfile(Data._file):
			fd=open(Data._file,'r')
			content=fd.read()
			fd.close()
			Data._data=simplejson.loads(content)
	
	# Write all data in memory to file.
	def writeData(self):
		fd=open(Data._file,'w')
		fd.write(self.encode())
		fd.close()
	
	# Update the Last Analyzed date so that we can save some time while read log files
	def modified(self, itemIndex,datetime):
		Data._data[itemIndex]=datetime.strftime("%Y-%m-%d %H:%M:%S.%f")
		self._is_updated = True
	
	# Just an alias for Write Data so that I can remember the name
	def save(self,force=False):
		if self._is_updated or force:
			self.writeData()
	
	# Check whether Log file is exists in list
	def exists(self,filename):
		if filename in self._data:
			return True
		else:
			return False
	
	def get(self,filename):
		return self._data.get(filename)