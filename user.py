class User:
    """
    Class that generates new instances of users
    """
    
    user_list = []

    def _init_(self,username,email,password):

      #docstring removed for simplicity

        self.username = username
        self.email= email
        self.password= password
    
    
       