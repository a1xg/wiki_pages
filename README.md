## Deploy

#### Copy the repository
```git clone https://github.com/a1xg/wiki_pages.git```
#### Go to the root of the project
```cd wiki_pages```
#### Run docker-compose
```docker-compose up```
* The DRF-API server will be launched at http://localhost:8000/
* Endpoints list:
   /api/v1/create
   /api/v1/pages/list
   /api/v1/pages/<int:pk>
   /api/v1/pages/<int:pk>/versions/list
   /api/v1/pages/<int:page>/versions/<int:pk>
   /api/v1/pages/<int:pk>/versions/set-current
        
* Unit tests will be run during the execution of the docker compose script
* Superuser django will be created in docker compose script: 
username:admin, 
password:admin

## Postman API endpoint tests
* Import the Postman collection from the [link](https://github.com/a1xg/wiki_pages/postman_collection/)
* Create a new empty environment in Postman before running the collection
* Run collection
