def Pin_change(i):
    k = int(input('enter your pin'))
    if k != pin[i]:
        print('you entred pin is wrong :(')
        print("please try again ")
        print("******************************")
        print('thanks for choseing ur bank')
        print("******************************")
    else:
        while(1):
            p = int(input('enter a new pin :'))
            m = int(input('Renter the pin :'))
            if p != m:
                print("pin are not macthing ")
                print('please try again ')
            else:
                pin[i] = p
                print("******************************")
                print('sucessfully the pin is change ')
                print("******************************")
                break
def Balance_enqurie(i):
    p = int(input("enter ur pin:"))
    if p != pin[i]:
        print('you entred pin is wrong :(')
        print("please try again ")
        print("******************************")
        print('thanks for choseing ur bank')
        print("******************************")
    else:
        print(balance[i])
        print("******************************")
        print('thanks for choseing ur bank')
        print("******************************")
def Withdraw(i):
    p = int(input('enter your pin:'))
    if p != pin[i]:
        print("you entred a wrong pin ")
        print('please try again:(')
    else:
        k = int(input('enter amount:'))
        if k >= balance[i]:
            print('******************************')
            print('insuffucient balance')
            print('******************************')
        else:
            balance[i] = balance[i] - k
            print('please collect your money :')
            print('******************************')
            print("withdraw process is sucessfull")
            print('******************************')
def Deposit(i):
    p = int(input("enter your pin:"))
    if  p != pin[i]:
        print("entered pin is wrong u have only 2 chances")
        flag = 0
        p = int(input("enter your pin:"))
        if p != pin[i]:
            print("entered pin is wrong u have only 1chances")
            flag = 0
            p = int(input("enter your pin:"))
            if p != pin[i]:
                print("chances are over")
                flag = 0
            else:
                flag = 1
        else:
            flag =1
    else:
        flag =1

    if flag == 0:
        print("Try again :(")
    else:
        k = int(input('enter amount :'))
        balance[i] = balance[i] + k
        print('******************************')
        print("Deposit process is sucessfull")
        print('******************************')
def Atm(i):
    passcode = str(input('enter a vaild password: '))
    if passcode != password[i]:
        print("enter password is wrong u have only 2 chances")
        flag = 0
        passcode = str(input('enter a vaild password: '))
        if passcode != password[i]:
            print("enter password is wrong u have only 1 chances")
            flag = 0
            passcode = str(input('enter a vaild password: '))
            if passcode != password[i]:
                print("The chances are over :(")
                flag = 0
            else:
             flag = 1
        else:
            flag=1
    else:
       flag=1
    if flag == 0:
        print('The is blocked :Try again :)')
    else:
        print('1.Deposit')
        print('2.Withdraw')
        print('3.Balance enqurie')
        print('4.pin change')

    choice = int(input('enter a vaild choice:'))
    while(1):
        if choice >= 5:
            print("invaild choice try again:")
            choice = int(input('enter a vaild choice:'))
        else:
           if choice == 1:
               Deposit(i)
           elif choice == 2:
               Withdraw(i)
           elif choice == 3:
              Balance_enqurie(i)
           elif choice == 4:
               Pin_change(i)
           break
user_name = ['gopi','mani','shanker']
password = ['gopi@123','mani@123','shanker@123']
balance = [10000,2500,3210]
pin = [1234,1432,2004]
name = str(input('enter a vaild user name: '))
if name not in user_name:
    print('invaild user name')
else:
    i = user_name.index(name)
    Atm(i)