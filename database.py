import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["AutoTrading_bot"]

class Status():
    def save_status(collection, status, time):
        collection = db[collection]
        data = collection.remove({})
        new_stat = {"Status":status, "Time":time}
        data = collection.insert(new_stat)
        return data

    def find_status(collection):
        collection = db[collection]
        data = collection.find({})
        for dt in data:
            stat = dt["Status"]
        return stat

class Signals():

    def add(collection, ticker, volume):
        collection = db[collection]
        new_signal = {"Ticker":ticker, "Volume":volume }
        data = collection.insert(new_signal)
        return data

    def find_all(collection):
        tickers = {}
        collection = db[collection]
        data = collection.find({})
        for dt in data:
            tickers[dt["Ticker"]] = dt["Volume"]
        return tickers

    def clear_all(collection):
        collection = db[collection]
        collection.remove({})
