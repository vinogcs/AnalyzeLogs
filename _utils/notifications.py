import smtplib
from _utils import constants

def sendEmail(to,content):
	# Prepare message
	subject="Server needs your attention!"
	message ="""From:{}
To:{}
Subject: {}
Hi
Seems that you have some issues to look at server. Following are the critical errors to follow: 
{}
""".format(
		constants.Email._USERNAME,
		to,
		subject,
		"\r\n".join(content)
	)
	tls=constants.Email._TLS
	server= smtplib.SMTP(constants.Email._SERVER,constants.Email._PORT)
	if tls:
		server.starttls()
		server.login(constants.Email._USERNAME,constants.Email._PASSWORD)
	else:
		server.connect()
	problems = server.sendmail(constants.Email._USERNAME,to,message)
	server.quit()
	return problems