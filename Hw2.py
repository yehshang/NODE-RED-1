[
    {
        "id": "ce95166b.e0b328",
        "type": "inject",
        "z": "24e62232.c43e9e",
        "name": "mcs",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 110,
        "y": 120,
        "wires": [
            [
                "280d6035.c5526",
                "5ff9cae5.d8d134"
            ]
        ]
    },
    {
        "id": "280d6035.c5526",
        "type": "function",
        "z": "24e62232.c43e9e",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"aiPA8TCGnwGWXCqD\"\n}\nreturn msg;",
        "outputs": "1",
        "noerr": 0,
        "x": 100,
        "y": 260,
        "wires": [
            [
                "6ce71fd3.5dadf"
            ]
        ]
    },
    {
        "id": "6ce71fd3.5dadf",
        "type": "http request",
        "z": "24e62232.c43e9e",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DL6YK308/datachannels/Temperature/datapoints.csv",
        "tls": "",
        "x": 230,
        "y": 260,
        "wires": [
            [
                "d93dafcc.04f61",
                "d0f76647.03adf8"
            ]
        ]
    },
    {
        "id": "413a3a94.8ebe74",
        "type": "http request",
        "z": "24e62232.c43e9e",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DL6YK308/datachannels/Humidity/datapoints.csv",
        "tls": "",
        "x": 230,
        "y": 340,
        "wires": [
            [
                "d0f76647.03adf8",
                "d93dafcc.04f61"
            ]
        ]
    },
    {
        "id": "d93dafcc.04f61",
        "type": "http response",
        "z": "24e62232.c43e9e",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 410,
        "y": 260,
        "wires": []
    },
    {
        "id": "d0f76647.03adf8",
        "type": "debug",
        "z": "24e62232.c43e9e",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 430,
        "y": 340,
        "wires": []
    },
    {
        "id": "5ff9cae5.d8d134",
        "type": "function",
        "z": "24e62232.c43e9e",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"aiPA8TCGnwGWXCqD\"\n}\nreturn msg;",
        "outputs": "1",
        "noerr": 0,
        "x": 100,
        "y": 340,
        "wires": [
            [
                "413a3a94.8ebe74"
            ]
        ]
    }
]
