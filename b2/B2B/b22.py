from flask import *

app= Flask(__name__)

@app.route('/')
def fun():
	return render_template('index.html',msg="")
	
@app.route('/check/',methods = ['POST','GET'])

def check():
	a= checker(request.form['string'])
	return render_template('index.html',msg=a)

def checker(str1):
	fdata=""
	with open('data.txt','rt') as f:
		for line in f:
		
			fdata=fdata + line
	
	c= fdata.replace('.',' ')
	a=c.split(' ')
	
	d= str1.replace('.',' ')
	
	b= d.split(' ')
	z= list(set(a) & set(b))
	
	count=len(z)
	print count
	p= str(float(count)/(len(b))*100)
	
	return p
	
if __name__ == "__main__":
	
	app.run(host='0.0.0.0',port=7888)
