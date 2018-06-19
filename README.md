# python-app

## Quick start

1. Create virtual env:

Using python 2.7

```bash
virtualenv -p `which python` env
```

2. Activate & install dependency

```bash
source ./env/bin/activate
pip install -r requirements.txt
```

3. Run on host

```bash
# start flask
./scripts/flask-start.sh

# start using gunicorn dispatcher (multiple processes)
./scripts/gunicorn-start.sh
```

4. Verify API

Note install `jq` to have pretty json format

```bash
curl http://127.0.0.1:8000/api/v1/test?p=1 | jq .
```

5. Build & Run on docker

```bash
make docker-build
make docker-run
```

