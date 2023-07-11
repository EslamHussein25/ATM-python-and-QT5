'''

******************  Author: Eslam Hussein   ******************
******************       Version: 1         ******************
******************     Date: 1/7/2023       ******************
******************supervisor: Kareem Ashraf ******************
            App : ATM APP Using Python and QT5
	    
'''

from PyQt5.QtWidgets import *
import PyQt5.QtGui
import ATMPY 
import ATMPYCustomers
import withdraw
import ATMFawryPY
import sys
import time

from PyQt5.QtCore import QSize  

Customers = []
CustomerID = 0


#main class of the main project or main window and ny init we want to do in the first of the operation do it here 
#so this class like class of the main window in C# and init function is the constructor of the main to run any thing before init of the app 



#----------------------------------------------------- Classes------------------------------------------------------------#	
#here self insied the class like this in C# 

#this is the main class will start first and contain the user name and password 
class Appli(QDialog , ATMPY.Ui_Dialog):
			
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		self.btnOk.clicked.connect(Check_Customer_Click) 
		
#this the home page of the user class		
class Cust(QDialog , ATMPYCustomers.Ui_Dialog):
			
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		self.btnExit.clicked.connect(Exit_Click) 
		self.btnPassChnage.clicked.connect(Channge_Pass_Click) 
		self.btnPassOK.clicked.connect(Pass_OK_Click)  #lambda: Pass_OK_Click(CustomerID)
		self.btnFawry.clicked.connect(Fawry_Click)  
		self.btnBalance.clicked.connect(Balanc_Click)  
		self.btnWithdraw.clicked.connect(Withdraw_Click)  
		self.btnOkBlance.clicked.connect(Balanc_OK_Click)  
		self.boxPass.hide()
		self.bxbalanc.hide()

#this is the page of the withdraw proccess 
class With(QDialog , withdraw.Ui_digWithdraw):
			
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		self.btnOK.clicked.connect(OK_Click) 
		self.btnExit.clicked.connect(Exit_With_OK) 

#this the class of fawry services 
class Fawry(QDialog , ATMFawryPY.Ui_Dialog):
			
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		self.btnOK.clicked.connect(OK_Service_Click) 
		self.btnOrg.clicked.connect(lambda: Show_Servic_Click(1)) 
		self.btnEit.clicked.connect(lambda: Show_Servic_Click(2)) 
		self.btnVoda.clicked.connect(lambda: Show_Servic_Click(3)) 
		self.btnWE.clicked.connect(lambda: Show_Servic_Click(4)) 
		self.btnExit.clicked.connect(Exit_From_Service_Click) 
		self.txtamount.hide()  
		self.txtPhone.hide() 
		self.btnOK.hide() 
		self.lblOrgType.hide()

#this class contain the data of the user to change it any time or even conect with the dataabse no problem 
class Customer():

    def __init__(self, ID, NAME, PASS , BALANCE , Block):
        self.ID = ID
        self.NAME = NAME
        self.PASS = PASS
        self.BALANCE = BALANCE
        self.Block = Block


#----------------------------------------------------- funtion utality between classes ------------------------------------------------------------#	

# this the first function to load the data to the list in run time 
def LoadCustomers():
	
	Customer1 = Customer("215321701332", "Ahmed Abdelrazek Mohamed", "1783" , 3500166 , 0)
	Customer2 = Customer("203659302214", "Salma Mohamed Foaad", "1390" , 520001 , 0 )
	Customer3 = Customer("126355700193", "Adel Khaled Abdelrahman", "1214" , 111000 , 0 )
	Customer4 = Customer("201455998011", "Saeed Amin Elsawy", "2001" , 1200 , 0)
	Customer5 = Customer("201122369851", "Amir Salama Elgendy", "8935" , 178933 , 0 )
	Customer6 = Customer("201356788002", "Wael Mohamed khairy", "3420" , 55000 , 0)
	Customer7 = Customer("203366789564", "Mina Sameh Bishoy", "1179" , 18000 , 0)
	Customer8 = Customer("201236787812", "Omnia Ahmed Awad", "1430" , 180350 , 0)
	Customer9 = Customer("e", "e", "e" , 180350 , 0)

	Customers.append(Customer1)
	Customers.append(Customer2)
	Customers.append(Customer3)
	Customers.append(Customer4)
	Customers.append(Customer5)
	Customers.append(Customer6)
	Customers.append(Customer7)
	Customers.append(Customer8)
	Customers.append(Customer9)

# work with App class to check the user name ID and password of the user 	
def Check_Customer_Click():	

	#read all the data from text boxes 
	Name = qt_app.txtName.text()
	Pass = qt_app.txtPass.text()
	ID   = qt_app.txtID.text()
	Found = 0
	State = 0
	CustomerCouner = 0
	for c in Customers:
		if Name == c.NAME or ID == c.ID:
			Found = 1
			if c.Block == 3:
				qt_app.lblError.setText("your account has been diabled")
				break
			if Pass == c.PASS:
				qt_app.lblError.setText("Login Success")
				global CustomerID # to use this variable as global must be use global key word 
				CustomerID = int(CustomerCouner)
				CustomerData()				
				State = 1
				break
			else:
				qt_app.lblError.setText("Wrong Pass:Enter Password again")
				qt_app.txtPass.setText("")
				c.Block = c.Block  + 1
		CustomerCouner+=1
		
	if Found == 0:
		qt_app.lblError.setText("This Customer not exist")

# intermeiate funtion: this function to the show the user home page if his data is correct 
def CustomerData():
	qt_appCustomer.show()
	qt_appCustomer.lblCustomerName.setText(Customers[CustomerID].NAME)
	qt_app.hide()

