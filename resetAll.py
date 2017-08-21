#!/usr/bin/env python
from _utils import constants,Data,LogFile

_data=Data.Data()
for file in _data._data:
	print("Reseting {}".format(file))
	_data._data[file]=""
_data.save(True) # Saving Forcefully.