from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schema import Todo
from database import fetch_one_todo, fetch_all_todo, create_todo, update_todo, remove_todo

app = FastAPI()



origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/")
def read_root():
    return {'Ping': 'Pong'}


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todo()
    return response


@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_id(title):
    response = await fetch_one_todo(title)
    if not response:
        raise HTTPException(status_code=404, detail=f"Todo with title {title} not found")
    return response


@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if not response:
        raise HTTPException(status_code=400, detail=f"Something went wrong")
    return response


@app.put("/api/todo{title}", response_model=Todo)
async def put_todo(title: str, description: str):
    response = await update_todo(title, description)
    if not response:
        raise HTTPException(status_code=404, detail=f"Todo with title {title} not found")
    return response


@app.delete("/api/todo/{title}")
async def delete_todo(title: str):
    response = await remove_todo(title)
    if not response:
        raise HTTPException(status_code=404, detail=f"Todo with title {title} not found")
    return {"message": "Todo deleted"}


