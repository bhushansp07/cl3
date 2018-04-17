import random
import hashlib

print "Enter p and q such that both are prime and satisfy the condition (p-1)%q = 0"
while True:
    p = input()
    q = input()
    if (p-1)%q == 0:
        break

def get_g(p,q,h):
	for g in range(1,p):
		if pow(g,q)%p!=1 or g!=pow(h,((p-1)/q))%p:
			g=g+1
		else:
			return g
	return -1

msg = raw_input("Enter message")
m = hashlib.sha1()
m.update(msg)
print m.hexdigest()
h = int(str(m.hexdigest()),16)
print "h: ",h
g = get_g(p,q,h)
print g

while True:
    x = int(input("Enter x such that 1<x<q"))
    if x > 1 and x < q:
        break


print x
y=pow(g,x)%p
print "Public Key",[p,q,g,y]
print "Private Key",[p,q,g,x]

while True:
    k = random.randint(1,q)
    r = (pow(g,k)%p)%q
    i=0        
    while True:
        if(k*i)%q ==1:
            break
        i+=1
    s = i*(h+r*x)%q
    if s!=0 and r!=0:
        break
        
print "Digital Signature",[r,s]

w = 0
while True:
    if(s*w)%q == 1:
        break
    w+=1
u1 = (h*w)%q
u2 = (r*w)%q
v = ((pow(g,u1) * pow(y,u2))%p)%q

if v == r:
    print "Signature Verified"
else:
    print"Signature Invalid"
    

        
