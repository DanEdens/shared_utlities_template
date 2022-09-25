# mosquitto_pub -h %awsip% -p %awsport% -t "loggernet/devicelist" -f "devicelist.txt"
deviceList = [
        "S10",
        "bs"
        ]

testList = [
        "pullDeviceList",
        # "pubFullStatus",
        "start-server",
        "update"
        ]
