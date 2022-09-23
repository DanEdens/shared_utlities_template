import os
import argparse
from TestKit import devices
import paho.mqtt.client as paho


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

parser.add_argument('-t', '--test',
                    default=os.environ.get("testkit_test", 'all'),
                    choices=devices.testList,
                    help='Only output data for given group')


args = parser.parse_args()
outStyle = args.output


client = paho.Client(args.user, clean_session=True)

client.connect(args.address, int(args.port))
