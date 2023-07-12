from ncclient import manager
import xml.dom.minidom
m = manager.connect(
        host="192.168.1.18",
        port=830,
        username="cisco",
        password="cisco123!",
        hostkey_verify=False
        )
netconf_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>Molina-Plaza-Hurtado-Ossa</hostname>
  </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
