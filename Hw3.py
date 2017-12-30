[
    {
        "id": "d4b6ee1d.170a7",
        "type": "inject",
        "z": "b7d8f72c.686438",
        "name": "node",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 90,
        "y": 120,
        "wires": [
            [
                "ab341505.6a5438",
                "1721ea9c.ccd4a5"
            ]
        ]
    },
    {
        "id": "ab341505.6a5438",
        "type": "function",
        "z": "b7d8f72c.686438",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"aiPA8TCGnwGWXCqD\"\n    };\n    \nmsg.payload= \"Temperature,,26\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 80,
        "y": 220,
        "wires": [
            [
                "fd1a5159.84226"
            ]
        ]
    },
    {
        "id": "1721ea9c.ccd4a5",
        "type": "function",
        "z": "b7d8f72c.686438",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"aiPA8TCGnwGWXCqD\"\n    };\n    \nmsg.payload= \"Humidity,,43.5\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 80,
        "y": 280,
        "wires": [
            [
                "a4ebe717.96a2a8"
            ]
        ]
    },
    {
        "id": "fd1a5159.84226",
        "type": "http request",
        "z": "b7d8f72c.686438",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/DL6YK308/datapoints.csv",
        "tls": "",
        "x": 210,
        "y": 220,
        "wires": [
            [
                "e8068de.3877e7",
                "abe5e390.c1391"
            ]
        ]
    },
    {
        "id": "a4ebe717.96a2a8",
        "type": "http request",
        "z": "b7d8f72c.686438",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/DL6YK308/datapoints.csv",
        "tls": "",
        "x": 210,
        "y": 280,
        "wires": [
            [
                "e8068de.3877e7",
                "abe5e390.c1391"
            ]
        ]
    },
    {
        "id": "e8068de.3877e7",
        "type": "http response",
        "z": "b7d8f72c.686438",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 390,
        "y": 220,
        "wires": []
    },
    {
        "id": "abe5e390.c1391",
        "type": "debug",
        "z": "b7d8f72c.686438",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 410,
        "y": 280,
        "wires": []
    }
]
