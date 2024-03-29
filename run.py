#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
import random
import string
import pyperclip

def create_user(username,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,email,password)
    return new_user

def create_credentials(accountName,siteName,username,email,password):
    '''
    Function to create the new credentials
    '''
    new_credentials = Credentials(accountName,siteName,username,email,password)
    return new_credentials


def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def save_credential(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def del_user(user):
    '''
    Function to delete an user
    '''
    user.delete_user()

def del_credentials(credentials):
    '''
    Function to delete the credentials
    '''
    credentials.delete_credentials()
    return True


def find_user(email):
    '''
    Function that finds an user by email and returns the user
    '''
    return User.find_by_email(email)

def find_credentials(email):
    '''
    Function that finds the credentials by email and returns the credentials
    '''
    return Credentials.find_by_email(email)


def check_existing_users(email):
    '''
    Function that check if an user exists with that email and return a Boolean
    '''
    return User.user_exists(email)

def check_existing_credentials(email):
    '''
    Function that check if the credentials exist with that email and return a Boolean
    '''
    return Credentials.credentials_exists(email)


def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def display_credential():
    '''
    Function that returns all the saved credential
    '''
    return Credentials.display_credential()


def copy_email(myEmail):
    '''
    '''
    myEmail.copy_credentials(myEmail)

def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def main():
    
    print("Welcome to Password Locker Application! what is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
        print("Use these short codes: ct -create a new user account, lg - login ad - add the credentials , dy - display credentials, cp - copy the credentials, dl - delete credentials, ex - exit the password locker")
                        
        short_code = input().lower()
                        
        if short_code == 'ct':
            
            
            print("New User")
            print("-"*10)
                            
            print("username ....")
            user_name = input()
            print("email ...")
            e_mail = input()
                            
            print("password ...")
            password = input()
                            
            save_users(create_user(user_name,e_mail,password)) #create and save new user.
            print('\n')
            print(f"New User {user_name} {e_mail} created and saved")
            print('\n')


        elif short_code == 'lg':
            print("LOG IN")
            print('-'*10)
            print('\n')
            print("please enter the created account")
            email = input()

            if check_existing_users(email):
                searched_email = find_user(email)
                print(f"{searched_email.username} {searched_email.email}")
                print('-'*30)
                print('\n')
                print('Thank you for logging in')

            else:
                print('the email does not exist')

        elif short_code == 'ad':
            print("New Credentials")
            print("-"*10)
                            
            print("accountName ...")
            account_Name = input()
                            
            print("siteName ...")
            site_Name = input()
                            
            print("username ...")
            user_name = input()
                            
            print("email ...")
            e_mail = input()
                            
            # print("password ...")
            
            print("use this short_code: gn - if you want system to generate password for you, or use cc - to create your own password")
            # password = input()
            choice = input().lower()
            if choice == 'gn':
                print("Random password generated for you")
                print ("First Random String is ", randomString(8) )
                print ("second Random String is ", randomString(8) )

                save_credential(create_credentials(account_Name,site_Name,user_name,e_mail,password)) #create and save new credentials.
                print('\n')
                print(f"New Credentials {account_Name} {site_Name} {user_name} {e_mail} created and saved")
                print('\n')
            
                         
            else :
                new_password = input()
                save_credential(create_credentials(account_Name,site_Name,user_name,e_mail,new_password)) #create and save new credentials.
                print('\n')
                print(f"New Credentials {account_Name} {site_Name} {user_name} {e_mail} created and saved")
                print('\n')
                
        
        elif short_code == 'dy':
            
            if display_credential():
                print("Here there is a list of all your credentials")
                print('\n')
                
                for credentials in display_credential():
                    print(f"{credentials.accountName} {credentials.siteName} {credentials.username} {credentials.email} {credentials.password}")
                    print('\n')

        elif short_code == 'cp':
            print ('Copy the credentials')
            print('-'*10)
            print('\n')
            print('enter email of the credentials you want to copy')
            searched_email = input()
            print(check_existing_credentials(searched_email))

            if check_existing_credentials(searched_email):
                searche_email = find_credentials(searched_email)
                print(f"{searche_email.accountName} {searche_email.siteName} {searche_email.username}")
                print('-'*10)
                searche_email.copy_credentials(searched_email)
                print('credentials copied')
                print('\n')

        elif short_code == 'dl':
        
            for credentials in display_credential():
                
            
                if del_credentials(credentials):
                    print("account has successfully deleted")
    
        elif short_code == 'ex':
            print("Bye .......")
            break
        else:
            print("I didn`t get that. Please use the short codes")
                
                                
if __name__ == '__main__':
    

    main()                         

                            
                            
                            
                            


