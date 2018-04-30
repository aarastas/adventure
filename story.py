import os
import time
import textwrap
import subs
	
def s000():
	text = '''
		You sit around a warm campfire on a cold night in the forest. You watch as the fire crackles and dances in the cool night breeze. You hear a crack or a twig behind you. Slowly, you turn around, tensing as the approaching noise increases in volume. All of a sudden, the quiet twig cracks turn into wild and ferocious sounds intruding from the darkness upon your small sphere of fire light.	There is a cave enterence just out of reach of the firelight. As the sounds of the forest get louder you wonder if you'd be safer in the cave.
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	choice=input("\n\tDo you brave the darkness and enter the cave? y or n: ")
	os.system("cls")
	return choice
	
def s001():
	text ='''
		You feel that it would be safer in the cave and quickly make your way towards the cave when a crunching sound turns you around.  A hideous beast now stands near the fire, the log you were sitting on just moments ago is now crushed and splintered beneath the foot of the behemoth.  You scream and sprint toward the cave enterence. As you stumble into the cave you dare to glance over your shooulder and see that the beast did not follow you into the mouth of the cave. You try to quiet your breathing and your beating heart, you can see it's sillowette at the mouth of the cave.  It tunes and walkes back out into the forest.  Before you lyes two passageways. The one to the left dissapears into darkness, while there is a faint light off to the right.  Not daring to go back out to yoru fire you pick a path.
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	choice=input("\n\tDo you choose left or right? l or r: ")
	os.system("cls")
	return choice

def s002():
	text ='''
		Deciding that the fire would be safer and more comforatable than the dark dank cave, despite the wild sounds coming from the woods.  You stretch out moving your feet closer to the fire and relax, convincing yourself there's nothing to be afraid of when there is a loud snarling sound behind you, you turn to look just as claws collide with your head and fangs snap down. 
	''' #In the split second you're still alive you regret choosing the fire over the cave.
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	subs.dead()
	
def s003():
	text ='''
		You turn left and stumble blindly down the rough tunnel filled with stalagmites that threten to impale you with any stumble or mistep. You walk with caution, minding each sharp point. You trip over something and fall to the ground.  Did you imagine that it made a grunting sound?  It sure didn't feel like a rock and there seems to be a faint smell of alchohol.  You, crawl on your hands and knees feelin for a wall when you touch something that makes a clinking sound.  You feel back toward where it was and grab it.  It feels like a key, you put it in your pocket and continue onward putting distance between you and what ever or who ever it was that you tripped over.  After a few minutes it seems like there's a light up ahead. 
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	return(True) #You got the key

def s004(key):
	choice="n"
	if key==False:
		text ='''
			You turn toward the faint light, looking briefly over your shoulder, then continue. After some time you come to the source of the light, a window in an old wooded door. You test the door to see if it's open and find out it's not. 
		'''
		print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
		choice=input("\n\tDo you go back to the warmth of your fire to see if the beast is gone? y or n: ")
		os.system("cls")
	else:
		text ='''
			You turn toward the faint light, looking briefly over your shoulder, then continue. After some time you come to the source of the light, a window in an old wooded door. You pull out the rusty skeleton key that you found and try it in the lock.  You hear a click and slowly push open the door.  It screeches loudly.  You stop and look around, proceeding more slowly, drawing out the screeching, but it is quieter.  The room seems as if it has been ocupied recently.  The light is coming from an lanturn running low on oil hanging from an iron hook in the wall.  There's a table and another door that leads into a small pantry of sorts, a table with some dishes on it, a chair and a bed.  Ther's a rug under the table that's partialy covering what looks liek a trap door.  You start to investigate when you year suffling from out in the tunnel.  You quickly look around for a place to hide.  You could hide in the closet, or call out to see who's there. 
		'''
		print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
		choice=input("\n\tDo you hide? y or n: ")
		os.system("cls")
	return choice

def s005():
	text ='''
		blah 5
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	input("")
	

def s006():
	text ='''
		blah 6
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	input("")

def s007():
	text ='''
		You struggle to open the door to no avail.  And backtrack to take the other tunnel.
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	input("")
	

def s008():
	text ='''
		blah 8
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	input("")

def s009():
	text ='''
		blah 9
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	input("")
	

def s010():
	text ='''
		blah 10
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	input("")

def s011():
	text ='''
		blah 11
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	input("")
	

def s012():
	text ='''
		blah 12
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	input("")

def s013():
	text ='''
		blah 13
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	input("")
	

def s014():
	text ='''
		blah 14
	'''
	print ("\n\n"+textwrap.indent(textwrap.fill(textwrap.dedent(text)),"\t"))
	input("")