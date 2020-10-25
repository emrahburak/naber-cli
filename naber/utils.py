

import dataset
import os
from stuf import stuf
from naber.storage import constant
from datetime import date


def multiline_content(number):
    if number < 3:
        number = 3
        print(f"Default lines 3")
        print(f'You have "3" lines')
    else:
        print(f'You have "{number}" lines')

    print(f'{constant.BColors.OKGREEN}Write your content. \
    {constant.BColors.ENDC}\n')
    counter = number
    lines = ""
    for i in range(number):
        lines += input('('+str(counter)+')'+" >> ")+"\n"
        counter = counter-1

    title = input(f'{constant.BColors.OKGREEN}Write your title.\
    {constant.BColors.ENDC}\n >> ')
    return title, lines



def to_storage(post):
    """ find db_path or create db connect to db and commit"""
    title, content = post
    root_dir = '.'
    for dir_name, subdirlist, filelist in os.walk(root_dir):
        #print(f'found directory {dir_name}')
        if dir_name == constant.DB_PATH:
            path = os.path.join(dir_name, constant.DB_NAME)

    db = dataset.connect(os.path.join(constant.DB_SQLITE, path), row_type=stuf)
    table = db[constant.DB_TABLE_POSTS]
    db.begin()
    try:
        table.insert(dict(title=title, content=content, created=date.today()))
        db.commit()
        print(f"{constant.BColors.OKBLUE}Comitted.{constant.BColors.ENDC}")
    except:
        db.rollback()
        



    
