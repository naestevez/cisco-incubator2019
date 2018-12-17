#  Author: Nayeli Alejandra Estevez
#  Title: NXOS toolkit


import json
import requests

nexus = {}

nexus["ip"] = input("ip:")
nexus["port"] = input("port:")
nexus["user"] = input("user:")
nexus["pw"] = input("password:")


uri = 'http://{}:{}/ins'.format(nexus['ip'], nexus['port'])

jsonrpc_headers = {'Content-Type': 'application/json-rpc'}

payload = [
          {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
              "cmd": "show version",
              "version": 1
            },
            "id": 1
          }
          ]

payload2 = [
            {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
              "cmd": "show ip interface brief",
              "version": 1
            },
            "id": 1
            }
            ]

response = requests.post(uri, data=json.dumps(payload), headers=jsonrpc_headers, auth=(nexus["user"], nexus["pw"]))

# print("status code:", response.status_code)


response2 = requests.post(uri, data=json.dumps(payload2), headers=jsonrpc_headers, auth=(nexus["user"], nexus["pw"]))

# print("status code:", response2.status_code)




class Nexus():

    def __init__(self):
    """initiates an Nexus instance with class attributes"""
        show_vers_plat_dict = json.loads(response.text)
        self.version = show_vers_plat_dict["result"]["body"]["kickstart_ver_str"]
        self.platform = show_vers_plat_dict["result"]["body"]["chassis_id"]



    def authenticate(self):
        """authenticates and prints status code if successful"""
        if response.status_code != 200:
            print("authentication unsuccessful")
        else:
            print("authentication successful - status code:", response.status_code)



    def get_interface_status(self, if_name):
        """prints status of specified interface"""
        show_if_json = json.loads(response2.text)
        interfaces = show_if_json["result"]["body"]["TABLE_intf"]["ROW_intf"]

        #  iterates through list of dictionaries, each dict containing interface
        #  creates new dictionary with all interface names and link states
        interface = ""
        link_state = ""
        interfaces_link_state = {}

        for intf in interfaces:
            for k, v in intf.items():
                if k == "intf-name":
                    interface = intf[k]
                if k == "link-state":
                    link_state = intf[k]
                interfaces_link_state[interface] = link_state


        #  checks to see if specified interface name is in new dictionary and prints whether it is up, down or does not exist
        #  need to add some regex cover all interface name variations
        if if_name in interfaces_link_state.keys():
            print("{} interface is {}".format(if_name, interfaces_link_state[if_name]))
        else:
            print("{} interface does not exist".format(if_name))

        #  return #up, down, or unknown
        #  need to add some regex cover all interface name variations
        if if_name in interfaces_link_state:
            return interfaces_link_state[if_name]
        else:
            return "unknown"

#  configures the description of the interface
#  def configure_interface_desc(self, if_name, description):
#
#
#
#
#
#  return None
