# ============ revision ===============
"""
git hub commands :
        git init   -> create .git
        git add .  -> o'zgarishlarni ro'yhatga olish
        git commit -m 'Revision 1'
        git status ->
        git branch -> korish va o'zgartirish
        git push    -> commit qilingan file papkalarni yuborish !
"""

"""
DOCKER:
    engine  -> windows and macos and linux
    desktop -> windows and macos
    
commands:
    image download     : docker pull image_name:alpine
    images delete      : docker rmi -f id id id id id id
    images list        : docker images 
    images delete none : docker image prune
    create container   : docker container create -i -t --name mycontainer alpine
    create container   : docker container run -i -t --name mycontainer alpine
    create container create            : docker create -i -t --name mycontainer image_name
    create container create and start  : docker run -i -t -d --name mycontainer image_name
    
    
    container stop  : docker stop [id or name]
    docker exec -it mycontainer 
    
    
command for postgres con:
    docker run --name -i -t pg -e POSTGRES_PASSWORD=1 -p 5433:5432 -d postgres:alpine
    systemctl status postgresql
    systemctl start postgresql
    systemctl stop postgresql
    docker ps
     
"""

# postgres in docker : volume
