#Coded by Muhd Thahir
#lab work 1
#Basic Information
print("Currency Conversion Program")
print("Exchange Rates :")
print("USD - US Dollar : 0.25")
print("USD - US Dollar : 0.21")
print("USD - US Dollar : 0.18")
#User Choice
print("Choose the target currency")
print("1. USD - US Dollar")
print("2. EUR - Euro")
print("3. GBP - British Pound")
#input section for user
choice = float(input("Enter your choice :"))
#user input amount
exc_amount = float(input("Enter the amount in Malaysian Ringgit (MYR) :"))
#statement
USD = 0.25
EUR = 0.21
GBP = 0.18
#calculation(choice * exc_amount)
if choice == 1 :
    exc_rate = (exc_amount * USD)
    print("Equivalent amount in USD :",exc_rate)

elif choice == 2 :
    exc_rate = (exc_amount * EUR)
    print("Equivalent amount in EUR :", exc_rate)

elif choice == 3 :
    exc_rate = (exc_amount * GBP)
    print("Equivalent amount in GBP : ", exc_rate)

else:print("The input you entered is wrong !!! Please choose from the option given")





