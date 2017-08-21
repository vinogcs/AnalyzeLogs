from _utils import File
from datetime import datetime
from dateutil.parser import parse
import pandas as pd

class LogFile(File.baseFile):
	_last_log_at = None
	
	def __init__(self,filename):
		File.baseFile.__init__(self,filename)
		self._file_name=filename
	
	def getLatestChanges(self):
		_latest_changes=[]
		for line in self.readLine():
			if line.strip()=='' :
				continue
				
			_position_datetime = line.find("] ")
			try:
				_log_datetime=pd.to_datetime(line[1:_position_datetime].strip())
			except:
				continue
				
			if not (self._last_modified.strip()=='' or _log_datetime > pd.to_datetime(self._last_modified)):
				break;
			
			_latest_changes.append(line)
			if self._last_log_at == None or self._last_log_at < _log_datetime :
				self._last_log_at = _log_datetime
			
		return _latest_changes