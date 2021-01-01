import random
import time
print('Welcome to the game. I hope you know the rules. \n')
# time.sleep(3)
print('The game begins now!\n')
# time.sleep(2)
isoc = 'Heads'
cc = ['Flip', 'Not Flip']
ui1 = input("Choose to 'Flip' or 'Not Flip' the coin. I choose to ")
ci1 = random.choice(cc)
if ci1 == 'Flip':
    isoc = 'Tales'
else:
    isoc = 'Heads'
    
if ui1 == 'Flip' and isoc == 'Heads':
    isoc = 'Tales'
elif ui1 == 'Flip' and isoc == 'Tales':
    isoc = 'Heads'     
else:
    isoc = isoc
ci2 = random.choice(cc)
if ci2 == 'Flip' and isoc=='Heads':
    isoc = 'Tales'
elif ci2=='Flip' and isoc=='Tales':
    isoc = 'Heads'

if isoc == 'Tales':
    print('You Win')
    
if isoc == 'Heads':
    print('Computer Wins')
