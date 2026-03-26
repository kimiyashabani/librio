class User:
    def __init__(self,name, family_name, username, password):
        self.name = name
        self.family_name = family_name
        self.username = username
        self.password = password
        self.favorites = []
        self.wish_list = []
        self.finished_books = []
    
    @property
    def name(self):
        return self.name
    
    @property
    def family_name(self):
        return self.family_name
    
    @property
    def username(self):
        return self.username
    
    @property
    def password(self):
        return self.password
    
    def add_to_favorites(self, book_id):
        pass
    
    