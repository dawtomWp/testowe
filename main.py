
ADMIN = "admin"
MODERATOR = "moderator"
USER = "user"
BAN = "banned"

# account_type = USER

# if account_type == ADMIN:
#     print("Zalogowano jako admin")
# elif account_type == MODERATOR:
#     print("Zalogowano jako moderator")
# elif account_type == USER:
#     print("Zwykły użytkownik")
# else:
#     print("Wystąpił błąd")

account_type = MODERATOR
is_logged = False

# if account_type == USER and is_logged == True:
#     print("Witaj w panelu użytkownika")
# else:
#     print("Wystąpił błąd")


# if account_type == ADMIN or account_type == MODERATOR:
#     print("Witaj w panelu administracji")

# >
# <
# >=

# x = 5
# y = 4

# print(x != y)

# if x != y:
#     print("Zgadza się")


# users = ['Jan','Anna','John']

# result = 'Jan' in users 

# if result:
#     print("Zgadza się")


result2 = "" # False, "", 0 - Falsely values

# if result2:
#     print(23)
#     print("Test")


# sentence = "lorem ipsum"

# if "ipsum" in sentence:
#     print("Znaleziono ipsum")


# users = ['Anna','Sylwia','Jan','John',2,3,4,5,"Dawid","Adam"]

# last_user = users[len(users) - 1] # users[7]
# print("Najnowszy użytkownik to " + last_user)

# # for x in users:
# #     print("To jest " + x)

# for num in range( len(users) ):
#     # print("Liczba", num)
#     print(users[num])



# fruits = ["Jabłka","Gruszki","Pomarańcze"]

# for i,fruit in enumerate(fruits):
#     print(f"Owoc: {fruit} - Pozycja nr: {i} {2*5}")


import random

num = 0
iterations = 10

# while num != 7:
#     if(iterations >= 2000):
#         print("Nie udało się wylosować liczby")
#         break
#     num = random.randint(0,5000)
#     iterations += 1
#     print(f"Wylosowano liczbę {num}. Udało się za {iterations + 1} razem")

# for i in range(10):
#     if i == 5 or i == 7:
#         continue
#     print(i)



# even = 0
# odd = 0

# for i in range(100):
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print(f"Liczby parzyste {even}")
# print(f"Liczby nieparzyste {odd}")



# numbers = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for row in numbers:
#     for item in row:
#         print(item)

# person = {
#     "firstname":"Jan",
#     "lastname":"Kowalski",
#     "age":24
# }

# print( person["firstname"] )

# print(f"To jest {person['firstname']} {person['lastname']}")

# student_scores = {
#     "Alice":85,
#     "Jan":20,
#     "Dawid":30,
#     "Jack":90
# }

# for name,score in student_scores.items():
#     print(f"Uczeń/Uczennica: {name} - {score} pkt")








print("Wybierz liczbę")
operation = input()

# if operation == 1.......
