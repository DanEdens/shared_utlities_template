import logging
import os
import subprocess
import sys

from TestKit.config import fetch_config

logger = logging.getLogger('testkit')

varlist = [
        'DeNa'
        ]

commands = [
        'pullDeviceList',
        'start-server'
        ]


def script(filename):
    """
    Runs a script on the local device
    This is a security precaution to limit available commands
    """
    _path = os.environ['bin'] + f'\\{filename}.cmd'
    if filename in commands:
        subprocess.Popen(r'%s' % _path, shell=True)


def parseMessage(msg):
    key = msg.split('/')
    value = key[2].split(' ')
    if value[0] in commands:
        try:
            script(value[0])
        except:
            pass
        print(f"Running Command {value[0]}: {value[1]}")
    if value[0] in varlist:
        # Since all values are checked when called,
        # Value changes only need to be logged, not saved
        print(f"{value[0]} set to: {value[1]}")


if __name__ == "__main__":
    DeNa = fetch_config()
    parseMessage(sys.argv[1])
