import sys, os, getopt
from pysnmp.entity.engine import SnmpEngine
from pysnmp.hlapi import *
from pysnmp.hlapi.asyncio.cmdgen import getCmd
from pysnmp.hlapi.asyncio.transport import UdpTransportTarget
from pysnmp.hlapi.auth import CommunityData
from pysnmp.hlapi.context import ContextData
from pysnmp.smi.rfc1902 import ObjectType, ObjectIdentity

#TODO Ansible Facts
from pysnmp.hlapi import *

iterator = getCmd(
    SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('192.168.168.19', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.1.0'))
)

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:
    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
#Get command
# g = getCmd(SnmpEngine(),
#            CommunityData('zoom'),
#            UdpTransportTarget(('192.168.168.15', 161)),
#            ContextData(),
#            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
# errorIndication, errorStatus, errorIndex, varBinds = next(g)
# for varBind in varBinds:
#     print(' = '.join([x.prettyPrint() for x in varBind]))
#
#
# x = ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0), 'LocalHost')
#
# x[0].prettyPrint()

# g = getCmd(
#     SnmpEngine(), CommunityData('public'), UdpTransportTarget(
#         ('10.1.1.1', 161)), ContextData(), ObjectType(
#             ObjectIdentity('1.3.6.1.4.1.9.9.618.1.4.1.0')))
# errorIndication, errorStatus, errorIndex, varBinds = next(g)
# for varBind in varBinds:
#     print(' = '.join([x.prettyPrint() for x in varBind]))



# def get(target, oids, credentials, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
#     handler = hlapi.getCmd(
#         engine,
#         credentials,
#         hlapi.UdpTransportTarget((target, port)),
#         context,
#         *construct_object_types(oids)
#     )
#     return fetch(handler, 1)[0]