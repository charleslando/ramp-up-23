from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/{name}')
async def root(name):
    return 'Hello, ' + name

# Create a subfolder called fastapi in your ramp-up-23 repository.

# Open a VS Code workspace in the fastapi folder.

# Create a new virtual environment in the fastapi/.venv folder and configure your project to use this environment as its interpreter.

# Create a Basic Hello World API using FastAPI:

# You are tasked with writing a simple API using FastAPI that takes a name as an input and responds with a "Hello, name" message.
# Create a requirements.txt file and check it in along with your code to the repository.

# Test your API locally using curl and the auto-generated Swagger docs page.

# Have a friend check out your repository and run your program from the command line, having it listen on port 8080.

# Upload the URL of the fastapi folder in your repository as the submission for this assignment