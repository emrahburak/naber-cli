

import dataset
import os
from stuf import stuf
from naber.storage import constant
from datetime import date


def multiline_content(number):
    if number < 3:
        number = 3
        print(f"Default lines 3")
        print(f'You have 3 lines')
    else:
        print(f'You have {number} lines')

    print('Write your message\n')
    counter = number
    lines = ""
    for i in range(number):
        lines += input('('+str(counter)+')'+" >> ")+"\n"
        counter = counter-1

    title = input("Write your title : ")
    return title, lines



def to_storage(post):
    """ find db_path or create db connect to db and commit"""
    title, content = post
    root_dir = '.'
    for dir_name, subdirlist, filelist in os.walk(root_dir):
        #print(f'found directory {dir_name}')
        if dir_name == constant.DB_PATH:
            db_path = os.path.join(dir_name, 'mydatabase.db')

    db = dataset.connect('sqlite:///'+db_path, row_type=stuf)
    table = db[constant.TABLE]
    db.begin()
    try:
        table.insert(dict(title=title, content=content, created=date.today()))
        db.commit()
    except:
        db.rollback()
        



    
