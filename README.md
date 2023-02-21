# Task_24_3_3
Задание 24.3.3: реализация запросов GET, POST, DELETE, PUT в https://petstore.swagger.io/

В программе task_24_3_3.py реализованы запросы GET, POST, DELETE, PUT к api https://petstore.swagger.io/ в следующей последовательности:
1. POST: создание пользователя VarNa
2. GET: проверка наличия пользователя VarNa
3. GET: аутентификация пользователя VarNa
4. PUT: изменение пользователя VarNa на VarNa1
5. GET: проверка наличия пользователяя VarNa1
6. DELETE: удаление пользователя VarNa1
7. GET: проверка отсутствия пользователя VarNa1 (ошибка 404)

Внимание! Найден баг! По PUT создается новый пользователь, а не изменяются данные указанного. Поэтому в системе остается пользователь VarNa

8. GET: проверка наличия пользователя VarNa - баг, пользователь есть!
