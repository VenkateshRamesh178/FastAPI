from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id:int
    item:str

@app.get("/")
async def root():
    return {"message": "Hello World"}

todos =[]

@app.get("/todos")
async def get_todos():
    return {"list" : todos}


@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for i in todos:
        if  todo_id == i.id:
            return i
    return {"message":"No todo found"}


@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "added"}

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for i in todos:
        if  todo_id == i.id:
            todos.remove(i)
            return {"message":"Todo is deleted"}
    return {"message":"No todo found"}