import nxostoolkit

nexus1 = nxostoolkit.Nexus()

print(nexus1.version)
print(nexus1.platform)
print(nexus1.authenticate())
print(nexus1.get_interface_status("vlan101"))
