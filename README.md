# notifications
> Python notifications API

## Setup
### Dependencies
- MySQL

```sh
$ docker-compose up
```

### Running
```sh
pipenv install
pipenv run python app.py
```


### Build in docker
```sh
$ docker build -t notifications .
```

## Usage
### POST /api/v1/notifications
```sh
curl --request POST 'http://localhost/api/v1/notifications' \
--header 'Content-Type: application/json' \
--data-raw '{
	"id": "2b4d0c35-b111-472f-b47e-31de6c81d1e",
	"user_id": "2b4d0c35-b111-472f-b47e-31de6c81d10f",
	"message": "test"
}'
```

### GET /api/v1/notifications/{userId}
```sh
curl --request GET 'http://localhost/api/v1/notifications/2b4d0c35-b111-472f-b47e-31de6c81d10f'
```

## License
The MIT License (MIT)