# Proyecto Django Rest Framework
Este repositorio contiene un proyecto desarrollado con **Django Versión 5.2.10**.  

A continuación se describen los pasos necesarios para ejecutar el proyecto correctamente en Windows.

## Requisitos para su instalación
Python 3.13.1

## Clonar repositorio
Abra cmd en la ruta donde desea descargar el proyecto y ejecute: `git clone https://github.com/javie-rr/sorter-backend.git`

Accede a la carpeta raíz del proyecto `cd sorter-backend`

## Crear entorno virtual (Windows)
Para crear un entorno virtual ejecute `python -m venv venv`

Para activarlo ejecute: `venv\Scripts\activate`

Para desactivarlo ejecute: `deactivate`

## Instalar dependencias
Con el entorno virtual activado, ejecute: `pip install -r requirements.txt`

## Migraciones
Crear archivos de migración: `python manage.py makemigrations`

Aplicar archivos de migración a la base de datos: `python manage.py migrate`

## Crear un superusuario
Cree un superusuario, utilizando el comando: `python manage.py createsuperuser`

## Levanta un servidor 
Ejecute el comando: `python manage.py runserver`

## Endpoint Iniciar sesión
Endpoint para inicar sesión: `http://127.0.0.1:8000/api/auth/login`



