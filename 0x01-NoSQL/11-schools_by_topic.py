#!/usr/bin/env python3
"""
11-schools_by_topic - Returns the list of schools having a specific topic
"""


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic: Topic to search.

    Returns:
        List of schools matching the specified topic.
    """
    filter_criteria = {'topics': topic}
    return list(mongo_collection.find(filter_criteria))
