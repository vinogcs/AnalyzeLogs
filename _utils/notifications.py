import smtplib
from _utils import constants

def sendEmail(to,content):
	config = config.Config()
	# Prepare message
	subject="Server needs your attention!"
	message ="""From:{}
To:{}
Subject: {}
Hi
Seems that you have some issues to look at server. Following are the critical errors to follow: 
{}
""".format(
		config._config['email']['username'],
		config._config['email']['to'],
		subject,
		"\r\n".join(content)
	)
	tls=constants.Email._TLS
	server= smtplib.SMTP(config._config['email']['server'],config._config['email']['port'])
	if tls:
		server.starttls()
		server.login(config._config['email']['username'],config._config['email']['password'])
	else:
		server.connect()
	problems = server.sendmail(config._config['email']['username'],to,message)
	server.quit()
	return problems