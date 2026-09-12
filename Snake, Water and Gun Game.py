import random
import sys
print("===== Welcome! To Snake,Water and Gun Game =====")
choice=input("s = Snake\nw = Water \ng = Gun\nEnter Your Choice : ")
if choice=="s":
	print("You selected : Snake.")
elif choice=="w":
	print("You selected : Water.")
elif choice=="g":
	print("You selected : Gun.")
else:
	print("Invalid choice! Try Again.")
	sys.exit()
computer=random.choice(["s","w","g"])
if computer=="s":
	print("Computer selected : Snake.")
elif computer=="w":
	print("Computer selected : Water.")
elif computer=="g":
	print("Computer selected : Gun.")
if choice==computer:
	print("Match Draw !")
elif (choice=="s" and computer=="w")or(choice=="w" and computer=="g")or(choice=="g" and computer=="s"):
	print("You Win !")
else:
	print("Computer Win !")


	
