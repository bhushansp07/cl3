#include<bits/stdc++.h>
using namespace std;
class encrpyt
{
	void output(string);
	void cipher(string, int);
	void cipher(string, string);	
	public : 
	void getinput();
	
};

void encrpyt :: getinput()
{
	cout<<"1 to for Ceasar Cipher\t2 for Vignere Cipher"<<endl;
	int ch;
	cin>>ch;
	cout<<"Enter the plain text"<<endl;
	string text;
	cin>>text;
	
	if (ch == 1)
	{
		cout<<"Enter the key between 0 to 25"<<endl;
		int key;
		cin>>key;
		cipher(text,key);
	}
	else if (ch ==2)
	{
		cout<<"Enter the key"<<endl;
		string key;
		cin>>key;
		cipher(text,key);
	}
}

void encrpyt :: cipher(string text, int key)
{
	string result = "";

	for (int i=0;i<text.length();i++)
    	{
        	if (isupper(text[i]))
   			result += (text[i]+key-'A')%26 +'A';
       		else
   		     	result += (text[i]+key-'a')%26 +'a';
   	}
    	output(result);
}

void encrpyt :: cipher (string text, string key)
{
	int x = text.length();

	for(int i=0 ; ;i++)
	{	
		if(x == i)
			i = 0;
		if(key.size()== text.length())
			break;
		key += key[i];
	}
	
	string result = "";

	for (int i = 0 ; i<text.length(); i++)
	{	
		if (isupper(text[i]))
			result  += (text[i]+key[i]-(2*'A'))%26+'A';
		else 
			result  += (text[i]+key[i]-(2*'a'))%26+'a';
	}
	output(result);
}

void encrpyt :: output(string result)
{
	cout<<"The encrpyted text is  "<<result<<endl;
}

int main()
{
	encrpyt e;
	e.getinput();
	return 0;
}
