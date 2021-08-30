import random
import pyfiglet
print("****About the game****")
print("1.Gamer has three chances to guess the random number")

print("2.If gamer guesses correct number in three attempts then he/she will won the game")

print("3.If gamer not gueses the correct number in three attemps then he/she loose the game")

a=raw_input("enter name of the player:")
print("choices for the game")
print("1.low range which is from 1-10")
print("2.avg range which is from 1-25")
print("3.high range which is from 1-50")
print("\n")
b=int(input("enter ur choice:"))
print("\n")
if(b==1):
	i=0
	c=None
	
	while(i<3):
		i=i+1
		d=random.randint(1,10)
		c=input("guess the number:")
		print("\n")
		c=int(c)
		print("random number from given range:"+str(d))
		print("\n")
		if(c==d):
			pyfiglet.print_figlet(a)
			pyfiglet.print_figlet("    you  won ")
			break
	else:
		pyfiglet.print_figlet(a)
                pyfiglet.print_figlet("     you  loose")

if(b==2):
	i=0
	c=None
	while(i<3):
		i=i+1
		d=random.randint(1,25)
		c=input("guess the number:")
		print("\n")
		c=int(c)
		print("random number from given range:"+str(d))
		print("\n")
		if(c==d):
			pyfiglet.print_figlet(a)
                        pyfiglet.print_figlet("    you  won ")
			break
	else:
		pyfiglet.print_figlet(a)
                pyfiglet.print_figlet("    you  loose ")
if(b==3):
	i=0
	c=None
	while(i<3):
		i=i+1
		d=random.randint(1,50)
		c=int(input("guess the number:"))
		print("n")
		print("random number from given range:"+str(d))
		print("\n")
		if(c==d):
			pyfiglet.print_figlet(a)
                        pyfiglet.print_figlet("    you  won ")
			break
	else:
		pyfiglet.print_figlet(a)
                pyfiglet.print_figlet("    you  loose ")
if(b>3):
	print("enter correct choice")
	

        	









