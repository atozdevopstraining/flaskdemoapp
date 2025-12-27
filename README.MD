# Flask Demo APP

## run on local
```
python3 -m venv venv  # create virtual env
pip install -r requirements.txt

python3 app.py

```

## Run with Docker

```
docker build -t flaskdemoapp:latest .

docker run -it -d --name flaskdemoapp -p 8080:8080 flaskdemoapp:latest

curl localhost:8080/
curl localhost:8080/hi
```

## Create docker image and push to Dockerhub using github actions

Go through .github/workflows/ci.yml
```
docker run -it -d --name flaskdemoapp -p 8080:8080 atozdevopstraining/flaskdemoapp:latest
```
## Run on K8S

```
kubectl apply -f k8s/
```

