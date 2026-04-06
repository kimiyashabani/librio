import requests
from src.domain.book import Book
class LibrioAPI:
    URL = "https://www.googleapis.com/books/v1/volumes"
    
    def search_books(self,query:str):
        url = f"{self.URL}?q={query}"
        response = requests.get(url)
        data = response.json()
        books = []
        items = data.get("items",[])
        for item in items:
            volume = item.get("volumeInfo",{})
            bookID = item.get("id")
            book = Book(
                id=bookID,
                title=volume.get("title"),
                subtitle= volume.get("subtitle"),
                authors=volume.get("authors",[]),
                publisher=volume.get("publisher"),
                publishDate=volume.get("publishedDate"),
                description=volume.get("description"),
                pageCount=volume.get("pageCount"),
                genre=volume.get("categories",[]),
                language=volume.get("language")
            )
            books.append(book)
        return books
    
    #Get 1 specific book data:
    def get_book(self,bookID):
        url = f"{self.URL}/{bookID}"
        response = requests.get(url)
        book_data = response.json()
        book_data.get("volumeInfo",{})
        return Book(
            id=bookID,
            title=volume.get("title"),
            subtitle= volume.get("subtitle"),
            authors=volume.get("authors",[]),
            publisher=volume.get("publisher"),
            publishDate=volume.get("publishedDate"),
            description=volume.get("description"),
            pageCount=volume.get("pageCount"),
            genre=volume.get("categories",[]),
            language=volume.get("language")
        )

