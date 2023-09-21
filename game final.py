import random
import time
name=input("what is u name??: ")
print(name)
score=0
score_ia=0
def game(score,score_ia):
	l=["paper","rock","scissor"]
	i=0
	while i<3:
		player=input("what is u choice??: ").lower()
		while player not in l:
			print("wrong input")
			player=input("enter again: ").lower()	
		choice=random.choice(l)
		if player==choice:
			print("u choice: ",player) 
			print("computer choice: ",choice)
			score=score+1
			score_ia=score_ia+1
		elif player=="rock":
			if choice=="scissor":
				print("u choice: ",player) 
				print("computer choice: ",choice)
				score=score+1
			elif choice=="paper":
				print("u choice: ",player) 
				print("computer choice: ",choice)
				score_ia=score_ia+1	
		elif player=="scissor":
			if choice=="rock":
				print("u choice: ",player) 
				print("computer choice: ",choice)
				score_ia=score_ia+1
			elif choice=="paper":
				print("u choice: ",player) 
				print("computer choice: ",choice)
				score=score+1
		elif player=="paper":
			if choice=="rock":
				print("u choice: ",player) 
				print("computer choice: ",choice)
				score=score+1
			elif choice=="scissor":
				print("u choice: ",player) 
				print("computer choice: ",choice)
				score_ia=score_ia+1
		i+=1
	# play_again=input("do u want to try again(y/n)??")
		# if play_again=="n":
		# 	break	
	return score,score_ia 
while True:
	score,score_ia=game(score,score_ia)
	if score>score_ia:
		print("u score is: ",score)
		print("IA score is: ",score_ia)
		print("you won")
	elif score<score_ia:
		print("u score is: ",score)
		print("IA score is: ",score_ia)
		print("you lost")
	elif score==score_ia:
		print("u score is: ",score)
		print("IA score is: ",score_ia)
		print("this is tie")
	play_again=input("would you try to play again(y/n)??")
	if play_again=="n":
		break
			