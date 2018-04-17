from bottle import get,post,request,run,template # or route

@get ('/login') # or @route('/login')
def login():

	return '''
		<form action="/login" method="post">
		
		Testing String: <input name="text" type="text"/>
		<input value = "Login" type="submit" />
		</form>
		 
	
	'''
	
@post ('/login') # or @route('/login',method = 'POST') 
def check():
	with open ("data.txt","r") as myfile:
		text1 = myfile.read()
	text2 = request.forms.get('text')
	ret = lcs(text1,text2)
	if ret:
		for s in ret:
			print (s)
		ln = len(ret)
		
		return template('<H1> The plagrism percent is {{val}}% </H1>',val=float(ln)/len(text1.split(' '))*100)
	
	else:
	
		return template('<H1> The plagrism percent is {{val}}% </H1>',val=0)
		
		
def lcs(text1,text2):
	S = text1
	T = text2
	
	sWords = S.split(' ') 
	dWords = T.split(' ')
	
	m = len(sWords)
	n = len(dWords)
	
	counter = [[0]*(n + 1) for x in range(m + 1)]
	longest = 0
	lcs_set = []
	for i in range(m):
		for j in range(n):
			if sWords[i] == dWords[j]:
				c = counter[i][j] + 1
				counter[i+1][j+1] = c
				if c > longest:
					longest = c
				elif c == longest:
					longest = c
				lcs_set.append(sWords[i])
				
	return lcs_set
	
run	(host='localhost',port='7000')			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
