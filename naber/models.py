
import dataset
import os
from pathlib import Path
from stuf import stuf
from naber import constant
from datetime import date
from naber import utils


def create_storage():
    """ Crate Db on constant.ROOT_DIR dir and connect to db"""
    with Path.home() as home_dir:
        path_create = os.path.join(home_dir
                          ,constant.ROOT_DIR
                          ,constant.NABER_DIR)
        path_db = utils.path_creator(path_create)

        return dataset.connect(constant.DB_SQLITE
                               + os.path.join(path_db
                                              ,constant.DB_NAME),
                               row_type=stuf)

        
def to_storage(post):
    """ find db path connect and commit"""
    with create_storage() as db:
        title, content = post
        db[constant.DB_TABLE_POSTS].insert(dict(title=title, content=content, created=date.today()))
    
        return utils.color_blue_status(constant.COMMIT)
        

def get_storage(limit):
    with create_storage() as db:
        query = db[constant.DB_TABLE_POSTS].find(order_by=['-created',
                                                           '-id'],
                                                 _limit=limit)
        print(utils.color_green_info(constant.RESULT))

        for row in query:
            print(' >> ',utils.minimalize_string(row.title)
                  ,'\t', row.created)
        return utils.color_blue_status(f'Last {limit} '
                                           + utils.is_plural(limit,'row'))
