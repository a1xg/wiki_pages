## Deploy

#### Copy the repository
```git clone https://github.com/a1xg/wiki_pages.git```
#### Go to the root of the project
```cd wiki_pages```
#### Run docker-compose
```docker-compose up```


* The DRF-API server will be launched at http://localhost:8000/api/v1/news/list
* Superuser django will be created in docker compose script: 
username:admin, 
password:admin

## Postman API endpoint tests
* Import the Postman collection from the [link](https://github.com/a1xg/news/blob/master/News.postman_collection.json)
* Create a new empty environment in Postman before running the collection
* Run collection
