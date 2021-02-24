@echo off
set path=%path%;C:\Python27\
set PYTHONPATH=C:\Python27;C:\Python27\Lib

echo ^<head^> > .\release\log14108.html
echo ^<link rel="stylesheet" href="style.css"^> >> .\release\log14108.html
echo ^<title^>Logik - Leistungsmesser (11083)^</title^> >> .\release\log14108.html
echo ^<style^> >> .\release\log14108.html
echo body { background: none; } >> .\release\log14108.html
echo ^</style^> >> .\release\log14108.html
echo ^<meta http-equiv="Content-Type" content="text/html;charset=UTF-8"^> >> .\release\log14108.html
echo ^</head^> >> .\release\log14108.html

@echo on

type .\README.md | C:\Python27\python -m markdown -x tables >> .\release\log14108.html

@echo on

cd ..\..
C:\Python27\python generator.pyc "14108_tibber" UTF-8

xcopy .\projects\14108_tibber\src .\projects\14108_tibber\release

@echo Done.

@pause