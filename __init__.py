import argparse
import os
import sys
from TestKit import devices

os.environ['ROOT_DIR'] = os.path.dirname(os.path.abspath(__file__))
os.environ['bin'] = os.path.join(os.environ['ROOT_DIR'], '.bin')
sys.path.insert(0, os.environ['ROOT_DIR'])
sys.path.insert(1, os.environ['bin'])

parser = argparse.ArgumentParser(
        description="Command and Control hub for Test automation. ",
        prog='MinimTestKit',
        formatter_class=argparse.RawDescriptionHelpFormatter
        )

parser.add_argument('-v', '--debug', action='store_true',
                    default=os.environ.get("testkit_debug", False),
                    help='Print debug information to terminal')

parser.add_argument('--make-docs', action='store_true',
                    default=os.environ.get("testkit_make_docs", False),
                    help='Build Docs locally')

parser.add_argument('--post-docs', action='store_true',
                    default=os.environ.get("testkit_make_docs", False),
                    help='Update Docs to Confluence')

parser.add_argument('-d', '--device',
                    default=os.environ.get("testkit_device", 'all'),
                    choices=devices.deviceList,
                    help='Only output data for given group')

parser.add_argument('--server', action='store_true',
                    default=os.environ.get("testkit_server", False),
                    help='')

parser.add_argument('-t', '--test',
                    default=os.environ.get("testkit_test", 'all'),
                    choices=devices.testList,
                    help='Only output data for given group')

args = parser.parse_args()
print(args)
