"""
    Minim Internal testing Software
    Config Package for TestKit
"""
import configparser
import os.path
import subprocess
import sys
import paho.mqtt as mqtt
from . import utlis

logger = utlis.makeLogger('config')
devModeDeviceList = os.environ.get('ROOT_DIR', '~') + '/devModeDeviceList.ini'


def postData(msgs):
    """
    Pub multible messages in same session
    :param msgs: dict
        {
            'topic':   f'testkit/config/{DeNa}/var',
            'payload': config[DeNa]['name'],
            'retain':  True
        },
    """
    mqtt.publish.multiple(
            msgs,
            hostname=os.environ.get('AWSIP'),
            port=os.environ.get('AWSPORT')
            )


def edit_txtfile(file=devModeDeviceList, header=None):
    """
    Subprocess edit Project configuration file in notepad.

    ::returns:: Edit subprocess returncode
    """
    logger.info(f"{file} file opened. Please close to continue..")
    if header is not None:
        from . import utlis

        utlis.ensure_exists(file)
        with open(file, 'a+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(header.rstrip('\r\n') + '\n' + content)
    if os.supports_bytes_environ:
        subprocess.Popen(
                [os.environ.get('TESTKIT_EDITOR', "vim"), file]
                ).wait()
    else:
        subprocess.Popen(
                [os.environ.get('TESTKIT_EDITOR', "notepad"), file]
                ).wait()


def edit_config_option(DeNa, option, value):
    """
    Change an option in the projects.ini file
    :param DeNa: Device config to edit
    :param option: Option to edit
    :param value: New value of the option
    Example - edit_config_option(
    """
    config = configparser.ConfigParser()
    config.read(devModeDeviceList)
    config[DeNa][option] = value
    try:
        with open(devModeDeviceList, 'w') as configfile:
            config.write(configfile)
            logger.debug(f'Editted config file: {DeNa}, {option}, {value}')
    except configparser.Error as err:
        return err


def file_dialog():
    """
        Check and use Tkinter for file dialog, or call generate_default.

        ::returns:: filename
    """
    try:
        import tkinter
        from tkinter import filedialog

        options = {}
        options['defaultextension'] = '.ini'
        options['filetypes'] = [('ini config files', '.ini')]
        options['initialdir'] = os.environ['ROOT_DIR']
        options['initialfile'] = 'devModeDeviceList.ini'
        options['title'] = 'Select Device Configuration File'
        root = tkinter.Tk()
        filename = filedialog.askopenfilename(**options)
        root.destroy()
        return filename
    except ImportError:
        pass


def read_config_file():
    """
    Prompts user to select projects.ini configuration and returns contents as list
    Default file is ROOT_DIR+"\\devModeDeviceList.ini"

    :rtype: list
    """
    if os.path.isfile(devModeDeviceList):
        config_file = devModeDeviceList
    else:
        config_file = file_dialog()

    if config_file == '':
        sys.exit("No Config selected. Exiting..")
    elif not os.path.isfile(config_file):
        logger.critical("file (%s) not found. " % config_file)
        sys.exit("Exiting..")

    config = configparser.ConfigParser()
    try:
        config.read(config_file)
    except configparser.DuplicateSectionError as e:
        logger.debug('Duplicate Section Error\n' + str(e))
        edit_txtfile()
        logger.debug("config check..")
        read_config_file()
    except configparser.DuplicateOptionError as e:
        logger.debug('Duplicate Setup found in config, '
                     'Please locate the error in notepad \n' + str(e))
        edit_txtfile()
        logger.debug("Rerunning config check..")
        read_config_file()

    return config


class DeNa:
    """
    Retrieves and handles device config and system information
    """
    pass


def registerDevice(Name):
    """
    Adds Device name to agent pool stored as testkit/devicelist
    """
    _device = fetch_config()
    DeNa.deviceList = _device.fetchData('deviceList')

    if Name in DeNa.deviceList:
        logger.debug(f'Device registration confirmed using: {Name}')
    else:
        logger.debug(f'Registering as new device: {Name}')
        fetch_config.pubFullConfig(Name)

    # DeNa.deviceType = _device.fetchData('deviceType')
    # DeNa.testList = _device.fetchData('testList')
    # DeNa.status = _device.fetchData('status')
    # DeNa.force = _device.fetchData('force')


class fetch_config:
    """ Create's tuple object from given section [DeNa] """

    def __init__(self):
        self.isDev = os.environ.get('TESTKIT_DEVMODE', False)
        self.DeNa = os.environ.get('DeNa', os.environ.get('COMPUTERNAME'))
        self.deviceType = ''
        self.targetSSID = ''
        self.testList = ''
        self.status = 'Unset'
        self.force = False
        if self.isDev:
            self.fileConfig()
        else:
            self.mqttConfig()

    def fetchData(self, var):
        data = mqtt.subscribe.simple(
                f'testkit/config/{self.DeNa}/{var}',
                hostname=os.environ.get('AWSIP'),
                port=os.environ.get('AWSPORT'),
                keepalive=1)
        return str(data.payload)

    def mqttConfig(self):
        self.DeNa = self.fetchData('DeNa')
        self.deviceType = self.fetchData('deviceType')
        self.targetSSID = self.fetchData('targetSSID')
        self.testList = self.fetchData('testlist')
        self.status = self.fetchData('status')
        self.force = self.fetchData('force')
        return self

    def fileConfig(self):
        config = configparser.ConfigParser()
        config.read(devModeDeviceList)
        self.DeNa = config[self.DeNa]['DeNa']
        self.deviceType = config[self.DeNa]['deviceType']
        self.targetSSID = config[self.DeNa]['targetSSID']
        self.testList = config[self.DeNa]['testList']
        self.status = config[self.DeNa]['status']
        self.force = config[self.DeNa]['force']
        return self

    def pubFullConfig(self):
        postData([
                {
                        'topic':   f'teskit/{self.DeNa}/DeNa',
                        'payload': self.DeNa,
                        'retain':  True
                        },
                {
                        'topic':   f'teskit/{self.DeNa}/deviceType',
                        'payload': self.deviceType,
                        'retain':  True
                        },
                {
                        'topic':   f'teskit/{self.DeNa}/targetSSID',
                        'payload': self.targetSSID,
                        'retain':  True
                        },
                {
                        'topic':   f'teskit/{self.DeNa}/testList',
                        'payload': self.testList,
                        'retain':  True
                        },
                {
                        'topic':   f'teskit/{self.DeNa}/status',
                        'payload': self.status,
                        'retain':  True
                        },
                {
                        'topic':   f'teskit/{self.DeNa}/force',
                        'payload': self.force,
                        'retain':  True
                        }
                ])
