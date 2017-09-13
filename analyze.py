#!/usr/bin/env python
import functions,sys
from _utils import config

args=sys.argv[1:]
#print(args)

mainCommand=args[0].lower()

if mainCommand == 'process':
	processArgs=args[1:]
	functions.process(processArgs)
elif mainCommand == 'config':
	if len(args) == 1:
		print("Invalid command")
		exit()
	subCommand = args[1].lower()
	config = config.Config()
	if subCommand == 'notifylist':
		if len(args) == 2:
			print(config.get('notifyList'))
		else:
			toAdd = args[2]
			if toAdd in config._config['notifyList']:
				print("Type already exists")
			else:
				if toAdd[:1]=='-':
					toRemove=toAdd[1:]
					if not toRemove in config._config['notifyList']:
						print("Type '{}' not exists!".format(toRemove))
					else:
						print("Removing '{}'".format(toRemove))
						config._config['notifyList'].remove(toRemove)
				else:
					print("Adding '{}'...".format(toAdd))
					config._config['notifyList'].append(toAdd)
					print(config._config['notifyList'])
				config.save()
				print("NotifyList updated.")
	elif subCommand == 'email':
		if len(args) == 2:
			print(config.get('email'))
		elif len(args) == 3:
			if 'email' in config._config:
				print(config._config['email'].get(args[2]))
			else:
				print(None)
		else:
			if not 'email' in config._config:
				config._config['email']={};
			config._config['email'][args[2]]=args[3]
		config.save()
	else:
		print("Not valid command...")