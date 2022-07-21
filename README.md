# opcua-modbustcp
OPC UA and Modbus TCP Clients and Servers in Python

<h2>serverOPCUA.py</h2> 
<p>
  This file is a simple OPC UA server with one variable that changes every 5 seconds to a number between 0 and 100. A simple example of how to implement an OPC UA server   in Python.
</p>
<h2>clientOPCUA.py</h2> 
<p>
  This file is a simple OPC UA client that connects with the server from the file cited above. A simple example of how to implement an OPC UA client in Python.
</p>
<h2>client_OPCUA_server_ModbusTCP_gateway.py</h2> 
<p>
  This file is a simple gateway to work as an interface between OPC UA servers and Modbus TCP clients. The data from OPC UA servers can be read by this OPC UA client and   this data will be written inside a Modbus TCP server. Finally, a Modbus TCP slient can read this data from the Modbus TCP server. This way, the data in an OPCUA server   can be acessed by a Modbus TCP client.
</p>
