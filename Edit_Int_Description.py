from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )


new_config = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <GigabitEthernet>
                <name>1</name>
                <description>This is New Description askaskasc</description>
            </GigabitEthernet>
        </interface>
    </native>
</config>
"""
reply = m.edit_config(target="running", config=new_config)
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())
