## Prerequisites

1. Docker and Docker Compose should be installed on the machine.
2. Create .evn file and paste the following content there. It's for local setup in higher environment we have to ignore DB service as we will be using dedicated and independent db there.

```bash
DB_NAME=library
DB_USER=local
DB_PASS=local1234
DB_PORT=5432
DB_HOST=localhost
```
## Build and run Instructions

```bash
docker-compose build

docker-compose up
```

## To create migrations
```bash
docker-compose exec web alembic revision --autogenerate -m "message"

``` 

## To migrate changes to DB

```bash
alembic upgrade head
```
This step is already mention in start-all script to execute at inital level.


## To copy migrations changes to local before pushing to github

```bash
docker cp library_web_1:/library/migrations <to cloned repo path>

```