@echo off
cd /d "%~dp0"
python actualizar-biblioteca.py || py actualizar-biblioteca.py || echo No se encontro Python. Instalalo desde python.org
echo.
echo Ahora sube la carpeta assets con GitHub Desktop (Commit y Push).
pause
