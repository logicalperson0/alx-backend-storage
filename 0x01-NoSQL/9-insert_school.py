#!/usr/bin/env python3
"""
Module that has a Python function which lists all documents in a collection
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based
    on kwargs"""
    if mongo_collection is None:
        return []
    create_id = mongo_collection.insert_one(kwargs)
    return create_id.inserted_id