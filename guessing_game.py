from random import *
import time


print("Loading...")
time.sleep(4)
greeting = raw_input("***---Welcome to the Guessing Game!---***\nPlease ENTER your name below to begin.\n...")
greeting2 = raw_input("Welcome " + greeting +"! Please guess a number from 1 to 9, then hit ENTER.")


print("Picking a number...")
time.sleep(2)
nums = randint(1, 9)
print(nums)

if greeting2 == nums:
	print("You got it!")
elif greeting2 < nums:
	print("Your guess is too high.")
elif greeting2 > nums:
	print("Your guess is too low.")
else:
	print("Please enter a valid number.")
	

while greeting2 != nums:
	nice = raw_input("Would you like to try again?")
	if nice == 'yes' or 'Yes':
		pass
	elif nice == 'no' or 'No':
		break

	
