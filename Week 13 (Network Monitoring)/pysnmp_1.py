from pysnmp.hlapi import *

system_up_tim_oid = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0'))
cisco_contact_info_oid = ObjectType(ObjectIdentity('1.3.6.1.4.1.9.2.1.61.0'))

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('192.168.188.139', 161)),
        ContextData(),
        system_up_tim_oid,
        cisco_contact_info_oid
    )
)

# Check for errors and display the results
if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (
        errorStatus.prettyPrint(),
        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'
    ))
else:
    for varBind in varBinds:
        print('%s = %s' % (varBind[0].prettyPrint(), varBind[1].prettyPrint()))
