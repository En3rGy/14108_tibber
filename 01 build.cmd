@echo off
set path=%path%;C:\Python27\
set PYTHONPATH=C:\Python27;C:\Python27\Lib
@echo on

cd ..\..
C:\Python27\python generator.pyc "14108_tibber" UTF-8

xcopy .\projects\14108_tibber\src .\projects\14108_tibber\release

@echo Done.

@pause