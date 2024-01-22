#!/usr/bin/env python3
"""
9-insert_school - Inserts a new document into a MongoDB collection
"""


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: Keyword arguments representing the document fields.

    Returns:
        The new _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id


