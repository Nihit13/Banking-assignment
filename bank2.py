#This is a code developed by NIHIT
# line 7 to line 10 contains bank details of 4 bank holders
# While running this code check the details of the four bankholders
#The first item in the list contains the name
#The second item contains the account number
#The third  item contain the password of the user
user1 = ["rakesh", "2345", "rakesh", " 2546474", "0"]
user2 = ["mukesh", "7564", "mukesh", "873464", "0"]
user3 = ["lokesh", "9807", "lokesh", "345273", "0"]
user4 = ["raju", "5678", "raju", "879065", "0"]
username = ["", "", "", "", ""]


def bank():
    accnum = int( input( "Please enter your account number: " ) )

    if accnum == 2345:
        username = ["Rakesh", "2345", "rakesh", " 2546474", "0"]
    elif accnum == 7564:
        username = ["Mukesh", "7564", "mukesh", "873464", "0"]
    elif accnum == 9807:
        username = ["Lokesh", "9807", "lokesh", "345273", "0"]
    elif accnum == 5678:
        username = ["Raju", "5678", "raju", "879065", "0"]

    accpass = str( input( "Enter your password " ) )
    if accpass == str( username[2] ):
        print( "Welcome " )
        option = str(
            input( "What type of transaction you want to perform:Balance Inquiry,Cash Deposit,Cash Withdrawal,Loan" ) )
        if option == "Balance Inquiry":            # Note that  you have to enter exact option given by the program like :- Cash Deposit not cash deposit or CASH DEPOSIT or else it will give an error
            print("You have the balance of rupees " + username[3] )
        elif option == "Cash Deposit":
            deposit = str( input( "Enter amount to deposit cash " ) )
            username[3] = int( username[3] ) + int( deposit )
            print( "Your balance is " + str(username[3]) )
        elif option == "Cash Withdrawal":
            cash_withdrawal = int( input( "Enter cash to withdraw " ) )
            username[3] = int( username[3] ) - cash_withdrawal
            print("Money has been withdrawed")
            print( "Your balance is " + str( username[3] ) )
        elif option == "Loan":
            maxloan = int( 0.5 * int( username[3] ) )
            print( "You can have maximum loan of " + str( maxloan ))
            loanamount = int( input( "Enter loan amount " ) )
            if loanamount > maxloan:
                print( "Invalid loan amount" )
            else:

                username[3] = int( username[3] ) + int( loanamount )
                print( " Your balance is " + str( username[3] ) )
        else:
            print( "invaild option" )


bank()