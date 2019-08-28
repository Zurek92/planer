# planer
plane scraper

## Run application in developer mode
1. enter `docker/` folder and run `docker-compose up`

## Docker commands:
### Images:
1. `docker images` - show all images
1. `docker rmi <image_id or image_name>` - remove image

### Containers:
1. `docker ps` - show running containers
1. `docker ps -a` - show all containers
1. `docker container rm <container_id>` - remove container
1. `docker container prune` - remove all containers
1. `docker exec -it <container_id> /bin/bash` - enter container

### Docker-compose:
1. `docker-compose up` - run application (containers)
1. `docker-compose down` - stop application (containers)
