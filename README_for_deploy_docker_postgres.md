
# Guía para Instalar Docker y Restaurar una Base de Datos PostgreSQL

## 1. Actualizar el sistema

Abre una terminal y ejecuta el siguiente comando para asegurarte de que todos los paquetes estén actualizados:

```bash
sudo apt update
sudo apt upgrade
```

## 2. Instalar dependencias

Instala las dependencias necesarias para permitir que `apt` use paquetes a través de HTTPS:

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

## 3. Agregar la clave GPG de Docker

Ejecuta este comando para agregar la clave GPG oficial de Docker:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
## 4. Agregar el repositorio de Docker

Añade el repositorio de Docker a tus fuentes de APT:

```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

## 5. Actualizar el índice de paquetes

Después de agregar el repositorio, actualiza el índice de paquetes nuevamente:

```bash
sudo apt update
```
## 6. Instalar Docker

Ahora puedes instalar Docker con el siguiente comando:

```bash
sudo apt install docker-ce
```
## 7. Verificar la instalación

Para comprobar que Docker se ha instalado correctamente, ejecuta:

```bash
sudo systemctl status docker
```
Deberías ver que el servicio Docker está activo y en ejecución.

## 8. Ejecutar Docker sin sudo (opcional)

Si deseas ejecutar Docker sin utilizar `sudo`, agrega tu usuario al grupo `docker`:
```bash
sudo usermod -aG docker $USER
```
Luego, cierra la sesión y vuelve a iniciar sesión para que los cambios surtan efecto.

----------

## Comandos para Ejecutar PostgreSQL en Docker

```bash
docker run --name my_postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=mario_shop_db -p 5432:5432 -v my_data_volume:/var/lib/postgresql/data -d postgres
```
Para listar los contenedores en ejecución:

```bash
docker ps
```
### Si usas Docker Compose, ejecuta en la terminal desde el mismo lugar donde esté el fichero `docker-compose.yml`:

```bash
docker compose up -d
```

### Compose de despliegue completo (Django + Gunicorn + Celery + Nginx)

El repositorio incluye una configuración de despliegue con:

- `docker-compose.yml` (producción)
- `docker-compose-dev.yml` (infraestructura de desarrollo: Postgres + Redis)
- `Dockerfile` (aplicación Django)
- `Dockerfile.nginx` (reverse proxy Nginx)

Antes de levantar `docker-compose.yml`, define en `.env` al menos:

- `WEBSITE_SLUG_NAME`
- `SECRET_KEY`
- `DB_REMOTE_NAME`, `DB_REMOTE_USER`, `DB_REMOTE_PASSWORD`
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`

Para ejecutar el stack de producción:

```bash
docker compose -f docker-compose.yml up -d --build
```

## Restaurar la Base de Datos

Primero, muévete a la carpeta donde está el respaldo. Como ejemplo genérico, usaremos el nombre `backup.sql`.

### 1. Copiar el archivo de respaldo al contenedor

```bash
docker cp backup.sql marioshop_postgres:/backup.sql
```

### 2. Acceder al contenedor

```bash
docker exec -it marioshop_postgres bash 
```

### 3. Restaurar la base de datos

```bash
psql -U postgres -d mario_shop_db -f /backup.sql
```
## Notas Adicionales

-   Asegúrate de que la base de datos (`mario_shop_db`) ya exista antes de intentar restaurar el respaldo. Si no existe, puedes crearla con:
    
    ```bash
    createdb -U postgres mi_base_de_datos
    ```
-  Si el archivo de respaldo es un archivo comprimido (por ejemplo, `.tar` o `.gz`), necesitarás descomprimirlo antes de la restauración.