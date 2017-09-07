#!/usr/bin/env python3

lloyd = {
"name": "Lloyd",
"fee": [float(123.53), 321, 50],
"address": "Wall Street"
}
tyler = {
"name": "Tyrell",
"fee": [150000, 1000000, 27472814],
"address": "Unknown"
}
elliot = {
"name": "Elliot",
"fee": [14313, 74837],
"address": "Unknown"
}
ecorp = [lloyd,tyler,elliot]

for ecorpers in ecorp:
	print(ecorpers["name"])
	print(ecorpers["fee"])
	print(ecorpers["address"])

