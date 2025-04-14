from fastapi import FastAPI

app = FastAPI()
 
BANDS = [
    {
        "name": "The Beatles",
        "genre": "pop",
        "members": ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],
        "formed": 1960,
        "origin": "Liverpool, England"
    },
    {
        "name": "Queen",
        "genre": "Rock",
        "members": ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"],
        "formed": 1970,
        "origin": "London, England"
    },
    {
        "name": "Pink Floyd",
        "genre": "Progressive Rock",
        "members": ["Syd Barrett", "Roger Waters", "Nick Mason", "Richard Wright", "David Gilmour"],
        "formed": 1965,
        "origin": "London, England"
    },
    {
        "name": "Nirvana",
        "genre": "Grunge",
        "members": ["Kurt Cobain", "Krist Novoselic", "Dave Grohl"],
        "formed": 1987,
        "origin": "Aberdeen, Washington, USA"
    },
    {
        "name": "Metallica",
        "genre": "Heavy Metal",
        "members": ["James Hetfield", "Lars Ulrich", "Kirk Hammett", "Robert Trujillo"],
        "formed": 1981,
        "origin": "Los Angeles, California, USA"
    }
]

@app.get("/")
async def index() -> dict[str, str]:
    return {"hello": "world"}

@app.get("/about")
async def about() -> str:
    return "This is a simple FastAPI application."

@app.get("/bands")
async def bands() -> list[dict]:
    return BANDS

@app.get("/bands/{band_name}")
async def bands_id(band_name: str) -> dict:
    band = next((band for band in BANDS if band["name"].lower() == band_name.lower()), None)
    if band is None:
        return {"error": "Band not found"}
    return band

@app.get("/bands/genre/{genre}")
async def bands_genre(genre: GenreURLChoices) -> list[dict] | dict:
    genre_bands = [
        band for band in BANDS
        if band["genre"].lower().replace(" ", "_") == genre.value
    ]
    if not genre_bands:
        return {"error": "Genre not found"}
    return genre_bands

