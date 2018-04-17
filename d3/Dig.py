import sys 
import random
import  hashlib

def get_g(p,q,h):
	for g in range (1,p):
		if  (pow(g,q)%p != 1 and g != pow(h,(p-1/q))%p):
			g = g+1
		else:
			return g
	return -1

q = int(raw_input("Enter the value of q such that q is prime: "))
p = int(raw_input("Enter the value p of p such that p-1 is divisible by q and p is prime: "))
message = raw_input("Enter the message: ")

#converting the message in to message digest via sha1 
m = hashlib.sha1()
m.update(message)
print (m.hexdigest())
h = int(str(m.hexdigest()),16)
print ("The hash value of the message is "+str(h))

#compute the value of g
g = get_g(p,q,h)

#get privatekey and pulbic key
private = int(raw_input("Enter the private key between 1 and q: "))
public = pow(g,private)%p

print("The private key is "+str(private))
print("The pulbic key is "+str(public))

#signing the message
k = random.randint(1,q)
r = pow(g,k)%p
i = 0
while True:
 	if ((k*i)%q == 1):
 		break
 	i = i+1
s = i*(h+r*private)

print("The digital signature (r,s) is " + str(r) +","+ str(s))

# computing the value of v 
w = 0
while True:
	if((s*w)%q == 1):
		break
	w = w+1

u1 = pow(h,w)%q
u2 = pow(r,w)%q

v = ((pow(g,u1)*pow (public,u2))%p)%q
print(v)
print (r)
if (v != r):
	print ("Verification not successful")
print("Verification successful")
