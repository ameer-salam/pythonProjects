import os
import threading
import time 
import cli_v2_userDB_mananger as db_manage_prg

#variables
users_db="users.db"

def enter_user_mail():  
    user_mail=str(input("Enter user mail     : "))
    return user_mail

def enter_validate_userName(): #validate user name
    user_name=str(input("Enter the user name : "))
    length = int(len(user_name))
    lower=user_name.islower()
    upper=user_name.isupper()
    if(length<4):
        print("User Name must be at leat four characters longI\n")
        enter_validate_userName()
    return user_name
    
def create_new_user_screen():
    print("\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n----------------------------------------------------------------------------\033[1m\033[7mCREATE NEW USER\033[0m---------------------------------------------------------------------------\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def create_new_user():
    os.system("cls")
    top_screen()
    create_new_user_screen()
    user_name=enter_validate_userName()
    user_mail=enter_user_mail()
    #print(f"The user name is : {user_name}\nThe user mail is : {user_mail}")
    db_manage_prg.User_list.add_new_user(user_name, user_mail)
    #db_manage_prg.printAll()

def no_user_screen():
    print("\n\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n-----------------------------------------------------------------------------\033[1m\033[7mNO USER EXISTS\033[0m---------------------------------------------------------------------------\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n--------------     \033[01mOptions\033[0m                   -----------------------     \033[01mSelect the Following\033[0m     --------------------------------------------------------------------\n")
    print("a.-----       \033[01mCreate a new User\033[0m         -----------------------------------      1      ------------------------------------------------------------------------------")
    print("b.-----       \033[01mFind Users Database\033[0m       -----------------------------------      2      ------------------------------------------------------------------------------")
    print("c.-----       \033[01mAbout this Application\033[0m    -----------------------------------      3      ------------------------------------------------------------------------------")
    print("d.-----       \033[01mDocumentation\033[0m             -----------------------------------      4      ------------------------------------------------------------------------------")
    print("e.-----       \033[01mApplication Page\033[0m          -----------------------------------      5      ------------------------------------------------------------------------------")
    print("f.-----       \033[01mExit Application\033[0m          -----------------------------------      6      ------------------------------------------------------------------------------")

def top_screen():
    print("""----------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------//========\\\\                                     //\\\\                                         ------------
------------------------------------------------------------||        ||                                    //   \\\\                                       ------------
------------------------------------------------------------||        || ||====|| ||====== ||\\\\    ||      //     \\\\      ||      || ========== ||      ||------------
------------------------------------------------------------||        || ||    || ||       ||  \\\\  ||     //       \\\\     ||      ||     ||     ||      ||------------
------------------------------------------------------------||        || ||    || ||====   ||   \\\\ ||    //=========\\\\    ||      ||     ||     ||      ||------------
------------------------------------------------------------||        || ||====|| ||       ||    \\\\||   //           \\\\   ||      ||     ||     ||======||------------
------------------------------------------------------------||        || ||       ||       ||     \\\\|  //             \\\\  ||      ||     ||     ||      ||------------
------------------------------------------------------------\\\\========// ||       ||====== ||      \\\\ //               \\\\ ||======||     ||     ||      ||------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------- by - Ameer Salam ------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    
def find_user():
    if db_manage_prg.check_user_exists() == False: ##no user
        #db_manage_prg.connect_to_users_db()
        no_user_screen()
        choice_1=int(input("\n\033[01mEnter Your Choice (1-6) : \033[0m"))
        if(choice_1 == 1): #create a new user  
            users=create_new_user()
        if(choice_1 == 2): #find existing user database
            path=input("Enter the path!")
        #if(choice_1 == 3): #About page

        #if(choice_1 == 4): #documentation readme file

        #if(choice_1 == 5): #link to application page

        if(choice_1 == 6):
            os.system("cls")
            os.system("exit")
    else:
        print("Yenlaa sisya!")
        



def main():
    os.system('cls')
    print("\n")
    top_screen()
    #user_counts=
    find_user()


if __name__ == "__main__":
    main()