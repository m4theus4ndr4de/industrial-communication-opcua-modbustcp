from pyModbusTCP.server import ModbusServer
from time import sleep
import random

class ModbusTCP_Server():

    def __init__(self, ip_ModbusTCP, port_ModbusTCP):

        self.server_ModbusTCP = ModbusServer(host=ip_ModbusTCP, port=port_ModbusTCP, no_block=True)
        self.database_ModbusTCP = self.server_ModbusTCP.data_bank
        self.ip_ModbusTCP = ip_ModbusTCP
        self.port_ModbusTCP = port_ModbusTCP

    def run(self):

        try:

            self.server_ModbusTCP.start()
            print("Server MODBUS TCP Online at {}".format(self.ip_ModbusTCP))

            while True:

                i = random.randint(0, 100)
                self.database_ModbusTCP.set_input_registers(1, [i])
                variable1_ModbusTCP = self.database_ModbusTCP.get_input_registers(1)
                print("variable1 ModbusTCP = {}".format(variable1_ModbusTCP))

                sleep(5)

        except Exception as error:

            print("Error: ", error.args)

        except KeyboardInterrupt:

            print("Finished Execution")

        finally:

            self.server_ModbusTCP.stop()
            print("Server Modbus TCP Offline")

modbustcp_server = ModbusTCP_Server("127.0.0.1", 502)

modbustcp_server.run()