#this function work with withdraw and fawry classes to check the data like balance and mount and so on 
def Check_Input_Data(classes):
	if classes.txtamount.text() == "":
		classes.lblError.setText("Please Enter True number first")
		return 1
	amount = int(classes.txtamount.text())
	if amount > 5000:
		classes.lblError.setText("The maximum allowed 5000 !")
	else:
		if amount % 100 == 0:
			global CustomerID 
			if Customers[CustomerID].BALANCE >= amount:
				classes.lblError.setText("OK: Wait to take your money")
				Customers[CustomerID].BALANCE -= amount				
				classes.lblError.setText("your current balane is:  " + str(Customers[CustomerID].BALANCE))	
			else:
				classes.lblError.setText("your balane not enough!")
		else:
			classes.lblError.setText("Enter the multiple of 100 only !")


#----------------------------------------------------- events Function for buttons  ------------------------------------------------------------#	

#--------------------------------------------  Events for Cust class to transefer between classes  ------------------------------------------------------------#	

def Exit_Click():
	qt_app.show()
	qt_appCustomer.hide()
	qt_app.txtName.setText("")
	qt_app.txtPass.setText("")
	qt_app.txtID.setText("")
	CustomerID = 0
	
def Channge_Pass_Click():
	if qt_appCustomer.boxPass.isVisible():
		qt_appCustomer.boxPass.hide()
	else :
		qt_appCustomer.boxPass.show()
	
def Pass_OK_Click():
	if len(qt_appCustomer.txtNewPass.text()) >= 4:
		if qt_appCustomer.txtNewPass.text() == qt_appCustomer.txtPassConfirm.text():
			global CustomerID
			MBox = QMessageBox() 
			MBox.setText(str(CustomerID))		
			MBox.exec_()
			Customers[CustomerID].PASS = qt_appCustomer.txtPassConfirm.text()
			qt_appCustomer.txtPassConfirm.setText("")
			qt_appCustomer.txtNewPass.setText("")
			qt_appCustomer.boxPass.hide()
		else :
			MBox = QMessageBox() 
			MBox.setText("Pass Not Matched: Try Again !")		
			MBox.exec_()
			qt_appCustomer.boxPass.hide()
	else:
		MBox = QMessageBox() 
		MBox.setText("Password mustn't be less than 4 charcters")		
		MBox.exec_()
	
def Balanc_OK_Click():
	qt_appCustomer.bxbalanc.hide()
		
def Withdraw_Click():
	qt_appCustomer.hide()
	qt_appWith.show()
	global CustomerID
	qt_appWith.lblCustomerName.setText(Customers[CustomerID].NAME)
	
def Balanc_Click():
	qt_appCustomer.bxbalanc.show()
	global CustomerID
	qt_appCustomer.lblBalance.setText(str(Customers[CustomerID].BALANCE)) 

def Fawry_Click():	
		qt_appCustomer.hide()
		qt_Fawry.show()
		global CustomerID
		qt_Fawry.lblCustomerName.setText(Customers[CustomerID].NAME)
	

#----------------------------------------------------- Events for With Class ------------------------------------------------------------#	

def OK_Click():
	Check_Input_Data(qt_appWith)
	
def Exit_With_OK():
		qt_appCustomer.show()
		qt_appWith.hide()


#----------------------------------------------------- Events for Fawry Class ------------------------------------------------------------#	

def Show_Servic_Click(num):
		qt_Fawry.txtamount.show()  
		qt_Fawry.txtPhone.show() 
		qt_Fawry.btnOK.show() 
		qt_Fawry.lblOrgType.show()
		if num == 1:
			qt_Fawry.lblOrgType.setText("Orange")
		elif num == 2:
			qt_Fawry.lblOrgType.setText("Etisalat")
		elif num == 3:
			qt_Fawry.lblOrgType.setText("Vodafone")
		elif num == 4:
			qt_Fawry.lblOrgType.setText("WE")

def Exit_From_Service_Click():
		qt_appCustomer.show()
		qt_Fawry.hide()

def OK_Service_Click():
	Check_Input_Data(qt_Fawry)


#----------------------------------------------------------- MAIN --------------------------------------------------------------------------#	

#from here we start in the app 		
LoadCustomers()
app = QApplication(sys.argv)	
# the next classes instance will be work and use it in all program for every class 
qt_app = Appli() 
qt_appCustomer = Cust()
qt_appWith = With()
qt_Fawry = Fawry()
qt_app.show()
#qt_app.hide()
app.exec_()




#----------------------------------------------------------- about and some desc for the app  --------------------------------------------------------------------------#	

# Notes 
'''
1- to use any element inside the design like text box , button , check box and any other thing 
so must be call it form the class of the design which we work with it here 
EX :
qt_app = Appli() # this is our main class of the design of the password screen 
so any element insided this screen will be call from this class 
like :
qt_app.lblError.setText("your account has been diabled") # here to call the lable from this class 
-----------------------------
2- after this comment --> #from here we start in the app 
the main app like C# main is started here must be write the main sequnce of the program and call the functions or the main functions and classes to  start 
-----------------------------
3- the event of the buttons wil be like callback function will make the normal function 
inside this function will put all the things we need to perform when the button click 
then use this call back inside the start of the code inside the class of this design to be aware with any clck event happened
self.btnOk.clicked.connect(Check_Customer_Click) 
we can use self . any insied the class but out side of the class we must use the name of the class to call any thing inside the class
we do like the first comment 
qt_app.lblError.setText("your account has been diabled") 
so here will do that 
qt_app.btnOk.clicked.connect(Check_Customer_Click) 
insted of self 
----------------------------


'''



