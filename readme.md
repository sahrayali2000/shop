# shop
for run the project on your device you have some requirements : docker and docker-compose

after make sure that requirements is installed on your device following theese steps :

# step 1:
open your terminal and cd into project directory 

# step 2:
run the command " sudo docker-compose build "

# step 3:
run the command " sudo docker-compose up "

# step 4:
open another terminal and run the command " docker exec -it CONTAINER bash "

replace " CONTAINER " with the name of django app that docker made for this django app 

for finding name of django app just run command " sudo docker ps " and look at NAMES column  

# step 5:
cd shop and run the command " python manage.py createsuperuser "

# step 6:
open your browser and open " 0.0.0.0:8000 "

# DONE ! 

