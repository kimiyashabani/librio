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
        if book_id not in self.favorites:
            self.favorites.append(book_id)
    
    def remove_from_favorites(self, book_id):
        if book_id in self.favorites:
            self.favorites.remove(book_id)

    def read_later(self, book_id):
        if book_id not in self.wish_list:
            self.wish_list.append(book_id)
    
    def remove_read_later(self, book_id):
        if book_id in self.wish_list:
            self.wish_list.remove(book_id)
    
    def finished_book(self, book_id):
        if book_id not in self.finished_books:
            self.finished_books.append(book_id)
    
    def delete_finished_book(self, book_id):
        if book_id in self.finished_books:
            self.finished_books.remove(book_id)
    
    def to_dict(self):
        return{
            "name": self.name,
            "family_name": self.family_name,
            "username": self.username,
            "password": self.password,
            "favorite_books": self.favorites,
            "wishlist_books": self.wish_list,
            "finished_books": self.finished_books
        }