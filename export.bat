@ECHO OFF
TITLE F txt Packager and Exporter
python -m compileall .
if not exist "TMP/" mkdir "TMP"
TITLE 