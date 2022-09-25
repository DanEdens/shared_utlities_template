"""
    Minim Internal testing Software
    Main Package for TestKit
"""
import os
import subprocess
import sys

from TestKit.utlis import makeLogger
from . import __init__ as thread
from TestKit.config import fetch_config

logger = makeLogger('testkit')

# Variable WatchList to be logged by the Server
varlist = [
        'DeNa'
        ]

# List of commands available to the Server
commands = [
        'pullDeviceList',
        'start-server'
        ]


def script(filename):
    """
    Runs .bin scripts as subprocesses
    """
    _path = os.environ['bin'] + f'\\{filename}.cmd'
    if filename in commands:
        subprocess.Popen(r'%s' % _path, shell=True)


def parseMessage(msg):
    """
    Handles message payload and logs events
    Scripts in .bin must be hardcoded into the command list above
    :param msg:
    """
    key = msg.split('/')
    value = key[2].split(' ')
    if value[0] in commands:
        try:
            # Log script invocations
            logger.info(f"Running Command {value[0]}: {value[1]}")
            script(value[0])
        except:
            pass
    if value[0] in varlist:
        # Log variable changes
        logger.info(f"{value[0]} set to: {value[1]}")


if __name__ == "__main__":
    """
        Main Thread 
    """
    logger.debug(thread.args)

    if thread.args.server:
        print(sys.argv)
        # parseMessage(sys.argv[2])
    elif thread.args.make_docs:
        print('Failed')
    elif thread.args.post_docs:
        print('Failed')
    elif thread.args.device:

        DeNa = fetch_config()
    elif thread.args.test:
        print('Failed')