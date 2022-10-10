@ECHO OFF
TITLE F txt Packager and Exporter
SET CCD=%CD%
python -m compileall .

IF NOT EXIST "TMP\" MKDIR "TMP"
IF NOT EXIST "TMP\Modules\" MKDIR "TMP\Modules"
IF NOT EXIST "TMP\Modules\Interfaces\" MKDIR "TMP\Modules\Interfaces"
IF NOT EXIST "TMP\Modules\Outputs\" MKDIR "TMP\Modules\Outputs"

XCOPY "version.json" "TMP\" /c /y
XCOPY "requirements.bat" "TMP\" /c /y
XCOPY "requirements.txt" "TMP\" /c /y

XCOPY "__pycache__\main.cpython-310.pyc" "TMP\" /c /y
XCOPY "__pycache__\utils.cpython-310.pyc" "TMP\" /c /y
XCOPY "__pycache__\console.cpython-310.pyc" "TMP\" /c /y

XCOPY "Modules\__pycache__\Configure.cpython-310.pyc" "TMP\Modules\" /c /y

XCOPY "Modules\Interfaces\__pycache__\CLI.cpython-310.pyc" "TMP\Modules\Interfaces\" /c /y
XCOPY "Modules\Interfaces\__pycache__\GUI.cpython-310.pyc" "TMP\Modules\Interfaces\" /c /y
XCOPY "Modules\Interfaces\__pycache__\WebUI.cpython-310.pyc" "TMP\Modules\Interfaces\" /c /y

XCOPY "Modules\Outputs\__pycache__\HTML.cpython-310.pyc" "TMP\Modules\Outputs\" /c /y
XCOPY "Modules\Outputs\__pycache__\Markdown.cpython-310.pyc" "TMP\Modules\Outputs\" /c /y
XCOPY "Modules\Outputs\__pycache__\MicrosoftWord.cpython-310.pyc" "TMP\Modules\Outputs\" /c /y
XCOPY "Modules\Outputs\__pycache__\OpenDocumentText.cpython-310.pyc" "TMP\Modules\Outputs\" /c /y
XCOPY "Modules\Outputs\__pycache__\StrapDownJS.cpython-310.pyc" "TMP\Modules\Outputs\" /c /y
XCOPY "Modules\Outputs\__pycache__\TKinterApp.cpython-310.pyc" "TMP\Modules\Outputs\" /c /y

IF EXIST "TMP\main.pyc" DEL "TMP\main.pyc"
IF EXIST "TMP\utils.pyc" DEL "TMP\utils.pyc"
IF EXIST "TMP\console.pyc" DEL "TMP\console.pyc"

IF EXIST "TMP\Modules\Configure.pyc" DEL "TMP\Modules\Configure.pyc"

IF EXIST "TMP\Modules\Interfaces\CLI.pyc" DEL "TMP\Modules\Interfaces\CLI.pyc"
IF EXIST "TMP\Modules\Interfaces\GUI.pyc" DEL "TMP\Modules\Interfaces\GUI.pyc"
IF EXIST "TMP\Modules\Interfaces\WebUI.pyc" DEL "TMP\Modules\Interfaces\WebUI.pyc"

IF EXIST "TMP\Modules\Outputs\HTML.pyc" DEL "TMP\Modules\Outputs\HTML.pyc"
IF EXIST "TMP\Modules\Outputs\Markdown.pyc" DEL "TMP\Modules\Outputs\Markdown.pyc"
IF EXIST "TMP\Modules\Outputs\MicrosoftWord.pyc" DEL "TMP\Modules\Outputs\MicrosoftWord.pyc"
IF EXIST "TMP\Modules\Outputs\OpenDocumentText.pyc" DEL "TMP\Modules\Outputs\OpenDocumentText.pyc"
IF EXIST "TMP\Modules\Outputs\StrapDownJS.pyc" DEL "TMP\Modules\Outputs\StrapDownJS.pyc"
IF EXIST "TMP\Modules\Outputs\TKinterApp.pyc" DEL "TMP\Modules\Outputs\TKinterApp.pyc"

RENAME "TMP\main.cpython-310.pyc" "main.pyc"
RENAME "TMP\utils.cpython-310.pyc" "utils.pyc"
RENAME "TMP\console.cpython-310.pyc" "console.pyc"

RENAME "TMP\Modules\Configure.cpython-310.pyc" "Configure.pyc"

RENAME "TMP\Modules\Interfaces\CLI.cpython-310.pyc" "CLI.pyc"
RENAME "TMP\Modules\Interfaces\GUI.cpython-310.pyc" "GUI.pyc"
RENAME "TMP\Modules\Interfaces\WebUI.cpython-310.pyc" "WebUI.pyc"

RENAME "TMP\Modules\Outputs\HTML.cpython-310.pyc" "HTML.pyc"
RENAME "TMP\Modules\Outputs\Markdown.cpython-310.pyc" "Markdown.pyc"
RENAME "TMP\Modules\Outputs\MicrosoftWord.cpython-310.pyc" "MicrosoftWord.pyc"
RENAME "TMP\Modules\Outputs\OpenDocumentText.cpython-310.pyc" "OpenDocumentText.pyc"
RENAME "TMP\Modules\Outputs\StrapDownJS.cpython-310.pyc" "StrapDownJS.pyc"
RENAME "TMP\Modules\Outputs\TKinterApp.cpython-310.pyc" "TKinterApp.pyc"

IF EXIST "TMP\run.bat" DEL "TMP\run.bat"

XCOPY "run_export.bat" "TMP\"
RENAME "TMP\run_export.bat" "run.bat"

CD TMP
IF EXIST "app.zip" DEL "app.zip"
7z a app.zip run.bat
7z a app.zip Modules
7z a app.zip main.pyc
7z a app.zip utils.pyc
7z a app.zip console.pyc
7z a app.zip version.json
7z a app.zip requirements.bat
7z a app.zip requirements.txt
CD %CCD%

TITLE 