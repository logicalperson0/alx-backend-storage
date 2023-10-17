#!/usr/bin/env python3
"""
Module that has a Python function which changes all topics of a school
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a school document based on the
    name"""
    if mongo_collection is None:
        return []
    naming = { "name": name }
    topicing = { "$set": { "topics": topics  } }
    update_id = mongo_collection.update_many(naming, topicing)
    
    return update_id