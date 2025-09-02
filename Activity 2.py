moneyamount = int(input("Please enter an amount to withdraw:"))
note1 = moneyamount//100
note2 = (moneyamount%100)//50
note3 = ((moneyamount%100)%50)//20
note4 = (((moneyamount%100)%50)%20)//10
pound = ((((moneyamount%100)%50)%20)%10)//1
print("note1 is 100 pounds", note1)
print("note2 is 50 pounds", note2)
print("note3 is £20", note2)
print("note4 is £10", note3)
print("pound is 1 pound", pound)

