from pysnmp.hlapi.asyncio.cmdgen import nextCmd
from pysnmp.hlapi.asyncio.transport import UdpTransportTarget
from pysnmp.hlapi.auth import CommunityData
from pysnmp.hlapi.v1arch import *
from pysnmp.smi.rfc1902 import ObjectType, ObjectIdentity


class SnmpDispatcher(object):
    pass


iterator = nextCmd(
    SnmpDispatcher(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('192.168.100.1', 161)),
    ObjectType(ObjectIdentity('IF-MIB', 'ifDescr')),
    ObjectType(ObjectIdentity('IF-MIB', 'ifType')),
    ObjectType(ObjectIdentity('IF-MIB', 'ifMtu')),
    ObjectType(ObjectIdentity('IF-MIB', 'ifSpeed')),
    ObjectType(ObjectIdentity('IF-MIB', 'ifPhysAddress')),
    ObjectType(ObjectIdentity('IF-MIB', 'ifType')),
    lookupMib=True,
    lexicographicMode=False
)

for errorIndication, errorStatus, errorIndex, varBinds in iterator:

    if errorIndication:
        print(errorIndication)
        break

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
        break

    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))