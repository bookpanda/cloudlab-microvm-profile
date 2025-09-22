import geni.portal as portal

request = portal.context.makeRequestRSpec()
# Here we assign constants that will be used later to describe our machines.
DEFAULT_NODE_HARDWARE_TYPE = "c6525-25g"
DEFAULT_DISK_IMAGE = (
    "urn:publicid:IDN+utah.cloudlab.us+image+faasnetworkstack-PG0:base-setup"
)
DEFAULT_LAN_SOCKET = "eth1"
lan = request.LAN()
# Here we say that we want to use 4 machines for our experiment. We give unique names to each of these machines. Then we assign them to variables so we can give more information later on the hardware, software, and network connections of each machine.
node_1 = request.RawPC("svr_1")
# Here we group our machines into lists so that we can give multiple machines the same specifications.
nodes = [node_1]
# Every machine we define in the "nodes" list will have the following characteristics:
for node in nodes:
    node.hardware_type = DEFAULT_NODE_HARDWARE_TYPE
    node.disk_image = DEFAULT_DISK_IMAGE
    s_iface = node.addInterface(DEFAULT_LAN_SOCKET)
    lan.addInterface(s_iface)
