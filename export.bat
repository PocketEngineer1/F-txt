@ECHO OFF
TITLE F txt Packager and Exporter
python -m compileall .
IF NOT EXIST "TMP/" MKDIR "TMP"
IF NOT EXIST "TMP/Modules/" MKDIR "TMP/Modules"
IF NOT EXIST "TMP/Modules/Interfaces/" MKDIR "TMP/Modules/Interfaces"
IF NOT EXIST "TMP/Modules/Outputs/" MKDIR "TMP/Modules/Outputs"

XCOPY "__pycache__\main.cpython-310.pyc" "TMP\" /c /y
XCOPY "__pycache__\utils.cpython-310.pyc" "TMP\" /c /y
XCOPY "__pycache__\console.cpython-310.pyc" "TMP\" /c /y

XCOPY "Modules\__pycache__\Configure.cpython-310.pyc" "TMP\" /c /y
XCOPY "Modules\Interfaces\__pycache__\CLI.cpython-310.pyc" "TMP\" /c /y
XCOPY "Modules\Interfaces\__pycache__\GUI.cpython-310.pyc" "TMP\" /c /y
XCOPY "Modules\Interfaces\__pycache__\WebUI.cpython-310.pyc" "TMP\" /c /y

XCOPY "Modules\Outputs\__pycache__\HTML.cpython-310.pyc" "TMP\" /c /y
XCOPY "Modules\Outputs\__pycache__\Markdown.cpython-310.pyc" "TMP\" /c /y
XCOPY "Modules\Outputs\__pycache__\MicrosoftWord.cpython-310.pyc" "TMP\" /c /y
XCOPY "Modules\Outputs\__pycache__\OpenDocumentText.cpython-310.pyc" "TMP\" /c /y
XCOPY "Modules\Outputs\__pycache__\StrapDownJS.cpython-310.pyc" "TMP\" /c /y
XCOPY "Modules\Outputs\__pycache__\TKinterApp.cpython-310.pyc" "TMP\" /c /y
TITLE 