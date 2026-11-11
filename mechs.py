import random
possibleContents = {
        "Basic Sword": {
            "cost":5,
            "type":"weapon",
            "power":15,
            "maxQuant":1
        },
        "Apple": {
            "cost":5,
            "type":"food",
            "power":10,
            "maxQuant":5
        },
        "Bow": {
            "cost":2,
            "type":"weapon",
            "power":[8,25],
            "needs":"Arrow",
            "maxQuant":1
        },
        "Arrow": {
            "cost":3,
            "type":"commodity",
            "power":0,
            "maxQuant":15

        }
    }

