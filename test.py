import asyncio
from pysnmp.hlapi.v3arch.asyncio import *
async def run():
    # Define SNMP target details
    snmp_target = ('192.168.188.141', 161)
    community_string = 'public'

    print("\nStarting SNMP GET request...")

    # Perform an asynchronous SNMP GET request for multiple OIDs
    errorIndication, errorStatus, errorIndex, varBinds = await getCmd(
        SnmpEngine(), # SnmpEngine is the main object that drives the whole SNMP engine
        CommunityData(community_string), # CommunityData is used to specify the SNMPv1/v2c community string
        await UdpTransportTarget.create(snmp_target), # UdpTransportTarget is used to specify the target SNMP agent
        ContextData(), # ContextData is used to specify the SNMPv3 contextEngineId and contextName
        # Adding multiple OIDs to query
        ObjectType(ObjectIdentity('1.3.6.1.2.1.31.1.1.1.1.1')), # OID 1: Interface name
        ObjectType(ObjectIdentity('1.3.6.1.2.1.31.1.1.1.1.2')), # OID 2: Interface name
        ObjectType(ObjectIdentity('1.3.6.1.2.1.31.1.1.1.1.3')), # OID 3: Interface name
        ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0')), # OID 4: SysUpTime
        ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0')), # OID 5: SysName
        ObjectType(ObjectIdentity('1.3.6.1.2.1.11.13.0')) # OID 6: SnmpInPkts
    )
    
    # Handle errors and display the result
    if errorIndication:
        print(f"Error Indication: {errorIndication}")
        return  # Exit if there is an error indication
    elif errorStatus:
        print(f"Error Status: {errorStatus.prettyPrint()} at {errorIndex}")
        return  # Exit if there is an error status

    else:
        for name, value in varBinds: 
            print('%s = %s' % (name.prettyPrint(), value.prettyPrint()), type(value)) 
        
    print("SNMP GET request completed.\n")

# Run the asynchronous SNMP GET request
asyncio.run(run())
