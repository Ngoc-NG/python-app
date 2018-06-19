
# project home dir: grab-share-discount

REPO=grabds/python-app
TAG=latest

docker-build:
	docker build -t $(REPO):$(TAG) .

docker-push:
	docker push $(REPO):$(TAG)

docker-run:
	docker run -it --rm \
    	-p 8000:8000 \
    	-e APP_GUNICORN_WORKERS=2 \
    	grabds/python-app:latest
