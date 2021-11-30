## Deploy

#### Copy the repository
```git clone https://github.com/a1xg/wiki_pages.git```
#### Go to the root of the project
```cd wiki_pages```
#### Run docker-compose
```docker-compose up```
* The Django server will be launched at http://127.0.0.1:8000/
* Tests will be run during the execution of the docker-compose
* Superuser django will be created in docker-compose: 
  * username: **admin**, 
  * password: **admin**
#### Endpoints list:
   * `/api-auth/login/?next=/api/v1/pages/list` Login page
   * `/api/v1/create` Create a new page
   * `/api/v1/pages/list` Getting a list of created pages  
   * `/api/v1/pages/<int:pk>` Getting a specific page by id   
   * `/api/v1/pages/<int:pk>/versions/list` Getting a list of versions of a specific page by id   
   * `/api/v1/pages/<int:page>/versions/<int:pk>` Getting a specific version (id) of a specific page by id
   * `/api/v1/pages/<int:pk>/versions/set-current` Setting the current version of a specific page, you need to specify the ID of the historical page

## Postman API endpoint tests
* Import the Postman collection from the [link](https://github.com/a1xg/wiki_pages/tree/master/postman_collection/)
* Create a new empty environment in Postman before running the collection
* Run collection
