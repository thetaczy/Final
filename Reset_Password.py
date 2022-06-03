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
        <username>
            <name>user1</name>
                <password>
                    <password>user123</password>
                </password>
        </username>
    </native>
</config>
"""
reply = m.edit_config(target="running", config=new_config)
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())


