const logo = {
    name: 'Librio',
    imageUrl : 'https://www.rawpixel.com/search/book%20logo%20png',
    imageSize : 90,
}

export default function Logo(){
    return(
        <>
        <img
            className = "logo"
            src = {logo.imageUrl}
            alt = {'Logo of Biblio'}
            style = {{
                width: logo.imageSize,
                height: logo.imageSize
            }}
        />
        </>
    );
}