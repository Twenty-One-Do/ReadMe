# 📃 ReadMe
ReadMe is an online community where creators can share their portfolios and network with others. Users can showcase their own work and explore the works of other creators, facilitating collaboration and inspiration. This platform provides an intuitive and user-friendly space for exchanging creative work and experiences.

## 🔧 Environment
- Python: 3.11
- Redis: 
- Postgresql: 
- Nginx: 

## 🐋 Docker Setting

Run the following two commands in the root directory of the project to create both deployment and development environments:

``
docker-compose -f docker-compose.yml -p dep up -d
``

``
docker-compose -f docker-compose-develop.yml -p dev up
``

If the containers stop due to a computer restart or any other reason, run the following two commands to restart the containers:

``
docker start develop-env
``

``
docker start deploy-env
``

## ERD

## API

# 🚀 Release Notes

## Opinion 0.1.0(0000-00-00)

### New Features:

### Improvements:

### Bug Fixes:

### Known Issues:

### Other Information: