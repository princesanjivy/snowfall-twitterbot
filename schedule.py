from apscheduler.schedulers.blocking import BlockingScheduler
import twitter, os, json, pymongo

with open("cred.json", "r") as f:
	cred = json.loads(f.read())

api = twitter.Api(cred.get("CONSUMER_KEY"),
				cred.get("CONSUMER_SECRET"),
				cred.get("ACCESS_TOKEN_KEY"),
				cred.get("ACCESS_TOKEN_SECRET"))



url = 'mongodb+srv://prince:qwerty12345@snow-princebot-lgc4v.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(url)

db = client["id"]
collection = db["since_id"]

collection.insert({"_id": 0, "since_id": 1234567890})