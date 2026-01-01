@echo off

set "VENVDIR=.venv"
set "VENV_PATH=%CD%\%VENVDIR%"
set "ACTIVATE_PATH=%VENV_PATH%\Scripts\activate.bat"
set "MAIN=%CD%\Bot\main.py"

call cls

if NOT EXIST "%ACTIVATE_PATH%" (
    echo No launch as no VirtualEnvironment was found! Please launch _SETUP.bat first
  ) ELSE (
  call "%ACTIVATE_PATH%"
  
  if EXIST "%MAIN%" (
    py "%MAIN%"
  )
)

cmd /k
