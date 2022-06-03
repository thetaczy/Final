from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )


new_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <GigabitEthernet>
                <description></description>
            </GigabitEthernet>
        </interface>
    </native>
</filter>
"""
reply = m.get_config(source="running", filter=new_filter)
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())


