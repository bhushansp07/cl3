from bitstring import BitArray as dsp
from flask import *
app = Flask(__name__)

def booth(m,r,x,y):
	size=x+y+1
	
	mA=dsp(int=m,length=size)
	A=mA<<(y+1)
	
	mS=dsp(int=-m,length=size)
	S=mS<<(y+1)
	
	mP=dsp(int=r,length=y)
	mP.prepend(dsp(int=0,length=x))
	P=mP<<(1)

	for i in  range(1,y+1):
		if P[-2:] == '0b01':
			P=dsp(int=P.int+A.int,length=size)
		elif P[-2:] == '0b10':
			P=dsp(int=P.int+S.int,length=size)
		P=dsp(int=(P.int>>1),length=P.len)
	P=P[:-1]
	return P.bin,P.int

@app.route('/')
def f():
	return render_template("index.html")

@app.route('/',methods=['POST'])
def g():
	text1 = int(request.form['text1'])
	text2 = int(request.form['text2'])
	a,b=booth(text1,text2,8,8)
	return "Answer in Binary: "+str(a)+"<br>Answer: "+str(b)
	
if __name__ == '__main__':
	app.run('localhost', debug=True)
