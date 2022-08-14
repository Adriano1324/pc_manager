from pymongo import MongoClient


def get_db():
    CONNECTION_STRING = "mongodb://citizix:S3cret@mongo:27017/?authMechanism=DEFAULT"

    client = MongoClient(CONNECTION_STRING)

    return client["pc_manager"]
