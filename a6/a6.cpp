#include<bits/stdc++.h>
using namespace std;
class encrpyt
{
	public : 
	void getinput();
	void output(string);
	void ceasar_cipher(string, int);
	void vignere_cipher(string, string);
};

void encrpyt :: getinput()
{
	cout<<"1 to for Ceasar Cipher 		2 for Vignere Cipher"<<endl;
	int ch;
	cin>>ch;
	if (ch == 1)
	{
		cout<<"Enter the plain text"<<endl;
		string text;
		cin>>text;
		cout<<"Enter the key between 0 to 25"<<endl;
		int key;
		cin>>key;
		ceasar_cipher(text,key);
	}
	else
	{
		cout<<"Enter the plain text" <<endl;
		string text;
		cin>>text;
		cout<<"Enter the key"<<endl;
		string key;
		cin>>key;
		vignere_cipher(text,key);

	}
}

void encrpyt :: ceasar_cipher(string text, int key)
{
	string result = "";

	for (int i=0;i<text.length();i++)
    	{
        	if (isupper(text[i]))
   			result += char(int(text[i]+key-'A')%26 +'A');
       		else
   		     	result += char(int(text[i]+key-'a')%26 +'a');
   	}
    	output(result);
}

void encrpyt :: vignere_cipher (string text, string key)
{
	int x = text.length();

	for(int i=0 ; ;i++)
	{	
		if(x == i)
			i = 0;
		if(key.size()== text.length())
			break;
		key.push_back(key[i]);
	}
	
	string cipher_text = "";

	for (int i = 0 ; i<text.length(); i++)
	{
		int c;		
		if (isupper(text[i]))
			c = (text[i]+key[i]-(2*'A'))%26+'A';
		else 
			c = (text[i]+key[i]-(2*'a'))%26+'a';
			cout<<c;
		cipher_text.push_back(c);
	}
	output(cipher_text);
}

void encrpyt :: output(string pass)
{
	cout<<"The encrpyted text is  "<<pass<<endl;
}

int main()
{
	encrpyt e;
	e.getinput();
	return 0;
}
