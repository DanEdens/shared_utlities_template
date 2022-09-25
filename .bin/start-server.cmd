REM call "%cd%/update.cmd"

mosquitto_sub -h %awsip% -p %awsport% -v -t "TestKit/#" | xargs -o -r -I {} python __main__.py --server {}
