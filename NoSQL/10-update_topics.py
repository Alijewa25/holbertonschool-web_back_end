#!/usr/bin/env python3
""" Modul sənədləşdirməsi """


def update_topics(mongo_collection, name, topics):
    """ Funksiya sənədləşdirməsi """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
