#!/usr/bin/env python3
"""A Python script that provides some stats
about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client["logs"]
    col = db["nginx"]

    logsCount = col.count_documents({})

    print(f"{logCount} logs\nMethods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for items in methods:
        methodCount = col.count_documents({"method": method})
        print(f'\tmethod {method}: {methodCount}')

    getStatusCount = col.count_documents({'method': 'GET',
                                          'path': '/status'})

    print(f"{getStatusCount} status check")
