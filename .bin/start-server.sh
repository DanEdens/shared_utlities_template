export TESTKIT_DEVMODE=false
export TESTKIT_DEBUG=true
export TESTKIT_LOG=true
export TESTKIT_DENA="bs"
export TESTKIT_EDITOR="vim"

mosquitto_sub -h %awsip% -p %awsport% -v -t "TestKit/#" | xargs -o -r -I {} python __main__.py --server {}
