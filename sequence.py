import subprocess

while True:
	for i in range(256):
		subprocess.call(['python', 'setPixel.py', '0', str(i), '0', '0'])
		print i
