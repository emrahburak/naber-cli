#!/usr/bin/env python3

import click
import sys
from naber import utils
from naber import models
from naber import constant

 
class Config():

    def __init__(self):
        self.verbose = False


    def myfunction(self):
        print("--test my function")




pass_config = click.make_pass_decorator(Config, ensure=True)
   
@click.group()
@click.option('--verbose', is_flag=True)
@pass_config
def cli(config, verbose):
    config.verbose = verbose
    pass


@click.command()
@click.argument('out', type=click.File('w'), default='-',
                required=False)
def initdb(out):
    """ This scripts create your database """
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')


@click.command()
@click.option('--limit', default=3, help="number of row")
@click.argument('read', type=click.File('r'), default='-',
                required=False)
@pass_config
def read(config,limit, read):
    "read your posts"
    if config.verbose:
        click.echo("we are in verbose mode ",)
        config.myfunction()
    result = models.get_storage(limit)
    click.echo(result)



@click.command()
@click.option('--line', default=3, help='number of lines')
def post(line):
    "post your message"

    post = utils.multiline_content(line)
    commit = models.to_storage(post)
    click.echo(commit)
    pass
   


@click.command()
@click.option('-c','--count', default=1, help='number of greetings')
@click.option('-s','--string', default='you', help='write your name')
@click.argument('out', type=click.File('w'), default='-',
                required=False)
#@click.argument('')
def hello(count, string, out):
    """ This scripts greets you """
       
    for x in range(count):
        click.echo(utils.color_green_info(f'Hello {string}'),
                   file=out )
    


#cli.add_command(initdb)
#cli.add_command(dropdb)
cli.add_command(hello)
cli.add_command(read)
cli.add_command(post)





