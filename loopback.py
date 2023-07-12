from ncclient import manager
import xml.dom.minidom
m = manager.connect(
        host="192.168.1.6",
        port=830,
        username="cisco",
        password="cisco123!",
        hostkey_verify=False
        )
netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>1</name>
    <description>nueva loopback</description>
    <ip>
     <address>
      <primary>
       <address>1.1.1.1</address>
       <mask>255.255.255.255</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
