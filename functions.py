from _utils import constants,Data,LogFile,notifications
import sys,os,re

def process():
	alert_types=['error','fatal','critical','notice']

	data = Data.Data()
	all_logs = data.readList()
	log_to_notify=[]
	for log in all_logs:
		try:
			lgFile = LogFile.LogFile(log)

			latestChanges=lgFile.getLatestChanges()
			for changedLine in latestChanges:
				for alert_type in alert_types:
					if not changedLine.lower().find(alert_type) == -1:
						log_to_notify.append(changedLine)
					# END IF
				# END FOR
			# END FOR
			if len(latestChanges)>0:
				lgFile.modified()
			# END IF
			lgFile.close();
		except IOError:
			print('Can not open file \'{}\''.format(log))
	# END FOR

	if len(log_to_notify) > 0:
		notifications.sendEmail("vino.gcs@gmail.com",log_to_notify)
	print("DONE")
