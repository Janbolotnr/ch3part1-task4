import random

guessesTaken = 0

print("What is your name? ")

myName = input()
number = random.randint(1,100)

for guessesTaken in range(10):
    print('Poprobui ugadat.')
    guess = input()
    guess = int(guess)
    
    if guess < number:
        print('Your number is small')
    if guess > number:
        print('Your number is a big')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken+1)
    print('OK ,' + myName + '! You did it ' + guessesTaken)
if guess != number:
    number == str(number)
    print('I did it', + number + '.') 




















# import random
 
# count = 0
# num1, num2 = 1, 100
# enter = 0
 
# while enter != 'y':
#     count += 1
#     number = random.randint(num1, num2)
#     print (number)
#     enter = input("Угадал 'y', больше '>' ,меньше '<': ")
    
#     if enter == '<':
#         num2 = number-1
#     elif enter == '>':
#         num1 = number+1
 
# print('\n\nТак просто... Всего ' + str(count) +' попыток :))))\n\n' \
#       + '\t\t' +str(number))




# count = 0
# num1, num2 = 1, 100
# enter = 0 
# while enter != 'y':
#     count += 1
#     number = round((num1+num2) / 2)
#     print (number)
#     enter = input("Угадал 'y', больше '>' ,меньше '<': ")
    
#     if enter == '<':
#         num2 = number
#     elif enter == '>':
#         num1 = number
 
# print('\n\nТак просто... Всего ' + str(count) +' попыток :))))\n\n' \
#       + '\t\t' +str(number))

