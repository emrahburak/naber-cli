
import dataset
import os
from stuf import stuf
from naber import constant
from datetime import date
from naber import utils


def create_storage():
    """ Crate Db on root dir and connect to db"""
    for dir_name, subdirlist, filelist in os.walk(constant.ROOT_DIR):
       #print(f'found directory {dir_name}')
       if dir_name == constant.ROOT_DIR:
           path = os.path.join(dir_name, constant.DB_NAME)
           return dataset.connect(os.path.join(constant.DB_SQLITE, path), row_type=stuf)



def to_storage(post):
    """ find db path connect and commit"""
    with create_storage() as db:
        title, content = post
        db[constant.DB_TABLE_POSTS].insert(dict(title=title, content=content, created=date.today()))
    
        return utils.color_blue_status('Comitted')
        

def get_storage(limit):
    with create_storage() as db:
        query = db[constant.DB_TABLE_POSTS].find(order_by=['-created',
                                                           '-id'],
                                                 _limit=limit)
        print(utils.color_green_info('Result...'))

        for row in query:
            print(' >> ',row.title ,'\t', row.created)
        return utils.color_blue_status(f'Last {limit} '
                                           + utils.is_plural(limit,'row'))
