class User:
    """
    Class that generates new instances of users
    """
    
    user_list = []

    def __init__(self,username,email,password):

      #docstring removed for simplicity

        self.username = username
        self.email= email
        self.password= password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
    
    
       