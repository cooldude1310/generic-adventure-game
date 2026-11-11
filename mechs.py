import random
possibleContents = {
        "Basic Sword": {
            "cost":2,
            "type":"weapon",
            "power":15,
            "maxQuant":1
        },
        "Apple": {
            "cost":2,
            "type":"food",
            "power":10,
            "maxQuant":5
        },
        "Bow": {
            "cost":8,
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


def genContents(inventory):
    points = random.randint(5,8)
    newInventory = inventory
    while points >= 2:
        item = random.choice(list(possibleContents))
        if item in newInventory and newInventory[item["quant"]] < item["maxQuant"]:
            newInventory[item["quant"]] += 1
        elif not item in newInventory:
            newInventory[item["type"]] = item["type"]
            newInventory[item["power"]] = item["power"]
            newInventory[item["quantity"]] = 1
    newInventory["Gold"] += points
    return newInventory

print(genContents({
    "Gold":1
}))           
    
