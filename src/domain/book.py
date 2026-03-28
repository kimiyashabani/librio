class Book:
    def __init__(self,id, title, subtitle, authors, publisher, publishDate, description, pageCount, genre, language):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.authors = authors or []
        self.publisher = publisher
        self.publish_date = publishDate
        self.description = description
        self.pageCount = pageCount
        self.genre = genre or []
        self.language = language
    
    def __repr__(self):
        return f"Book {self.title}, authors are:{self.authors}"
    def to_dict(self):
        return{

        }