import string
class InvalidKeyException(Exception):
	pass
class InvalidMode(Exception):
	pass
  
class Cipher:
  
	@staticmethod
	def numeric_key(st):
		st =st.strip().lower()
		return [ord(x)-ord('a') for x in list(st)]
    
	@staticmethod
	def caesar(st,key,mode='encrypt'):
		st= st.lower()
		if mode not in ['encrypt','decrypt']:
			raise InvalidMode("Mode must be encrypt or decrypt")
    		if key <0 or key > 25:
      			raise InvalidKeyException("Key must be between 0 and 25")
    		return st.translate(Cipher.table(key,mode))
  
  	@staticmethod
  	def table(key,mode):
  		assert (mode in ['encrypt','decrypt']),"Invalid Mode"
    		alpha = string.ascii_lowercase
    		salpha = alpha[key:]+alpha[:key]
    		if mode == 'encrypt':
      			return string.maketrans(alpha,salpha)
    		return string.maketrans(salpha,alpha)
    
  	@staticmethod
  	def vignere(st,keystr,mode='encrypt'):
  		st = st.strip().lower()
    		l = len(st)
    		keys = Cipher.numeric_key(keystr)
    		tables = [Cipher.table(key,mode) for key in keys]
    		return "".join([c.translate(tables[i%l]) for i,c in enumerate(st)])
    
pt=raw_input("Enter Plain Text: ")
k1=raw_input("Enter key(Interger between 0 to 26): ")
k2=raw_input("Enter key(Size should same as Plain Text): ")

print "------------Ceasar Cipher------------"
cipher =  Cipher.caesar(pt,int(k1)+1,mode='encrypt')
print 'Plain Text: ', Cipher.caesar(cipher,int(k1)+1,mode='decrypt')
print 'Cipher Text: ', cipher

print "------------Vignere Cipher------------"
ct = Cipher.vignere(pt,str(k2),mode='encrypt')
print 'Plain Text: ', Cipher.vignere(ct,str(k2),mode='decrypt')
print 'Cipher Text: ', ct
