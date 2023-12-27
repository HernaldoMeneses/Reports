@echo off
set "source=%cd%"
set "HD=%source:~0,2%"

set "conex=\Friobom\Engineering\conex"
set "email=\Friobom\Engineering\email"

cd %HD%%conex%
%HD%
call conex.cmd
pause

cd %HD%%email%
%HD%
call send.cmd
pause

rem Bugada
rem cd L:\Friobom\Engineering\R
rem L:
rem call rscript.cmd
rem pause