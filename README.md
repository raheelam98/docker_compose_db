## Todo Api (Docker Compose with Database Service)

**add poetry drivers** (one line command)
```shell
poetry add fastapi sqlmodel uvicorn\[standard\] psycopg 
```

**==========================================**

 **build new image** 
```shell
 docker compose up -d 
```
build the image and starts the container in detached mode 

Note :- -d, --detach  (Detached mode: Run containers in the background)

 **rebuild the image** 
  ```shell
 docker compose up -d --build 
```
(recreate the image —> - - build)

**container detail** 
 ```shell
 docker compose config 
```

**stop running container**
```shell
 docker compose stop

 docker stop {OPTIONS} containerID/container_name
```

**restart container**
  ```shell
 docker restart container_name/container_id
```

**stops and removes the container**
```shell
 docker compose down
```
1. Stop all containers
2. Remove all containers
3. Remove all networks

**view logs** 
 ```shell
 docker-compose logs service-name
```

**view logs (real-time monitoring)**
 ```shell
 docker-compose logs service-name -f
```
- f  (follow)(real-time.) (give all the command running on terminal)
  
**display container** 
 ```shell
 docker compose ps 

 docker ps {OPTIONS}
```
-a flag:  shows us all the containers, stopped or running. {-a: Stands for "all"}

-l flag: shows us the latest container.

-q flag: shows only the Id of the containers. 

display : NAME ,  IMAGE,   COMMAND,  SERVICE,  CREATED , STATUS ,  PORTS
    
 **container list**
```bash
 docker compose ls 

 docker container ls {OPTIONS}

 docker container  ls -a
```
display containers :-  NAME  - STATUS  -  CONFIG FILES
-a : all  (list of all containers, both running and stopped)

**forcefully stop running container** 
 ```shell
 docker kill containerID/container_name 

 docker kill {OPTIONS} containerID/container_name 
```

### pgAdmin

<div style="text-align: center;">
    <img alt="" src="./images/db_pgAdmin_step1.png" width="400px"></img>
</div>

### Query Tool

<div style="text-align: center;">
    <img alt="" src="./images/db_queryTool.png" width="400px"></img>
</div>


### Online Class

#### Playlist

[Modern Cloud Native AI Stack: Python, Poetry, Docker.. Online Class](https://www.youtube.com/playlist?list=PL0vKVrkG4hWqWNAr6rcX0gOvU_eOULnJN)

[Docker - Complete Tutorial: (Docker File, Image, Container](https://www.youtube.com/playlist?list=PL0vKVrkG4hWoTh2SaepYf9N8ywxz_Cyfx)

[Apache Kafka - Event Driven Architecture](https://www.youtube.com/playlist?list=PL0vKVrkG4hWrlSxLssJeuyMKGIegYiUyz)

[Generative AI with Cloud-Native Power: Microservices, Multi-Agent](https://www.youtube.com/playlist?list=PL0vKVrkG4hWpk12F7wO41kdFWhuXuigDW)

[Cloud Deployment - Azure Container Apps](https://www.youtube.com/playlist?list=PL0vKVrkG4hWrqwmlQ6k8ArJ93BrwX6V4l)


#### Dev Container
[Dev Container Online Class 06: What is Dev Container (Development inside Containers) - Docker](https://www.youtube.com/watch?v=h32qw986-tI)

#### Kafka
[GenAI Quarter 5 Online Class 12: Interact with Kafka using aiokafka - A Python Library for Kafka](https://www.youtube.com/watch?v=PAU05OrLgho)

[GenAI Quarter 5 Online Class 13: Serialization and Deserialization Kafka Messages](https://www.youtube.com/watch?v=qVbAYHxW3xg&list=PL0vKVrkG4hWqWNAr6rcX0gOvU_eOULnJN&index=13)

#### Portobuf
[GenAI Quarter 5 Online Class 14: Protobuf in Kafka & Introduction to Kong - An API Gateway](https://www.youtube.com/watch?v=nMXMV48EiQA)

[GenAI Quarter 5 Online Class 13: Serialization and Deserialization Kafka Messages](https://www.youtube.com/watch?v=qVbAYHxW3xg)

#### Pg Admin
[GenAI Quarter 5 Online Class 08: Docker Compose - Running Multi Containers with Docker Compose](https://www.youtube.com/watch?v=l5eZMAhDwhQ&t=3117s)

[GenAI Quarter 5 Online Class 07: Docker Compose - Orchestrate Multi-Container Applications with Ease](https://www.youtube.com/watch?v=cpu44VE_J1I&t=5554s) 


### Github

### Docker

[Docker for Microservices](https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/14_docker)

**Production Dockerfile explanation**
05_microservices_all_in_one_platform/14_docker/01_containerizing_poetry
[Containerizing a Poetry Project](https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/14_docker/01_containerizing_poetry)

**Detailed explanation of the Docker Compose file:**
05_microservices_all_in_one_platform/14_docker/05_compose_db
[Docker Compose with Database Service](https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/14_docker/05_compose_db)

05_microservices_all_in_one_platform/14_docker/07_synchronous_messages
[Synchronous Inter Services Messages between Microservices](https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/14_docker/07_synchronous_messages)


### Event-driven architecture (EDA)

[Event-driven](https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/15_event_driven)

05_microservices_all_in_one_platform/15_event_driven/00_eda_challenge
[A Challenge: FastAPI Event Driven Microservices Development With Kafka, KRaft, Docker Compose, and Poetry](https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/15_event_driven/00_eda_challenge)

05_microservices_all_in_one_platform/15_event_driven/02_kafka_messaging
[kafka_messaging](https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/15_event_driven/02_kafka_messaging)


**Detailed explanation of Protobuf Kafka Messaging**
05_microservices_all_in_one_platform/15_event_driven/02_kafka_messaging
[Protobuf Kafka Messaging](https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/15_event_driven/03_protobuf)


### oauth2_auth

[FastAPI OAuth2 Authentication and Authorization](https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/16_oauth2_auth)





# docker_compose_db
