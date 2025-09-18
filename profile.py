import geni.portal as portal

request = portal.context.makeRequestRSpec()
# Here we assign constants that will be used later to describe our machines.
DEFAULT_SVR_HARDWARE_TYPE = "m510"
DEFAULT_CLI_HARDWARE_TYPE = "d6515"
DEFAULT_DISK_IMAGE = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
DEFAULT_LAN_SOCKET = "eth1"
lan = request.LAN()
# Here we say that we want to use 4 machines for our experiment. We give unique names to each of these machines. Then we assign them to variables so we can give more information later on the hardware, software, and network connections of each machine.
svr_1 = request.RawPC("svr_1")
svr_2 = request.RawPC("svr_2")
svr_3 = request.RawPC("svr_3")
cli_1 = request.RawPC("cli_1")
# Here we group our machines into lists so that we can give multiple machines the same specifications.
svrs = [svr_1, svr_2, svr_3]
clis = [cli_1]
# Every machine we define in the "svrs" list will have the following characteristics:
# 1. Each machine will be an m510. You can check http://docs.cloudlab.us/hardware.html to see what computers are available in Cloudlab
# 2. Each machine will come loaded with Ubuntu 18.04 created by the Cloudlab team.
# 3. Each machine will have a connection to a LAN interface.
for svr in svrs:
    svr.hardware_type = DEFAULT_SVR_HARDWARE_TYPE
    svr.disk_image = DEFAULT_DISK_IMAGE
    s_iface = svr.addInterface(DEFAULT_LAN_SOCKET)
    lan.addInterface(s_iface)
# Similar for clients.
for cli in clis:
    cli.hardware_type = DEFAULT_CLI_HARDWARE_TYPE
    cli.disk_image = DEFAULT_DISK_IMAGE
    c_iface = cli.addInterface(DEFAULT_LAN_SOCKET)
    lan.addInterface(c_iface)
    portal.context.printRequestRSpec(request)
