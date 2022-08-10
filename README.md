# Start app
```bash
python app/main.py
```
# Create virtual environment
```bash
pipenv shell
```

# Execute migration
```bash
alembic upgrade head
```

## Docker
You can then build and run the Docker image:

```bash
docker build -t product-api .
```

```bash
docker run -it --rm --name product-api product-api
```

Run api container
```bash
docker run -d --name mycontainer -p 80:80 product-api
```