[
    {
        "id": "330b82c6.84740e",
        "type": "rpi-gpio in",
        "z": "97fb5cc6.7180a",
        "name": "button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 70,
        "y": 60,
        "wires": [
            [
                "d4c1431a.39afd"
            ]
        ]
    },
    {
        "id": "2a3ffa8d.28fe96",
        "type": "rpi-gpio out",
        "z": "97fb5cc6.7180a",
        "name": "LED",
        "pin": "11",
        "set": true,
        "level": "1",
        "freq": "",
        "out": "out",
        "x": 430,
        "y": 140,
        "wires": []
    },
    {
        "id": "4c6ed8f7.293078",
        "type": "debug",
        "z": "97fb5cc6.7180a",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 450,
        "y": 220,
        "wires": []
    },
    {
        "id": "d4c1431a.39afd",
        "type": "switch",
        "z": "97fb5cc6.7180a",
        "name": "if button is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 90,
        "y": 180,
        "wires": [
            [
                "e397bd40.1f5d3"
            ],
            [
                "e2ea346b.c38bc8"
            ]
        ]
    },
    {
        "id": "e397bd40.1f5d3",
        "type": "change",
        "z": "97fb5cc6.7180a",
        "name": "change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 250,
        "y": 140,
        "wires": [
            [
                "4c6ed8f7.293078",
                "2a3ffa8d.28fe96"
            ]
        ]
    },
    {
        "id": "e2ea346b.c38bc8",
        "type": "change",
        "z": "97fb5cc6.7180a",
        "name": "change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 250,
        "y": 220,
        "wires": [
            [
                "4c6ed8f7.293078",
                "2a3ffa8d.28fe96"
            ]
        ]
    }
]
