class Credentials:
    """
    Class that generates new instances of credentials
    """

    Credentials_list = []

    def __init__(self,accountName,siteName,username,email,password):

      #docstring removed for simplicity
    
        self.accountName = accountName
        self.siteName = siteName
        self.username = username
        self.email = email
        self.password = password

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into Credentials_list
        '''

        Credentials.Credentials_list.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the Credentials_list
        '''

        Credentials.Credentials_list.remove(self)

    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in an email and returns the credentials that matches that email.

        Args:
            email: email address to search for 
        Returns:
            Credentials of person that matches the email.
        '''

        for credentials in cls.Credentials_list:
            if credentials.email == email:
                return credentials


    
   
       