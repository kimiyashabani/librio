function BookCard({book}){
    return(
        <div className = "book-card">
            <h3>{book.title}</h3>
            <h4>{book.subtitle}</h4>
            <h4>{book.authors}</h4>
            <h4>{book.publisher}</h4>
            <h4>{book.publish_date}</h4>
            <h4>{book.pageCount}</h4>
            <h4>{book.genre}</h4>
            <h4>{book.language}</h4>
            <p>{book.description}</p>
        </div>
    );
}
export default BookCard;