import random

random.randint(1,10)

print('\nHello, Today your fortune will be unfolded. I am the ultimate magic ball much more then 8. Enjoy!\n')

UserInput1 = input('Please enter any word of your choice. Honestly anything can be taken\n')

def key():

    FinalAnswer = random.randint(1,3)

    print("Now the final piece of advice for you")

    if FinalAnswer == 1:
        print('Do not doubt yourself to much.')
    elif FinalAnswer == 2:
        print('Be cautious. Do not rush.')
    elif FinalAnswer == 3:
        print('Take risks. There may be dpythonanger, but there is much more to gain')


def Key1():

    print('Your future is a vast one with much potential')
    Answer1 = float(input('Now enter your lucky number, If you think you do not have one just pick anything\n\n'))
    
    if Answer1 == 1:
        print('\nYour future is solid and sturdy. A good path in life')
    elif Answer1 == 0:
        print('\nYour life may seem empty, but it will not follow a dark demise')
    elif Answer1 < 0:
        print('\nYour life is upside down in ways. It will be filled with twist it is up to you if you make it a good life.')
    elif Answer1 > 1000:
        print("....\n....\n Unbeliveable.. I can not see your future.")
    else:
        print("\nYour fate is quite mondane. It's normal")
    key()

def Key2():
    
    print('Your future will be very varied and you life shaky')
    
    Answer2 = random.randint(1,10)
    Multiplyer = random.randint(1,10)
    Return = Answer2*Multiplyer
    
    print(f'Well you will live for the next {Return} Years')

    if Return < 9:
        print(f"Oh no, this fate is quite unfortunate only {Return} Years to live...")
    elif Return < 25 and not Return < 9:
        print(f"Well this is not the worst fate you can have. Make the most of the next {Return} years...")
    elif Return < 100 and not Return < 25:
        print(f'Your life is plenty long a solid {Return} years')
    else:
        print(f"Incredible, unbelievable you will live {Return} Years....")  
    key()      

def Key3():
    
    print('Now we shall see the next major event in your life')
    
    Month = random.randint(1,12)
    Day = random.randint(1,7)
    
    if Month == 1:
        Result = 'January'
    elif Month == 2:
        Result = 'February'
    elif Month == 3:
        Result = 'March'
    elif Month == 4:
        Result = 'April'
    elif Month == 5:
        Result = 'May'
    elif Month == 6:
        Result = 'June'
    elif Month == 7:
        Result = 'July'
    elif Month == 8:
        Result = 'August'
    elif Month == 9:
        Result = 'September' 
    elif Month == 10:
        Result = 'October'
    elif Month == 11:
        Result = 'November'
    elif Month == 12:
        Result = 'December'
    
    if Day == 1:
        Result2 = 'Monday'
    elif Day == 2:
        Result2 = 'Tuesday'
    elif Day == 3:
        Result2 = 'Wenesday'
    elif Day == 4:
        Result2 = 'Thursday'
    elif Day == 5:
        Result2 = 'Friday'
    elif Day == 6:
        Result2 = 'Saturday'
    elif Day == 7:
        Result2 = 'Sunday'

    print(f'And your fate is in {Result} on a {Result2} something life changing will happen')
    key()


def Key4():
    print('Your fortune is Simply good..')

if len(UserInput1.lower()) <= len('123'.lower()):
    print('\nkey 1 has been Opened\n'.upper())
    Key1()
elif len(UserInput1.lower()) <= len('12345'.lower()) and not len(UserInput1.lower()) <= len('123'.lower()):  
    print('\nkey 2 has been unlocked'.upper())
    Key2()
elif len(UserInput1.lower()) <= len('12346789'.lower()) and not len(UserInput1.lower()) <= len('12345'.lower()):
    print('\nKey 3 has been unshakled')  
    Key3() 
else:
    print('\nkey 4 has been unleashed'.upper())
    Key4()

