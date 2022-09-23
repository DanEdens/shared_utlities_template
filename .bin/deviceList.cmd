type devicelist.txt > Archive/devicelist.txt
"%programfiles%\mosquitto\mosquitto_sub.exe" -v -C 1 -h %awsip% -p %awsport% -t testkit/devicelist > devicelist.txt
