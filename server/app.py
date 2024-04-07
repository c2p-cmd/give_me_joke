import os
import json
from random import choice as random_element

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["get"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {
        "status" : "Okay!",
        "message" : "All systems operational"
    }

@app.get("/joke")
def get_joke(
    programming: bool = False,
    id: str = None
):
    cwd = os.getcwd()

    if programming:
        path = f"{cwd}/outputs/programming_jokes_combined.json" 
    else:
        path = f"{cwd}/outputs/non_programming_jokes_combined.json"
    with open(path) as joke_file:
        jokes = json.load(joke_file)
    
    if id:
        filered_joke = list(filter(lambda element: element['id'] == id, jokes))
        if len(filered_joke) == 0:
            raise HTTPException(status_code=404, detail="Joke not found")
        else:
            return filered_joke[0]
    
    return random_element(seq=jokes)