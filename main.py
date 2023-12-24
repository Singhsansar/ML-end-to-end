import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from pydantic import BaseModel
from mylib.bot import scrape


class Wiki(BaseModel):
    name: str
    length: int


app = FastAPI()


@app.post("/predict")
async def predict(wiki: Wiki):
    result = scrape(wiki.name, sentences=wiki.length)
    payload = {"wikipage": result}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data, status_code=201)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""
    return {"result": num1 + num2}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
