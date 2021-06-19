import subprocess

# It will ask you to enter your password, after it's done, you can execute elizabeth.py!
username = 'redacted'

subprocess.run(['instaloader', '--login', username])