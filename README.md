# ATM_ITI
python code and QT5 Designer for ATM Project with  multi-users and some services like Withdraw - Fawry services  - Password change and amount inquiry


and this some comments from the project for description:


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
