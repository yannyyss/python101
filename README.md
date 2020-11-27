# python101

Este es un proyecto de ejemplo para Rockstars G5

### Requisitos

-Python 3
-Docker

### Instrucciones

- Clonar este repo
- Crear imagen de docker

```
docker build -t "python101"
```

- Correr imagen en modo developer (salir con [CTR]+[C])

```
docker run -it -p 5000:5000 --rm --name "python101-volatil" python101
```

- Correr imagen en modo servicio

```
docker run -p 5000:5000 --name "python101-serv" python101
```
