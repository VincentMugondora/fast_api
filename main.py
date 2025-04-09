from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index() -> dict[str, str]:
    return{"hello": "world"}

@app.get("/about")
async def about() -> str:
    return "This is a simple FastAPI application."

@app.get("/services")
async def services():
    return{"services": "We offer a variety of services including web development, data analysis, and more."}