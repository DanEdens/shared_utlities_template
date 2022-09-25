REM call "%cd%/update.cmd"
set TESTKIT_DEVMODE=False
set TESTKIT_DEBUG=True
set TESTKIT_LOG=True
set TESTKIT_DENA="bs"
set TESTKIT_EDITOR="vim"


mosquitto_sub -h %awsip% -p %awsport% -v -t "TestKit/#" | xargs -o -r -I {} python __main__.py --server {}
