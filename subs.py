import random
import os
import time
import textwrap
min = 1
max = 7

def dice():
	d1 = random.randint(min, max)
	# d2 = random.randint(min, max)
	return d1

def roll_dice(tries):
	count=1
	roll=0
	roll_again = "yes"
	while (roll_again == "yes") or (roll_again == "y"):
		print (str(count)+"/"+str(tries)+" You rolled a "+str(dice()))
		count+=1
		if (count > tries):
			break
		roll_again = input("Roll the dices again?")
	return roll
	
def coin():
	c1 = random.randinit(1,2)
	return c1
	
def title():
	print ("\n\n")
	print ("\t                      Welcome")
	time.sleep(0.125)
	print ("\t                        to")
	time.sleep(0.25)
	print ("\t _______    __                   __                    ")
	print ("\t|       .--|  .--.--.-----.-----|  |_.--.--.----.-----.")
	print ("\t|   |   |  _  |  |  |  -__|     |   _|  |  |   _|  -__|")
	print ("\t|   _   |_____|\___/|_____|__|__|____|_____|__| |_____|")
	print ("\t|   |   |                                              ")
	print ("\t|   |   |                                              ")
	print ("\t`--- ---'                                              ")
	time.sleep(0.25)
	print ("\t                        by")
	time.sleep(0.125)
	print ("\t                   Arwen Nielsen")
	input("")
	os.system("cls")
	

	
def dead():
	input("")
	os.system("cls")
	print ("\n")
	print ("\t                 uuuuuuu                 ")
	print ("\t             uu$$$$$$$$$$$uu             ")
	print ("\t          uu$$$$$$$$$$$$$$$$$uu          ")
	print ("\t         u$$$$$$$$$$$$$$$$$$$$$u         ")
	print ("\t        u$$$$$$$$$$$$$$$$$$$$$$$u        ")
	print ("\t       u$$$$$$$$$$$$$$$$$$$$$$$$$u       ")
	print ("\t       u$$$$$$$$$$$$$$$$$$$$$$$$$u       ")
	print ("\t       u$$$$$$*   *$$$*   *$$$$$$u       ")
	print ("\t       *$$$$*      u$u       $$$$*       ")
	print ("\t        $$$u       u$u       u$$$        ")
	print ("\t        $$$u      u$$$u      u$$$        ")
	print ("\t         *$$$$uu$$$   $$$uu$$$$*         ")
	print ("\t          *$$$$$$$*   *$$$$$$$*          ")
	print ("\t            u$$$$$$$u$$$$$$$u            ")
	print ("\t             u$*$*$*$*$*$*$u             ")
	print ("\t  uuu        $$u$ $ $ $ $u$$       uuu   ")
	print ("\t u$$$$        $$$$$u$u$u$$$       u$$$$  ")
	print ("\t  $$$$$uu      *$$$$$$$$$*     uu$$$$$$  ")
	print ("\tu$$$$$$$$$$$uu    *****    uuuu$$$$$$$$$$")
	print ("\t$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*")
	print ("\t ***      **$$$$$$$$$$$uu **$***         ")
	print ("\t           uuuu **$$$$$$$$$$uuu          ")
	print ("\t  u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$ ")
	print ("\t  $$$$$$$$$$****           **$$$$$$$$$$$*")
	print ("\t   *$$$$$*                      **$$$$** ")
	print ("\t     $$$*                         $$$$*  ")
	os.system("cls")
	time.sleep(0.25)
	print ("\n")
	print ("\t                 uuuuuuu                 ")
	print ("\t             uu$$$$$$$$$$$uu             ")
	print ("\t          uu$$$$$$$$$$$$$$$$$uu          ")
	print ("\t         u$$$$$$$$$$$$$$$$$$$$$u         ")
	print ("\t        u$$$$$$$$$$$$$$$$$$$$$$$u        ")
	print ("\t       u$$$$$$$$$$$$$$$$$$$$$$$$$u       ")
	print ("\t       u$$$$$$$$$$$$$$$$$$$$$$$$$u       ")
	print ("\t       u$$$$$$*   *$$$*   *$$$$$$u       ")
	print ("\t       *$$$$*      u$u       $$$$*       ")
	print ("\t        $$$u       u$u       u$$$        ")
	print ("\t        $$$u      u$$$u      u$$$        ")
	print ("\t         *$$$$uu$$$   $$$uu$$$$*         ")
	print ("\t          *$$$$$$$*   *$$$$$$$*          ")
	print ("\t            u$$$$$$$u$$$$$$$u            ")
	print ("\t             u$*$*$*$*$*$*$u             ")
	print ("\t  uuu        $$u$ $ $ $ $u$$       uuu   ")
	print ("\t u$$$$        $$$$$u$u$u$$$       u$$$$  ")
	print ("\t  $$$$$uu      *$$$$$$$$$*     uu$$$$$$  ")
	print ("\tu$$$$$$$$$$$uu    *****    uuuu$$$$$$$$$$")
	print ("\t$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*")
	print ("\t ***      **$$$$$$$$$$$uu **$***         ")
	print ("\t           uuuu **$$$$$$$$$$uuu          ")
	print ("\t  u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$ ")
	print ("\t  $$$$$$$$$$****           **$$$$$$$$$$$*")
	print ("\t   *$$$$$*                      **$$$$** ")
	print ("\t     $$$*                         $$$$*  ")
	os.system("cls")
	time.sleep(0.25)
	print ("\n")
	print ("\t                 uuuuuuu                 ")
	print ("\t             uu$$$$$$$$$$$uu             ")
	print ("\t          uu$$$$$$$$$$$$$$$$$uu          ")
	print ("\t         u$$$$$$$$$$$$$$$$$$$$$u         ")
	print ("\t        u$$$$$$$$$$$$$$$$$$$$$$$u        ")
	print ("\t       u$$$$$$$$$$$$$$$$$$$$$$$$$u       ")
	print ("\t       u$$$$$$$$$$$$$$$$$$$$$$$$$u       ")
	print ("\t       u$$$$$$*   *$$$*   *$$$$$$u       ")
	print ("\t       *$$$$*      u$u       $$$$*       ")
	print ("\t        $$$u       u$u       u$$$        ")
	print ("\t        $$$u      u$$$u      u$$$        ")
	print ("\t         *$$$$uu$$$   $$$uu$$$$*         ")
	print ("\t          *$$$$$$$*   *$$$$$$$*          ")
	print ("\t            u$$$$$$$u$$$$$$$u            ")
	print ("\t             u$*$*$*$*$*$*$u             ")
	print ("\t  uuu        $$u$ $ $ $ $u$$       uuu   ")
	print ("\t u$$$$        $$$$$u$u$u$$$       u$$$$  ")
	print ("\t  $$$$$uu      *$$$$$$$$$*     uu$$$$$$  ")
	print ("\tu$$$$$$$$$$$uu    *****    uuuu$$$$$$$$$$")
	print ("\t$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*")
	print ("\t ***      **$$$$$$$$$$$uu **$***         ")
	print ("\t           uuuu **$$$$$$$$$$uuu          ")
	print ("\t  u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$ ")
	print ("\t  $$$$$$$$$$****           **$$$$$$$$$$$*")
	print ("\t   *$$$$$*                      **$$$$** ")
	print ("\t     $$$*                         $$$$*  ")
	print ("\t             GAME OVER MAN               ")
	input("")