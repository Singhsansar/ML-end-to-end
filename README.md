[![Python application test with Github Actions](https://github.com/Singhsansar/ML-end-to-end/actions/workflows/main.yml/badge.svg)](https://github.com/Singhsansar/ML-end-to-end/actions/workflows/main.yml)

# ML-end-to-end
training test and deploying the ML models

### To call Microservice


something like this 
```bash
curl -X 'POST' \
  'http://127.0.0.1:8080/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Nepal Country",
  "length": 2
}'
```
### Build container

`docker build .`
` docker image ls`

## Run Container 

  something like this

  `docker run -p 127.0.0.1:8080:8080  ff8872fe9684`

### Invoke POST request
run  `invoke.sh`