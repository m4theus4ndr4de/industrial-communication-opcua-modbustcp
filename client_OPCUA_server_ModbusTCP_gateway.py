from opcua import Client
from pyModbusTCP.server import ModbusServer
from time import sleep

# class created using a OPC UA client and a Modbus TCP server to act as an interface between a Modbus TCP client and a OPC UA server
class OPCUA_Client_ModbusTCP_Server():

    # init method for the class containing both OPC UA client and Modbus TCP server objects
    def __init__(self, url_OPCUA, ip_ModbusTCP, port_ModbusTCP):

        self.url_OPCUA = url_OPCUA
        self.client_OPCUA = Client(self.url_OPCUA)
        # variable1 is a variable created to act as data from a sensor and only needs to be read
        self.variable1_OPCUA = self.client_OPCUA.get_node("ns=2;i=2")
        # variable2 is a variable created to act as data from an actuator and needs to be read and written
        self.variable2_OPCUA = self.client_OPCUA.get_node("ns=2;i=3")

        self.server_ModbusTCP = ModbusServer(host=ip_ModbusTCP, port=port_ModbusTCP, no_block=True)
        self.database_ModbusTCP = self.server_ModbusTCP.data_bank
        self.ip_ModbusTCP = ip_ModbusTCP
        self.port_ModbusTCP = port_ModbusTCP

    def run(self):

        try:

            # initializing the client and the server
            self.client_OPCUA.connect()
            print("Client OPC UA Connected to {}".format(self.url_OPCUA))

            self.server_ModbusTCP.start()
            print("Server MODBUS TCP Online at {}".format(self.ip_ModbusTCP))

            while True:

                variable1_OPCUA = self.variable1_OPCUA.get_value()
                self.database_ModbusTCP.set_input_registers(1, [variable1_OPCUA])
                variable1_ModbusTCP = self.database_ModbusTCP.get_input_registers(1)
                print("variable1 ModbusTCP = {}".format(variable1_ModbusTCP))

                variable2_OPCUA = self.variable2_OPCUA.get_value()
                self.database_ModbusTCP.set_input_registers(2, [variable2_OPCUA])
                variable2_ModbusTCP = self.database_ModbusTCP.get_input_registers(2)
                print("variable2 ModbusTCP = {}".format(variable2_ModbusTCP))

                # this code is like modbus client changing the value of variable2 and see the changes in this test script
                variable2_write = self.variable1_OPCUA.get_value() + 100
                self.database_ModbusTCP.set_input_registers(102, [variable2_write])

                variable2_write_ModbusTCP = self.database_ModbusTCP.get_input_registers(102)[0]
                self.variable2_OPCUA.set_value(variable2_write_ModbusTCP)
                print("variable2 Write = {}".format(self.database_ModbusTCP.get_input_registers(102)))

                sleep(5)

        except Exception as error:

            print("Error: ", error.args)

        except KeyboardInterrupt:

            print("Finished Execution")

        finally:

            self.client_OPCUA.disconnect()
            print("Client OPC UA Disconnected")

            self.server_ModbusTCP.stop()
            print("Server Modbus TCP Offline")

OPCUA_ModbusTCP = OPCUA_Client_ModbusTCP_Server("opc.tcp://127.0.0.1:4840", "127.0.0.1", 502)

OPCUA_ModbusTCP.run()