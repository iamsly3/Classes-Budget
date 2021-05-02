name = input('What is your name?  \n')
allowedUsers = ['Sly', 'Mike', 'Love']
allowedPassword = ['passwordSly', 'passwordMike', 'passwordLove']
import datetime
now = datetime.datetime.today()
availableBalance = 100

if(name in allowedUsers):
    password = input("Your Password?  \n")
    userId = allowedUsers.index(name)
    allowedWithdrawal = input
    allowedDeposit = input
    allowedComplaint = input
    
    if(password == allowedPassword[userId]):
       print("Welcome %s" % name) 
       print('The Date and Time is %s' % now)

       print('These are the avaible option:')
       print('1. Withdrawal')
       print('2. Cash Deposit')
       print('3. Complaint')

       selectionOption = int(input('Please select an option: \n')) 
       print(selectionOption == 1)
       
       if(selectionOption == 1):
           
           withdrawalAmount = int(input("How much would you like to withdraw? \n"))
           balance = availableBalance - withdrawalAmount
           print("take your cash $ %d" % withdrawalAmount)
           print("Available Balance $ %d" % balance)

       if(selectionOption == 2):
            depositAmount = int(input("How  much would you like to Deposit? \n"))
            balance = availableBalance + depositAmount
            print('Deposit Amount $ %d' % depositAmount)
            print("Available Balance $ %d" % balance)
            
       elif(selectionOption == 3):
            allowedComplaint = input("What will you like to report? \n")
            print('Thanks for contacting us, someone will get bact to you soon')
       else:
            print('Invalid Option selection, please try again')   
    else:
        print('Password Incorrect, please try again')
else:
    print('Name not found, please try again')       






