import subprocess
import time

stupidEx = '[REDACTED]'		# Username of my ex-girlfriend, REDACTED
username = '[REDACTED]'	    # My Instagram username

while True:
	subprocess.run(['instaloader', stupidEx, '--login', username, '--stories'])
	time.sleep(18000)