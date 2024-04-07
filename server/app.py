import os
import json
from random import choice as random_element

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = ["*"]
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["get"],
    allow_headers=["*"],
)


@api.get("/")
def health_check():
    return {
        "status" : "Okay!",
        "message" : "All systems operational"
    }

@api.get("/joke")
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

if __name__ == '__main__':
    uvicorn.run(app="app:api", host="0.0.0.0", port=8000, reload=True)