# Arcade Credit Counter

Pequeña y simple propuesta para visualizar un contador global de creditos estilo arcade.

![Ejemplo](/Proposal/Un-par-de-fichas-1-3.jpg)
![Diagrama](/Proposal/Un-par-de-fichas-2-3.jpg)
![Font](/Proposal/Un-par-de-fichas-3-3.jpg)

Como Bridge.py utiliza el módulo `serial`, es necesario instalar la librería `pyserial`.

Puedes instalarlo globalmente `pip install pyserial`

Y finalmente ejecutar el programa `python Bridge.py`

Con eso es suficiente, aunque si lo deseas puedes ponerlo en un entorno virtual:

# 1. Crear entorno virtual.
En la raíz del proyecto, ejecutar:

`./Bridge python -m venv venv`

# 2. Activar el entorno virtual

Windows cmd

`.\venv\Scripts\activate`

Windows PowerShell

`.\venv\Scripts\Activate.ps1`

macOS / Linux

`source venv/bin/activate`

# 3. Instalar dependencias (PySerial)

`pip install pyserial`


# 4. Ejecutar el script principal (Bridge.py)
Desde la raíz del proyecto:

`python Bridge.py`

# 5. Desactivar el entorno virtual (opcional)

`deactivate`