class Session:
    def __init__(self,func):
        self.function = func

    def __call__(self,*args):
        """1. This is Created By Mitesh Amin
2. This is Developed for Check user in Session or Not
3. You want Use this Deco Following This Step
    1. Import Module
        Ex. from deco import Session
    2. Put this Decorator Above a Function
        Ex. @Session
            def user_check(): """
        if (args[0] == True):
            result = self.function(*args)
            print("Welcome Back The WebSite.")
            return result
        else:
            print("***************************************You Are New User So First SignUp***************************************")
            user_name = input("Enter Your Username:- ")
            user_pass = input("Enter Your New Password:- ")
            print("*************************************** Login ***************************************")
            login_name = input("Enter Your Username:- ")
            login_pass = input("Enter Your Password:- ")
            if user_name == login_name and user_pass == login_pass:
                result = self.function(*args)
                return result
            else:
                print("Sorry, Your Username and Password Don't Match!!")
                print("Please Try Again Later!!")

