class Credentials:
    """
    Class that generates new instances of credentials
    """

    Credentials_list = []

    def _init_(self,accountName,siteName,username,email,password):

      #docstring removed for simplicity
    
        self.accountName = accountName
        self.siteName = siteName
        self.username = username
        self.email = email
        self.password = password


    
   
       