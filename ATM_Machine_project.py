#ATM Machine Project In Python

print("\nWelcome to Personal Bank\n\n Please Insert your card....")

#card pin and card balance
password=2222
balance =10000

choice=0

pin = int(input("Enter your four digit pin number: "))

#show menu and use while loop
if pin==password:
    while(choice !=4):
        print("\n\n____Menu____")
        print("1 == balance")
        print("2 == deposite")
        print("3 == withdraw")
        print("4 == cancel\n")

        choice = int(input("\nEnter your option: "))

        if(choice==1):
            print("Balance = Rs", balance)
        elif(choice ==2):
            deposite=int(input("Enter your deposite: Rs "))
            balance+=deposite
            print("\ndesposite amount: Rs",deposite)
            print("Total Balance = Rs",balance)
        elif(choice==3):
            withdraw=int(input("Enter the amount to withdraw: "))
            balance -=withdraw
            print("\nwithdraw amount: Rs",withdraw)
            print("total balance = Rs",balance)

        elif(choice==4):
            print("\nthanks")
else:
    print(" Wrong Pin Number!! try agian...! ")