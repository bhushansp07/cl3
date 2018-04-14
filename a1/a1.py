import unittest,os
class BinSearch:
	arr=[]
	def read(self,filename):
		desc=open(filename,'r')
		input_arr=[]
		for i in desc:
			input_arr.append(int(i))
		return (input_arr)
	

	def search(self,lst,key,start,end):
		if(start<=end):
			mid=(end+start)/2
			if(key==lst[mid]):
				print"\nValue found at index:",mid
				return mid
			elif(key<lst[mid]):
				return self.search(lst,key,start,mid-1)
			elif(key>lst[mid]):
				return self.search(lst,key,mid+1,end)
		else:
			print "\nValue Not Found!!\n"

b1= BinSearch()
b1.arr=b1.read("input.txt")
	
print "Input array:\n"
print (b1.arr)

print "\n---------------\ntesting\n---------------\n"
b1.arr.sort()

print "Sorted array:\n "
print (b1.arr)

key=int(input("\nEnter the element to be searched: "))
ind=b1.search(b1.arr,key,0,len(b1.arr)-1)

class Test(unittest.TestCase):
	def test_postive(self):
		self.assertEqual(b1.search([0,1,2,3,4,5],1,0,5),1)
			
	def test_negative(self):
		self.assertEqual(b1.search([0,1,2,3,4,5],10,0,5),None)



print("\n------------\nUnit testing\n------------\n")
unittest.main()
