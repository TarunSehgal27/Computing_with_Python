'''text=input("Enter the line of text : " )
distance=int(input("Enter the distance value : "))
encrypt=""
text=text.lower()
for ch in text:
    ch_order=ord(ch)
    ch_index=ord(ch)-ord("a")
    new_index=(ch_index+distance)%26
    new_value=new_index + ord("a")
    new_ch=chr(new_value)
    encrypt+= new_ch
    if ch==" ":
        encrypt+=ch
print("Plain Text : ",text)
print("Encrypted Text : ",encrypt)
'''

'''import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename='indians-diabetes.data.csv'
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=pd.read_csv (filename, names=hnames)
array=dataframe.values
X=array [:, 0:8]
Y=array [:, 8]
model=LogisticRegression ()
num_folds=10
kfold=Kfold (n_splits=num_folds)
results=cross_val_score(model,X,Y,cv=kfold)
print('results:',results)
print("Accuracy:%.2f%%"%(results.mean()*100.0))
print("Std.Deviation=%.2f"%(results.std()*100.0))
'''
'''import random
import matplotlib. pyplot as plt
account=0
x=[]
y=[]
for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    print("Your bet",bet)
    print("Lucky draw::",lucky_draw)
    if bet==lucky_draw:
        account=account+900-100
    else:
        account=account-100
    y.append(account)
print("Amount in account",account)
plt.plot(x,y)
plt.show()
'''
import speech_recognition  as sr
audio_file=("test_file.wav")
r=sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio=r.record(source)
    try:
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError:
        print("Result not found from Google Speech Recognition")
        
'''import string
from random import *
characters = string.ascii_letters + string.digits
password =  "".join(choice(characters) for x in range(randint(10, 16)))
print(password)
'''


'''class GroceryList(dict):

    def __init__(self):
    	self = {}

    def addToList(self, item, price):
            self.update({item:price})

    def Total(self):
		total = 0
		for items in self:
			total += (self[items])*.07 + (self[items])
		return total

    def Subtotal(self):
		subtotal = 0
		for items in self:
			subtotal += self[items]
		return subtotal

    def returnList(self):
		return self

Test list should return:
Total = 10.70
Subtotal = 10
returnList = {"milk":4, "eggs":3, "kombucha":3}
List1 = GroceryList()

List1.addToList("milk",4)
List1.addToList("eggs", 3)
List1.addToList("kombucha", 3)


print List1.Total()
print List1.Subtotal()
print List1.returnList()

#*****************************************************
print
#*****************************************************


List2 = GroceryList()

List2.addToList('cheese', 7.49)
List2.addToList('wine', 25.36)
List2.addToList('steak', 17.64)

print List2.Total()
print List2.Subtotal()
print List2.returnList()
'''