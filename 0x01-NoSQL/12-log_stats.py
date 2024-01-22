#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Display stats about Nginx logs stored in MongoDB.

    Args:
        mongo_collection: PyMongo collection object.

    Returns:
        None
    """
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check_count = mongo_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check_count} status check")
