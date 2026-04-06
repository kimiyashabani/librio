import { useState } from "react";
function BookSearch(){
    const [query, setQuery] = useState("");
    const [books, setBooks] = useState([]);

const handleSearch = async () => {
    if (!query) return;
    try{
        const response = await fetch(
            `http://localhost:5000/library?q=${encodeURIComponent(query)}`
        );
        const data = await response.json();
        setBooks(data);
    }catch (error){
        console.error("Error fetching books:", error);
    }
};
return(
    <div>
        {/* Search bar*/}
        <input
            type = "text"
            placeholder = "Search a book ..."
            value = {query}
            onChange = {(e) => setQuery(e.target.value)}
        />
        <button onClick = {handleSearch}>Search</button>
        <div>
            {/* Search Result*/}
            {books.map((book) => (
          <div key={book.book_id}>
            <h3>{book.title}</h3>
            <p>{book.authors?.join(", ")}</p>
          </div>
        ))}
        
        </div>
    </div>

);
}
export default BookSearch;