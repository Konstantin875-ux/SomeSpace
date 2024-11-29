from requests import delete

adress = 'http://' + input() + '/users/' + input()
delete(adress)
