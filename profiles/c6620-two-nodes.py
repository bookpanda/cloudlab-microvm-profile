import geni.portal as portal
import geni.rspec.pg as pg

pc = portal.Context()
request = pc.makeRequestRSpec()

node1 = request.RawPC("node1")
node2 = request.RawPC("node2")

for node in [node1, node2]:
    node.hardware_type = "c6620"
    node.disk_image = (
        "urn:publicid:IDN+utah.cloudlab.us+image+faasnetworkstack-PG0:baseNodeV4"
    )

# Request the 100G NICs
iface1 = node1.addInterface("eth100g")
iface1.component_id = "urn:publicid:IDN+utah.cloudlab.us+interface+eth100g"

iface2 = node2.addInterface("eth100g")
iface2.component_id = "urn:publicid:IDN+utah.cloudlab.us+interface+eth100g"

# Explicitly connect them
link = request.Link("p2p100g")
link.addInterface(iface1)
link.addInterface(iface2)

pc.printRequestRSpec(request)
