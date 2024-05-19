docker build -t postgres:1 -f DockerfilePostgres .
docker run -p 5432:5432 --name DBcont postgres:1
docker rm DBcont

scrapy crawl mycrawler


docker exec -it pythonproject-crawler-1 ./bin/bash
