import requests
import json


url = 'https://petstore.swagger.io/v2'

# Создание пользователя VarNa
data_post = json.dumps({"id": 0, "username": "VarNa", "firstName": "Na", "lastName": "Var", "email": "mail@mail.eu", "password": "1q2w3", "phone": "123", "userStatus": 0})
res = requests.post('https://petstore.swagger.io/v2/user', headers={'Content-type': 'application/json', 'accept': 'application/json'}, data=data_post)
print("POST new user VarNa\n", res.status_code, res.json())

# Пользователь VarNa
res = requests.get(f'{url}/user/VarNa', headers={'accept': 'application/json'})
print("GET new user VarNa\n", res.status_code, res.json())
print("res_id = ", res.json)

# Аутотентификация
res = requests.get(f'{url}/user/login', params={'username' : 'VarNa', 'password' : '1q2w3'}, headers={'accept': 'application/json'})
print("GET for logs user VarNan", res.status_code, res.json())

# Изменение данных пользователя VarNa
data_put = json.dumps({"id": 0, "username": "VarNa1", "firstName": "Na1", "lastName": "Var", "email": "test@mail.ru", "password": "1q2w3", "phone": "(900)0000001", "userStatus": 0})
res = requests.put('https://petstore.swagger.io/v2/user/VarNa', headers={'Content-type': 'application/json', 'accept': 'application/json'},data=data_put)
print("PUT user VarNa to VarNa1\n", res.status_code, res.json())

# Пользователь VarNa1 - проверим изменения
res = requests.get(f'{url}/user/VarNa1', headers={'accept': 'application/json'})
print("GET user VarNa1\n", res.status_code, res.json())

# Удаление пользователя  VarNa1
res = requests.delete(f'{url}/user/VarNa1')
print("DELETE user\n", res.status_code, res.json())

# Пользователь VarNa1 - проверим удаление
res = requests.get(f'{url}/user/VarNa1', headers={'accept': 'application/json'})
print("GET deleted user VarNa1\n", res.status_code, res.json())

# Найден баг: по PUT создается новая запись, а не обновляется указанная
res = requests.get(f'{url}/user/VarNa', headers={'accept': 'application/json'})
print("GET user VarNa than had been changed to VarNa1 (bug!)\n", res.status_code, res.json())
