from pymongo import MongoClient
client = MongoClient()

db = client['ip_database']
collection = db['current_collection']

ip_data = []

with open("ips.data", "r") as file:
	for line in file:
		currentline = line.split(",")
		info = {
			"ip" : currentline[0],
			"hostname" : currentline[1],
			"data" : currentline[2],
			"value" : currentline[3],
			"version" : currentline[4]
		}
		ip_data.append(info)

result = collection.insert_many(ip_data)
print("Inserted these ids: ")
print(result.inserted_ids)
		
		
