# Question class
class Question:
	def __init__(self, question, answer):
		self.setQ(question)
		self.setA(answer)
    	
	def setQ(self, question):
		self.q = question
    
	def setA(self, answer):
		self.a = bool(answer)
    
	def getQ(self):
		return self.q
    
	def getA(self):
		return self.a

	@classmethod
	def from_str(cls, question):
		question, answer = question.split('-')
		return cls(question, int(answer))
	
	def __str__(self):
		return(f'Question: {self.getQ()} Answer: {self.getA()}')

