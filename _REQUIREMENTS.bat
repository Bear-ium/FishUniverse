@echo off

set "VENVDIR=.venv"
set "VENV_PATH=%CD%\%VENVDIR%"
set "ACTIVATE_PATH=%VENV_PATH%\Scripts\activate.bat"
set "REQPATH=%CD%\requirements.txt"

if NOT EXIST "%ACTIVATE_PATH%" (
  echo VirtualEnvironment does not exist. No attempt at installing requirements is being made.
  ) ELSE (
  call "%ACTIVATE_PATH%"
  
  if EXIST "%REQPATH%" (
    echo Installing requirements..
    pip install -r "%REQPATH%"
  )
)

call cls

cmd /k
