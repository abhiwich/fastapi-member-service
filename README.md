# Fastapi Member Service 
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

เป็นการทดสอบ member service ที่พัฒนาด้วย python fastapi ร่วมกับ MongoDb ซึ่งการใช้งานจำลองสภาพแวดล้อม และเรียกใช้งานผ่าน Docker

## Requirement 
```
Docker
Python 3.9
MongoDb
```
## Network Diagram
![image](https://drive.google.com/uc?export=view&id=1QfTYFx9L9_DFpzXFylZ1kDVyrx3BePz_)


![image](https://drive.google.com/uc?export=view&id=1EaoKkVdKqHBUzhPuckBEK3aoRmRQyKpJ)


## 1.Installation 
- Docker install
(https://docs.docker.com/engine/install/) - Docker install for you os.

## 2.Setup Network Backend-nw 
```sh
docker network create --driver=bridge --subnet=172.18.0.0/16 backend-nw
docker network ls
docker network inspect backend-nw
```

## 3.Setup MongoDb 
```sh
- Docker pull MongoDb
docker pull mongo:5.0

- Create folder volumne for Mac 
mkdir ~/Docker/mongodb
- Create folder volumne for Windows 
d:
mkdir Docker/mongodb

- Docker run
docker run -d -p 27017:27017 -v ~/Docker/mongodb:/data/db --name mongo-con mongo:5.0
```

## 4.Setup Fastapi Project 

#### 4.1 Download member service
```sh
git clone https://github.com/abhiwich/fastapi-member-service.git
```
#### 4.2 Docker build
```sh
docker buile -t member-image:1.0 .
```
```sh
docker images
```
#### 4.3 Docker run
```sh
docker run -d -p 8300:8000 --network=backend-nw -e MONGO_DB_URL=mongodb://mongo-con:27017 --name member-con member-image:1.0
```



