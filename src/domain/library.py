from src.api.books_api import LibrioAPI

bookAPI = LibrioAPI()

print(bookAPI.search_books("harry potter"))