import requests #type: ignore
import string #type: ignore

url = "https://raw.githubusercontent.com/spyguessgame-boop/own_dataset/refs/heads/main/data.txt"

response = requests.get(url)
response.raise_for_status()

text_data = response.text

text_data = text_data[:1000]
print(text_data)


#removing punctuation before tokenization

text=""
for ch in text_data:
    if(ch not in string.punctuation):
        text+=ch
print(text) #printing after removing punctuation 

#tokeniztion 
tokens=text.split(" ")
print(tokens)

#calculate number of tokens
print(len(tokens))

#unique tokens
s=set(tokens) 

#calculating number of individual tokens
d={}
for i in s:
    d[i]=tokens.count(i)

print(d)

#maximum occuring string
m = max(d.values())

for i in d:
    if d[i] == m:
        print(i)


