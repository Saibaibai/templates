from tkinter import *
from PIL import Image,ImageTk
from random Import randint

#main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

#picture
rock_img = ImageTk.PhotoImage(Image.open("rock.user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.user.png"))
scissor_img = Imagetk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

#insert picture
user_label = Label(root, image=scissor_ing, bg = "#9b59b6")
comp_label = Label(root, image=scissor_img_comp, bg = "#9b59b6")
comp_label.grid(row = 1, column = 0)
user_label.grid(row = 1, column = 4)


#scores
playerScore = Label(root, text = 0, font = 100, bg = "#9b59b6", fg = "white")
computerScore = Label(root, text = 0, font = 100, bg = "#9b59b6", fg = "white")
computerScore.grid(row = 1, column = 1)
playerscore.grid(row = 1, column = 3)

#indicators
user_indicator = Label(root, font = 50, text = "User", bg = "#9b59b6", fg = "white")
comp_indicator = Label(root, font = 50, text = "Computer", bg = "#9b59b6", fg = "white")
user_indicator.grid(row = 0, column = 3)
comp_indicator.grid(row = 0, column = 1)

#messages
msg = Label(root, font = 50, bg = "#9b59b6", fg = "white")
msg.grid(row = 3, columnt = 2)

#update message
def updateMessage(x):
	msg["text"] = x
	
#update user score
	def updateUserScore():
	score = int(playerScore["text"])
	score += 1
	playerScore["text"] = str(score)
	
#update computer score
	def updateCompScore():
		score = int(computerScore["text"])
	score += 1
	computerScore["text"] = str(score)

#check winner
	def checkWin(player, computer):
		if player == computer:
			updateMessage("Its a tie!")
		elif player == "rock":
			if computer == "paper":
				updateMessage("You loose")
				updateCompScore()
			else:
				updateMessage("You win")
				updateUserScore()
		elif player == "paper":
			if computer == "scisor":
				updateMessage("You loose")
				updateCompScore()
			else:
				updateMessage("You win")
				updateUserScore()
		elif player == "scissor":
			if computer == "rock":
				updateMessage("You loose")
				updateCompscore()
			else:
				updateMessage("You win")
				updateUserScore()
				
			else:
				pass
			
	
#update choices
	choices = ["rock", "paper", "scissor"]
	def updateChoice(x):
	
	#for computer
	compChoice = choices[randint(0, 2 )]
	if compChoice == "rock";
		comp_label.configure(image = rock_img_comp)
	elif compChoice == "paper":
		user_label.configure(image=paper_img)
	else:
		user_label.configure(image=scissor_img)	


	#for user
	if x == "rock":
		user_label.configure(image=rock_img)
	elif x == "paper":
		user_label.configure(image=paper_img)
	else:
		user_label.configure(image=scissor_img)
		
	checkWin(x, compChoice)

#buttons
rock = Button(root, width = 20, height = 2, text = "Rock", bg = "#FF3E4D", fg = "white", command = lambda:updateChoice("rock")).grid(row = 2, column = 1)
paper = Button(root, width = 20, height = 2, text = "Paper", bg = "#FAD02E", fg = "white", command = lambda:updateChoice("paper")).grid(row = 2, column = 2)
scisosor = Button(root, width = 20, height = 2, text = "Scissor", bg = "#0ABDE3", fg = "white", command = lambda:updateChoice("scissor")).grid(row = 2, column = 3)

root.mainloop()