from fastapi import FastAPI
from models import Todo

app = FastAPI()

@app.get('/')
async def root():
    return{"message": "Test"}

todos = []

# Get All Todos
@app.get('/todos')
async def get_todos():
    return{"todos": todos}


# Get Single Todo
@app.get('/todos/{todo_id}')
async def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return{"message": "No Data Found"}



# Create Todo
@app.post('/todos')
async def create_todo(todo: Todo):
    todos.append(todo)
    return{"message": "Sucessfully Created !"}


# Update Todo
@app.put('/todos/{todo_id}')
async def update_todo(todo_id: int, todo_new: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_new.item
            return {"tood": todo}
    return{"message": "No Data Found"}


# Delete Todo
@app.delete('/todos/{todo_id}')
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Operation Complete"}
    return{"message": "No Data Found"}