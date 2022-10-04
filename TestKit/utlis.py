"""
    Minim Internal testing Software
    Utilities Package for TestKit
"""
import datetime
import errno
import logging
import os
from pathlib import Path

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

client = mqtt.Client(os.environ.get('TESTKIT_DENA', os.environ.get('USERPROFILE')))
hostname = os.environ.get('AWSIP', 'localhost')
port = int(os.environ.get('AWSPORT', 3001))
client.connect(hostname, port)
logger = logging.getLogger('utlis')
os.environ['ROOT_DIR'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..' )
fileDate = datetime.datetime.now().strftime("%Y-%m-%d")


def makeLogger(name) -> object:
    """
    Create the project wide logger.
    Sets Output level from Argument flags and if output should be directed
    to a log file.
    Default location is data//FILEDATE//TestKit.log
    :param name:
    :return: Logger
    :rtype: Object
    """
    if os.environ.get('TESTKIT_DEBUG', False):
        _format: str = '%(asctime)s - %(module)s - %(message)s'
    else:
        _format: str = '%(asctime)s - %(message)s'

    log = logging.getLogger(name)

    if os.environ.get('TESTKIT_LOG', True):
        _log = ensureExists(
                Path(os.environ['ROOT_DIR']).joinpath(
                        f"data//{fileDate}//TestKit.log"
                        ))
        with open(_log, 'a') as file:
            file.write(
                    f'\nRun Log for {fileDate}\n=============================\n')
        logging.basicConfig(filename=_log, level=None, format=_format)
    else:
        logging.basicConfig(level=None, format=_format)

    if os.environ.get('TESTKIT_DEBUG', False):
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)

    myHandler = mqttHandler(topic=f'testkit/{name}')
    log.addHandler(myHandler)
    return log


def removeFile(*args):
    """
    Removes Old copy of **file** is file exists
    :return: none
    """
    for file in args:
        try:
            os.remove(file)
            logger.debug(f'Removing previous copy of {file}.. ')
        except OSError:
            pass


def linePrepender(filename, line):
    """
    Prepends data for
    :param filename:
    :param line:
    :return:
    """
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def ensureExists(path):
    """
    Accepts path to file, then creates the directory path if it does not exist
    :param path:
    :return:
    """
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    return path


class mqttHandler(logging.Handler):
    """
    A handler class which writes logging records, appropriately formatted,
    to a MQTT server to a topic.
    """

    def __init__(
            self,
            _hostName=hostname,
            topic='testkit/log',
            qos=0, retain=True,
            _port=port,
            client_id='',
            keepalive=60,
            will=None,
            auth=None,
            tls=None,
            protocol=3,
            transport='tcp'):
        logging.Handler.__init__(self)
        self.topic = topic
        self.qos = qos
        self.retain = retain
        self.hostname = _hostName
        self.port = _port
        self.client_id = client_id
        self.keepalive = keepalive
        self.will = will
        self.auth = auth
        self.tls = tls
        self.protocol = protocol
        self.transport = transport

    def emit(self, record):
        """
        Publish a single formatted logging record to a broker, then disconnect
        cleanly.
        """
        msg = self.format(record)
        publish.single(
                self.topic, msg, self.qos, self.retain,
                hostname=self.hostname, port=self.port,
                client_id=self.client_id,
                keepalive=self.keepalive,
                will=self.will, auth=self.auth, tls=self.tls,
                protocol=self.protocol, transport=self.transport)


def post(topic, payload, retain=False):
    """
    Post results to MQTT broker for processing
    :param retain: 
    :param topic: Project name
    :param payload: Sensor Data
    """
    topic = str(f'testkit/{topic}')
    payload = str(payload)
    try:
        client.publish(topic, payload, retain)
    except ValueError:
        logger.info(
                f"pub Failed because of wildcard: {str(topic)}=:={str(payload)}")
        logger.info(f"Attempting fix...")
        try:
            tame_t = topic.replace("+", "_")
            tame_topic = tame_t.replace("#", "_")
            tame_p = payload.replace("+", "_")
            tame_payload = tame_p.replace("#", "_")
            logger.info("Fix successful, Sending data...")
            client.publish(str(tame_topic), str(tame_payload), retain)
        except Exception as error:
            logger.info(f"Fix Failed. Bug report sent.")
            client.publish("testkit/error", str(error), qos=1, retain=True)
