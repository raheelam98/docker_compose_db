from fastapi.testclient import TestClient
from sqlmodel import Session
import pytest

from app.main import app, get_session


from app import settings
from sqlmodel import create_engine, SQLModel

#####   pip install pytest

# ===============  test databse string =============== #

# connecting with database 
test_conn_string = str(settings.test_database_url).replace("postgresql", "postgresql+psycopg2")

# create engine
test_engine = create_engine(test_conn_string, connect_args={"sslmode":"require"}, pool_recycle=300, echo=True)

# create database and tables
def test_create_db_tables():
    SQLModel.metadata.create_all(test_engine)


#### ==================== fixture ==================== #####

# https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/?h=test

@pytest.fixture(name="session")
def session_fixture():
    test_create_db_tables()
    with Session(test_engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):   
    def get_session_override():
        return session  
    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


#### ==================== read main file ==================== #####
    

#### function to read main file
    
def test_read_main():
    #create TestClind for the fastapi app
    clinet = TestClient(app=app)
    response = clinet.get('/')
    assert response.status_code == 200
    assert response.json() == {'Fast API' : 'Todo Api'}

#### ==================== Get Data From Test Database ==================== #####


#### get todo from test-db
    
def test_get_todo(client : TestClient):
    response = client.get('/api_get_todos')
    assert response.status_code == 200   
     

#### ==================== Add Data Into Test Database ==================== #####

#### add todo into test-db

def test_add_in_db(client: TestClient):
    add_new_todo: str = "Operational Research"
    is_complete: bool = True
    
    # Ensure the response is assigned before accessing it
    response = client.post("/api_todos_test/", json={"todo_name": add_new_todo, "is_complete": is_complete})
    
    # Check that the status code is 200
    assert response.status_code == 200
    
    # Extract the JSON data from the response
    data = response.json()
    
    # Validate the data returned from the response
    assert data["todo_name"] == add_new_todo
    assert data["is_complete"] == True


#### ==================== Update Data From Test Database  ==================== ##### 

def test_update_todo_new(client : TestClient):
   
    id = 5  # todo id for testing
    test_name = "Discrete Mathematics"  # update todo name

    # Make the PUT request
    response = client.put(f'/api_update_todo_test?todo_id={id}', json=test_name)

    # Check the response
    assert response.status_code == 200  


#### ==================== Delete Data From Test Database (hero) ==================== ##### 

def test_delete_todo(client : TestClient):

        todo_id = 6
        response = client.delete(f'/api_delete_todo_hero/{todo_id}')
        assert response.status_code == 200

        for ids in response.json():
            assert  ids
            print(ids)

#### https://sqlmodel.tiangolo.com/tutorial/delete/
####  https://sqlmodel.tiangolo.com/tutorial/fastapi/delete/?h=dele   
