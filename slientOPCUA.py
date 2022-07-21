from opcua import Client
from time import sleep
import threading

class OPCUA_Client():

    def __init__(self, url):

        self.url = url
        self.client = Client(self.url)

        self.variable1 = self.client.get_node("ns=2;i=2")
        self.variable2 = self.client.get_node("ns=2;i=3")

    def run(self):

        try:

            self.client.connect()
            print("Client OPC UA Connected to {}".format(self.url))

            while True:

                print(self.variable1.get_value())
                sleep(5)

        except Exception as error:

            print("Error: ", error.args)

        except KeyboardInterrupt:

            print("Finished Execution")

        finally:

            self.client.disconnect()
            print("Client OPC UA Disconnected")

opcua_client = OPCUA_Client("opc.tcp://127.0.0.1:4840")

opcua_client_thread = threading.Thread(target=opcua_client.run, args=()).start()