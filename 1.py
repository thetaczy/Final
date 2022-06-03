import xml.dom.minidom
from ncclient import manager




m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )
    
netconf_reply = m.get_config(source="running")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())





















'''
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <hostname></hostname>
            <username></username>
            <interface>
                
            </interface>
    </native>
</filter>
"""


netconf_reply = m.get_config(source="running", filter=netconf_filter)

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
'''
