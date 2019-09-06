from user import User
from credentials import Credentials

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






