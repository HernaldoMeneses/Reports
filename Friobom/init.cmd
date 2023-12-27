@echo off
set "source=%cd%"
set "HD=%source:~0,2%"

set "Adm=\GitHub\Reports\Friobom\Adm"


cd %HD%%Adm%
%HD%

call init.cmd

pause

