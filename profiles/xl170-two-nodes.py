import geni.portal as portal
import geni.rspec.pg as pg

pc = portal.Context()
request = portal.context.makeRequestRSpec()
# Here we assign constants that will be used later to describe our machines.
DEFAULT_NODE_HARDWARE_TYPE = "xl170"
DEFAULT_DISK_IMAGE = (
    "urn:publicid:IDN+utah.cloudlab.us+image+faasnetworkstack-PG0:baseNodeV4"
)
DEFAULT_LAN_SOCKET = "eth1"
lan = request.LAN()
# Here we say that we want to use 4 machines for our experiment. We give unique names to each of these machines. Then we assign them to variables so we can give more information later on the hardware, software, and network connections of each machine.
node_1 = request.RawPC("node_1")
node_2 = request.RawPC("node_2")
# Here we group our machines into lists so that we can give multiple machines the same specifications.
nodes = [node_1, node_2]
# Every machine we define in the "nodes" list will have the following characteristics:
for node in nodes:
    node.hardware_type = DEFAULT_NODE_HARDWARE_TYPE
    node.disk_image = DEFAULT_DISK_IMAGE
    node.addService(pg.Execute(shell="sh", command="/local/repository/init.sh"))
    s_iface = node.addInterface(DEFAULT_LAN_SOCKET)
    lan.addInterface(s_iface)

pc.printRequestRSpec(request)
