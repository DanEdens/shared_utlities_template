@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
if "%confluence_server_url%" == "" (
    set confluence_server_url=https://danedens.atlassian.net/wiki/home/
)
if "%confluence_server_key%" == "" (
    set confluence_server_key = False
)
if "%confluence_server_user%" == "" (
    set confluence_server_user = dane@minim.com
)
if "%confluence_server_pass%" == "" (
    echo "Pass not set. Please set confluence_server_pass"
    exit /B 5
)
if "%confluence_server_publish%" == "" (
    echo Confluence Publish disabled 
    set confluence_server_publish = False
)

set SOURCEDIR=source
set BUILDDIR=build

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "" goto help

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
