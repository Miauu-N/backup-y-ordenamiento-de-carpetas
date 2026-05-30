# Scripting en Python: Organizador de Carpetas y Backups

Este repositorio contiene un conjunto de scripts en **Python** desarrollados con el propósito de aprender y poner en práctica conceptos básicos y fundamentales de scripting, automatización de tareas y diseño de interfaces gráficas sencillas. 

El proyecto abarca el manejo del sistema de archivos, la programación de tareas concurrentes y la creación de una interfaz visual intuitiva.

---

## 🚀 Características Principales

1. **Organizador Automático de Archivos (`ordenar_carpeta.py`)**
   - Escanea un directorio seleccionado y clasifica de forma automática todos los archivos en subcarpetas organizadas según sus respectivas extensiones (por ejemplo: `.txt` en una carpeta llamada `txt`, `.pdf` en una carpeta `pdf`, etc.).
   - Mueve de manera segura los archivos y gestiona de forma dinámica la creación de los directorios necesarios.

2. **Programador de Copias de Seguridad (Backups) (`schedule_backup.py`)**
   - Realiza copias de seguridad de un directorio origen a un directorio destino de manera automatizada.
   - Utiliza programación horaria periódica para ejecutar los respaldos en segundo plano.
   - Cuenta con una política de **rotación de backups**: controla la cantidad de copias guardadas según el límite establecido por el usuario, eliminando automáticamente la versión más antigua para optimizar el almacenamiento.

3. **Interfaz Gráfica de Usuario (`interfaz.py`)**
   - Una GUI limpia e intuitiva desarrollada en **Tkinter** que permite a cualquier usuario interactuar con los scripts de organización y backup sin necesidad de usar la línea de comandos.
   - Utiliza **hilos en segundo plano** (`threading`) para que las tareas de larga duración (como el bucle de backups) no congelen la interfaz gráfica.

---

## 🛠️ Stack Tecnológico

El proyecto está desarrollado utilizando Python y diversas librerías tanto de la biblioteca estándar como de terceros:

- **Lenguaje**: [Python 3.x](https://www.python.org/)
- **Interfaz Gráfica**: [Tkinter](https://docs.python.org/3/library/tkinter.html) (Biblioteca estándar)
- **Manejo de Archivos y Rutas**: `pathlib` y `shutil` (Biblioteca estándar)
- **Concurrencia**: `threading` (Biblioteca estándar)
- **Programación de Tareas**: `schedule` (Librería externa para programar eventos en intervalos)

---

## 📋 Guía de Uso

A continuación se detallan los pasos para clonar, instalar dependencias y ejecutar el proyecto localmente.

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/backup-y-ordenamiento-de-carpetas.git
cd backup-y-ordenamiento-de-carpetas
```

### 2. Configurar el Entorno Virtual (Recomendado)
Es aconsejable utilizar un entorno virtual para mantener limpias las dependencias globales del sistema.

*En Windows:*
```bash
python -m venv venv
venv\Scripts\activate
```

*En macOS/Linux:*
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias
Instala los paquetes necesarios definidos en `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Ejecución del Proyecto

#### Interfaz Gráfica (Organizador y Backups)
Para iniciar la aplicación visual, ejecuta el script principal:
```bash
python interfaz.py
```
- **Botón "Seleccionar carpeta y organizar"**: Te solicitará elegir un directorio para organizar de forma inmediata sus archivos por su extensión.
- **Botón "Seleccionar carpeta y crear backup"**: Te pedirá seleccionar la carpeta origen, el destino para los respaldos y la cantidad máxima de copias de seguridad a conservar. Una vez configurado, el proceso se ejecutará de fondo en un hilo secundario y generará los respaldos de forma programada diaria.

---

## 💡 Aprendizajes Adquiridos
Durante el desarrollo de este proyecto se reforzaron habilidades en:
- Automatización de tareas repetitivas en el sistema operativo local.
- Uso de programación concurrente (hilos) para evitar bloqueos de la interfaz principal en aplicaciones de escritorio.
- Manipulación segura de rutas de archivos independientes del sistema operativo con `pathlib`.
