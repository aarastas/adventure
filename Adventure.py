import subs	
import story
import os
key=False

# roll = subs.roll_dice(2)
os.system("cls")

subs.title()
choice=story.s000()
if ("y"==choice):
	choice=story.s001()
	if ("l"==choice):
		key=story.s003()				#you get the key
		input("")
	else:
		choice=story.s004(key)
		if ("y"==choice):
			story.s002() 				#death by the fire
		else:							#you backtrack and go left
			story.s007()				#you take the other path
			key=story.s003()			#you get the key
	if (key==True):
		choice=story.s004(key)
		if ("y"==choice): 
			story.s008()				#you hid
		else:
			story.s009()				#you said hi
else:
	story.s002()						#death by the fire

os.system("cls")
