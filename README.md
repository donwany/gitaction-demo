[![Test Multiple Python Versions](https://github.com/donwany/gitaction-demo/actions/workflows/main.yml/badge.svg)](https://github.com/donwany/gitaction-demo/actions/workflows/main.yml)

# devops-for-mlops
This demonstrates the core ideas of DevOps using git actions workflows

## Usage
```python
from mathz.add import add, multiply, divide
from mathz.subtract import subtract

add(1, 1)
multiply(2, 5)
divide(20, 2)

# collins added
subtract(99, 10)
```

## Train model
```python
from mathz.train import train

train()
```

## Build and Push Image
```shell
docker build -t worldbosskafka/mathz-app:1.0.0 .
docker tag worldbosskafka/mathz-app:1.0.0 worldbosskafka/mathz-app:1.0.0
docker push worldbosskafka/mathz-app:1.0.0

docker run worldbosskafka/mathz-app:1.0.0

```


