import tkinter as tk
import random
import os


def play_rock():
	global player_play

	human_icon.configure(image=rock)
	player_play = 0
	random_computer_play()


def play_paper():
	global player_play

	human_icon.configure(image=paper)
	player_play = 1
	random_computer_play()


def play_scissors():
	global player_play

	human_icon.configure(image=scissors)
	player_play = 2
	random_computer_play()


def clear_screen():
	human_icon.configure(image=void)
	computer_icon.configure(image=void)


def random_computer_play():
	global computer_play

	random_value = random.randint(0, 2)
	computer_play = random_value
	computer_icon.configure(image=[rock, paper, scissors][random_value])
	update_score()


def update_score():
	global player_play
	global computer_play
	global player_score_value
	global computer_score_value

	if player_play == 0 and computer_play == 1:
		computer_score_value += 1
	elif player_play == 0 and computer_play == 2:
		player_score_value += 1
	elif player_play == 1 and computer_play == 2:
		computer_score_value += 1
	elif computer_play == 0 and player_play == 1:
		player_score_value += 1
	elif computer_play == 0 and player_play == 2:
		computer_score_value += 1
	elif computer_play == 1 and player_play == 2:
		player_score_value += 1

	computer_score.configure(text=str(computer_score_value))
	player_score.configure(text=str(player_score_value))


computer_score_value = 0
player_score_value = 0

player_play = None
computer_play = None


def launch():
	global computer_score
	global player_score
	global void
	global rock
	global paper
	global scissors
	global human_icon
	global computer_icon

	window = tk.Tk()
	window.title('Rock, paper, scissors')

	current_dir = os.path.dirname(os.path.abspath(__file__))

	void = tk.PhotoImage(file=current_dir+'/images/rien.gif')
	versus = tk.PhotoImage(file=current_dir+'/images/versus.gif')
	rock = tk.PhotoImage(file=current_dir+'/images/pierre.gif')
	paper = tk.PhotoImage(file=current_dir+'/images/papier.gif')
	scissors = tk.PhotoImage(file=current_dir+'/images/ciseaux.gif')

	human_label = tk.Label(window, text='Human:', font=('Helvetica', 16))
	human_label.grid(row=0, column=0)

	computer_label = tk.Label(window, text='Computer:', font=('Helvetica', 16))
	computer_label.grid(row=0, column=2)

	player_score = tk.Label(window, text="0", font=("Helvetica", 16))
	player_score.grid(row=1, column=0)

	computer_score = tk.Label(window, text="0", font=("Helvetica", 16))
	computer_score.grid(row=1, column=2)

	human_icon = tk.Label(window, image=void)
	human_icon.grid(row=2, column=0)

	versus_icon = tk.Label(window, image=versus)
	versus_icon.grid(row=2, column=1)

	computer_icon = tk.Label(window, image=void)
	computer_icon.grid(row=2, column=2)

	rock_button = tk.Button(window, command=play_rock)
	rock_button.configure(image=rock)
	rock_button.grid(row=4, column=0)
	paper_button = tk.Button(window, command=play_paper)
	paper_button.configure(image=paper)
	paper_button.grid(row=4, column=1)
	scissors_button = tk.Button(window, command=play_scissors)
	scissors_button.configure(image=scissors)
	scissors_button.grid(row=4, column=2)
	leave_button = tk.Button(window,text='Quitter',command=window.destroy)
	leave_button.grid(row=5, column=2, pady=10, sticky=tk.W)

	window.mainloop()
