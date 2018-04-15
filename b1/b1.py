import json
import unittest

class MyTestCases(unittest.TestCase):
	def test_positive(self):
    		self.assertEqual(run("input2.json"), True)
  	def test_negative(self):
    		self.assertEqual(run("input3.json"), False)

def isattack(board,r,c):
	#attacking in col?
 	for i in range(r):
  		if(board[i][c]==1):
   			return True

	#attacking in diag?
 	i=r-1
 	j=c-1

 	while i>=0 and j>=0:
  		if(board[i][j]==1):
   			return True
  		i-=1
  		j-=1
  
	#attacking in diag?
 	i=r-1
 	j=c+1

 	while i>=0 and j<8:
  		if(board[i][j]==1):
   			return True
  		i-=1
  		j+=1
 	return False

def solve(board,row):
	i=0
 	while i<8:
  		if (not isattack(board,row,i)):
   			board[row][i]=1
   			if row==7:
    				return True
   			else:
				if(solve(board,row+1)):
		 			return True
				else:
		 			board[row][i]=0
  		i=i+1
 	if i==8:
  		return False

def run(filename):
  
 	board=[[0 for x in range(8)] for x in range(8)]

 	if __name__=='__main__':
  		data=[]
  		with open(filename, 'r') as f:
   			data=json.load(f)

  	if (data["start"]>7 or data["start"]<0):
   		print "Invalid input"
   		return False 

  	board[0][data["start"]]=1

  	if (solve(board,1)):
  		print "8 Queens solved!!"
   		print "Board Configuraion"

   		for i in range(8):
    			for j in range(8):
     				print str(board[i][j])+"  ",
    			print "\n"

   		return True
  	else:
   		print "8 Queens not solved"
 
run('input.json')
print "\n--------TESTING--------\n"
unittest.main()
