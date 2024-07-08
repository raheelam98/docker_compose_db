# main.py
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
from app import settings
from sqlmodel import Field, Session, SQLModel, create_engine, select, Sequence
from fastapi import FastAPI, Depends, HTTPException, Body
from typing import AsyncGenerator

####  https://www.youtube.com/watch?v=cpu44VE_J1I&t=5554s 

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)


# only needed for psycopg 3 - replace postgresql
# with postgresql+psycopg in settings.DATABASE_URL
connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)


# recycle connections after 5 minutes
# to correspond with the compute scale down
engine = create_engine(
    connection_string, connect_args={}, pool_recycle=300
)

def create_db_and_tables()->None:
    SQLModel.metadata.create_all(engine)


# The first part of the function, before the yield, will
# be executed before the application starts.
# https://fastapi.tiangolo.com/advanced/events/#lifespan-function
@asynccontextmanager
async def lifespan(app: FastAPI)-> AsyncGenerator[None, None]:
    print("Creating tables..")
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan, title="API with DB container")


# app = FastAPI(lifespan=lifespan, title="API with DB", 
#     version="0.0.1",
#     servers=[
#         {
#             "url": "http://0.0.0.0:8000", # ADD NGROK URL Here Before Creating GPT Action
#             "description": "Development Server"
#         }
#         ])

def get_session():
    with Session(engine) as session:
        yield session


@app.get("/")
def read_root():
    return {"Docker": "Compose DB"}

@app.get("/api_todos/", response_model=list[Todo])
def read_todos(session: Annotated[Session, Depends(get_session)]):
        todos = session.exec(select(Todo)).all()
        return todos

@app.post("/api_todos_test/", response_model=Todo)
def create_todo(todo: Todo, session: Annotated[Session, Depends(get_session)]):
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo


@app.put("/api_update_todo_test", response_model=Todo)
async def update_todo(todo_id : int, content :Annotated[str, Body()], session: Annotated[Session, Depends(get_session)]):
     get_id : Todo = select(Todo).where(Todo.id == todo_id)
     update_todo = session.exec(get_id).first()
     if not update_todo:
        raise HTTPException(status_code=404, detail=(f"Todo Id: {todo_id} Not Found In DB"))
     else:
        update_todo.content = content
        session.add(update_todo)
        session.commit()
        session.refresh(update_todo)
        return  update_todo

@app.delete("/api_delete_todo_hero/{todo_id}/")
def delete_todo(todo_id: int, session: Annotated[Session, Depends(get_session)]):   
    todo_sel = session.get(Todo, todo_id)
    if not todo_sel:
        raise HTTPException(status_code=404, detail=(f'Todo ID {todo_id} Not Found In DB'))
    session.delete(todo_sel)
    session.commit()
    return todo_sel

@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo, session: Annotated[Session, Depends(get_session)])->Todo:
        try:
            session.add(todo)
            session.commit()
            session.refresh(todo)
            return todo
        except Exception as e:
            print(f"Error creating todo: {e}")
            raise HTTPException(status_code=405 , detail="Failed to create todo")




######  ---------------------------------------------------------- ####


