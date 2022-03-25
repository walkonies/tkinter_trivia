import tkinter as tk 
from question import Question

# Set up window
root = tk.Tk()
root.title('Vulcan Triva Game')
root.geometry('300x200')


# Global data
q = []
results = []


def triviaGame(q):
	# Create widgets
	questionBox = tk.Label(root,text=q.getQ(), bg='blue', fg='white')
	trueBut = tk.Button(root, text="TRUE", fg='green', bg='white', command=lambda:clickAwnser(q, True))
	falseBut = tk.Button(root, text='FALSE', fg='red', bg='white', command=lambda:clickAwnser(q, False))
  
	# Pack widgets
	questionBox.pack(ipadx=10, ipady=10, fill='x')
	trueBut.pack(ipadx=10, ipady=10, expand=True, side='left', fill='both')
	falseBut.pack(ipadx=10, ipady=10, expand=True, side='right', fill='both')


def clickAwnser(q, a):
	res = None
	# Bitwise check for correct answer
	# T T -> T
	# T F -> F
	# F T -> F
	# F F -> T
	res = not q.getA() ^ a

	# Update global results
	global results
	results.append(res)

	# Show result of question
	showRes(res)


def showRes(res):
	# Clear answers
	clearAns()

	# Create output label
	output = 'Correct' if res else 'Incorrect'
	outputLabl = tk.Label(root,text=output, bg='green' if res else 'red', fg='white')
	outputLabl.pack(ipadx=10, ipady=10, expand=True, fill='both')

	#Create next question button
	if len(q) > 0:
		NextBut = tk.Button(root, text="NEXT", fg='black', command=nextQuestion)
		NextBut.pack(ipadx=10, ipady=10)

	# If no more questions show results
	else:
		ResBut = tk.Button(root, text="RESULTS", fg='black', command=printReults)
		ResBut.pack(ipadx=10, ipady=10)


def nextQuestion():
	# Clear screen
	clear()
	# Start next question
	triviaGame(q.pop(0))


def printReults():
	clear()
	# Get total correct
	score = sum(results)

	# Get percent right
	percent = score/len(results)

	# Create result widgets
	endLabl = tk.Label(root,text='Good game!', bg='white')
	scoreLabl = tk.Label(root, text=f'SCORE: {score}', fg='red', bg='white')
	percentLabl = tk.Label(root, text= f'{int(percent*100)}%', bg='white')

	# Pack result widgets
	endLabl.pack(ipadx=10, ipady=10, fill='x')
	scoreLabl.pack(ipadx=10, ipady=10, fill='x')
	percentLabl.pack(ipadx=10, ipady=10, fill='x')

	# Create and pack quit
	quit = tk.Button(root, text='QUIT', bg = 'black', fg='red', command=root.quit)
	quit.pack(ipadx=10, ipady=10, expand= True)


def clearAns():
	# Clear all but question label
	widgets = root.pack_slaves()
	for i in range(1, len(widgets)):
		widgets[i].destroy()


def clear():
	# Clear all widgets
	for widget in root.pack_slaves():
		widget.destroy()


# Read example questions from file
def getQuestions():
	global q
	with open('/Users/walker/Documents/Code/Python/Games/Trivia/questions.txt', 'r') as file:
		for line in file.readlines():
				q.append(Question.from_str(line))


# Play game
def main():
	# Get questions from file
	getQuestions()
	# Setup first question
	nextQuestion()
	# GUI loop
	root.mainloop()
	# Terminate
	print('Goodbye')
	
if __name__ == '__main__':
	main()