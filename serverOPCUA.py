from opcua import Server
from time import sleep
import threading
import random

class OPCUA_Server():


    def __init__(self, url):
        self.url = url
        self.server = Server()

        self.server.set_endpoint(self.url)

        self.name = "OPC UA Server"
        self.addspace = self.server.register_namespace(self.name)

        self.node = self.server.get_objects_node()
        self.variables = self.node.add_object(self.addspace, "variables")

        self.variable1 = self.variables.add_variable(self.addspace, "Variable1", 0)
        self.variable1.set_writable()

        self.variable2 = self.variables.add_variable(self.addspace, "Variable2", 0)
        self.variable2.set_writable()

    def run(self):

        try:
            self.server.start()
            print("Server Online at {}".format(self.url))

            while True:

                i = random.randint(0, 100)
                self.variable1.set_value(i)
                print("variable1 = {}".format(self.variable1.get_value()))
                print("variable2 = {}".format(self.variable2.get_value()))
                sleep(5)

        except Exception as error:

            print("Error: ", error.args)

        except KeyboardInterrupt:

            print("Finished Execution")

        finally:

            self.server.stop()
            print("Server Offline")

opcua_server = OPCUA_Server("opc.tcp://127.0.0.1:4840")

opcua_server_thread = threading.Thread(target=opcua_server.run, args=()).start()