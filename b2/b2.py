from __future__ import division
from flask import Flask,render_template,request
import string

class Pcheck():
  _data = None
  
  def __init__(self,data):
    self._data = Pcheck.str_to_set(data)
    
  @staticmethod  
  def str_to_set(data):
    for p in list(string.punctuation+'\n'):
      data = data.replace(p,' ')
    return set(data.lower().strip().split(' '))-set([''])
    
  def check(self,text):
    testset = Pcheck.str_to_set(text)
    lenp = len(testset & self._data)
    return (lenp/len(testset))*100

#text1 = "Hello\nbye...kill bill\n\nsimba"
with open('data.txt', 'r') as myfile:
    dataset=myfile.read().replace('\n', '')
p=Pcheck(dataset)


app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('final.html')
  
  
@app.route('/',methods=['POST'])
def plagcheck():
  global p
  text = request.form['value']
  sc= p.check(text)
  response = "Plagiarism Score: "+str(sc)
  return (response)
 
if __name__ =="__main__":
  app.run("localhost",port=1234,debug=True)
