# Prerequisites
- Install docker. Go to https://docs.docker.com/install/ and install a docker to your system
- Install redis-cli
- Install python redis module

# Setup Docker swarm
- Initialize docker swarm by executing a command like this one
``` docker swarm init --advertise-addr $(hostname -i) ```
- Make sure node is enabled
``` docker node ls ```
- Install docker registry 
``` docker service create --name registry --publish published=5000,target=5000 registry:2 ```

# Create and push stack
- Build the docker image
``` docker build --force-rm=true --tag=127.0.0.1:5000/redis ./redis-image ```
- Push the image
``` docker push 127.0.0.1:5000/redis ```
- Deploy docker swarm stack
``` docker stack deploy --compose-file=docker-stack.yml redis ```

# Healthcheck the redis service
- Make sure that all three dockers are up and running
``` redis-cli -h 127.0.0.1 -p 16379 ping ```
``` redis-cli -h 127.0.0.1 -p 16380 ping ```
``` redis-cli -h 127.0.0.1 -p 16381 ping ```

# Python script
- Run python script to write results
``` python test-redis.py ```
