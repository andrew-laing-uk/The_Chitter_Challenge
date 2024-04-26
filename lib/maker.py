class Maker():
    def __init__(self, id, full_name, username, user_email, user_password):
        self.id = id
        self.full_name = full_name
        self.username = username
        self.user_email = user_email
        self.user_password = user_password
        self.logged_in = False

    def __repr__(self):
        return f"Maker({self.id}, {self.full_name}, {self.username}, {self.user_email}, {self.user_password})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def is_valid(self):
        if self.full_name == None or self.full_name == "":
            return False
        if self.username == None or self.username == "":
            return False
        if self.user_email == None or self.user_email == "":
            return False
        if self.user_password == None or self.user_password == "":
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.full_name == None or self.full_name == "":
            errors.append("Full Name can't be blank")
        if self.username == None or self.username == "":
            errors.append("Username can't be blank")
        if self.user_email == None or self.user_email == "":
            errors.append("Email can't be blank")
        if self.user_password == None or self.user_password == "":
            errors.append("Password can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)   
        
    def log_in(self):
        self.logged_in = True
           
    def log_out(self):
        self.logged_in = False     