# FastAPI Todo List
A simple todo list API written with FastAPI.

## Features

- Follows a basic MVC architecture
- Connects to a PostgreSQL database
- Dockerized  
- Unit tested with Pytest
- Uses Nginx as a reverse proxy

## Tech Stack  

- Python
- FastAPI
- PostgreSQL
- Nginx
- Docker & Docker Compose
- Pytest


## Usage

Clone the repository:

```
git clone https://github.com/mohamad-liyaghi/fastapi-todo-list.git
```

Change directory:

```
cd fastapi-todo-list/src
```

Start the app with Docker Compose:

```
docker-compose up --build 
```

Thats it! The API will be available on port 80, proxied through Nginx.
