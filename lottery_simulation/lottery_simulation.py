import random
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

Output---> Amount :  1300 (Figure_1.png)
           Amount : -5000 (Figure_2.png)
