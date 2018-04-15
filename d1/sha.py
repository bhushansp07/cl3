# Author: https://en.wikipedia.org/wiki/SHA-1
def chunks(bits,chunkSize) :
	return [bits[i:i+chunkSize] for i in range(0, len(bits), chunkSize)]

def rotateLeft(bits,positions) :
	return ((bits << positions) | (bits >> (32 - positions))) & 0xffffffff 

def shaDigest(data) :
	h0 = 0x67452301
	h1 = 0xEFCDAB89
	h2 = 0x98BADCFE 
	h3 = 0x10325476 
	h4 = 0xC3D2E1F0 # end pairings

	bitFormOfData = ""
	for c in range(len(data)) :
		bitFormOfData = bitFormOfData + '{0:08b}'.format(ord(data[c]))

	originalBitFormOfData = bitFormOfData
	bitFormOfData = bitFormOfData + "1"
	while ((len(bitFormOfData) % 512) != 448) :
		bitFormOfData = bitFormOfData + "0"

	bitFormOfData = bitFormOfData + '{0:064b}'.format(len(originalBitFormOfData))

	for c in chunks(bitFormOfData , 512) : 
		words = chunks(c,32) 
		w = [0] * 80

		for n in range(0,16) :
			w[n] = int(words[n] , 2)

		for i in range(16,80) :
			w[i] = rotateLeft((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1) # ^ is for XOR

		a = h0
		b = h1
		c = h2
		d = h3
		e = h4

		for i in range(0,80) :
			if (0 <= i <= 19) :
				f = b ^ c ^ d   
				k = 0x5A827999  
			elif (20 <= i <= 39) :
				f = b ^ c ^ d  
				k = 0x6ED9EBA1 
			elif (40 <= i <= 59) :
				f = b ^ c ^ d   
				k = 0x8F1BBCDC  
			elif (60 <= i <= 79) :
				f = b ^ c ^ d   
				k = 0xCA62C1D6  

			temp = rotateLeft(a, 5) + f + e + k + w[i] & 0xffffffff
			e = d
			d = c
			c = rotateLeft(b , 30)
			b = a
			a = temp

		h0 = h0 + a
		h1 = h1 + b
		h2 = h2 + c
		h3 = h3 + d
		h4 = h4 + e

	return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

if __name__ == "__main__":
	print("Enter a message : ")
	message = raw_input()
	print("")
	digest = shaDigest(message)
	print("It's SHA-1 digest is -> ")
	print(digest)
	print("")
