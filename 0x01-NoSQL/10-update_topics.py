#!/usr/bin/env python3
"""
10-update_topics - Changes all topics of a school document based on the name
"""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object.
        name: Name of the school to update.
        topics: List of strings representing the new topics.

    Returns:
        None
    """
    filter_criteria = {'name': name}
    update_data = {'$set': {'topics': topics}}
    mongo_collection.update_many(filter_criteria, update_data)
