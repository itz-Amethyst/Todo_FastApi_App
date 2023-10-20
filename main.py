from fastapi import FastAPI

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



# Create Todo



# Update Todo



# Delete Todo