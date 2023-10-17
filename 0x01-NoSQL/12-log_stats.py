#!/usr/bin/env python3
"""
Module that has a Python function which provides some stats about Nginx logs
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')

    logs_stats = client.logs.nginx
    
    cou_doc = logs_stats.count_documents({})
    get_doc = logs_stats.count_documents({ "method": "GET" })
    post_doc = logs_stats.count_documents( {"method": "POST"} )
    put_doc = logs_stats.count_documents( { "method": "PUT" } )
    patch_doc = logs_stats.count_documents( { "method": "PATCH" } )
    del_doc = logs_stats.count_documents( { "method": "DELETE" } )
    status_doc = logs_stats.count_documents( { "path": "/status" } )

    print('{} logs'.format(cou_doc))
    print("Methods:")
    print('\tmethod GET: {}'.format(get_doc))
    print('\tmethod POST: {}'.format(post_doc))
    print('\tmethod PUT: {}'.format(put_doc))
    print('\tmethod PATCH: {}'.format(patch_doc))
    print('\tmethod DELETE: {}'.format(del_doc))
    print('{} status check'.format(status_doc))