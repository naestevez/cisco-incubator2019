# NXOS Toolkit Library

The NXOS Toolkit can access Nexus switch through NX-API CLI. Authentication is needed with the credentials as stated below. Version and platform can be identified and the link status of a specified interface can be retrieved.

## Requirements

The following credentials are needed for authentication:

* IP address
* port number
* username
* password

---

## Usage

```python
import json
import requests

#  create an object from the Nexus() class
nexus = Nexus()

#  confirm authentication
print(nexus.authenticate())

#  print version and platform
print(nexus.version)
print(nexus.platform)

#  find out link status of specified interface
print(nexus.get_interface_status([interface_name]))
```
----

## Contributing

Pull requests are welcome. For major changes or feedback, please open an issue first to discuss what you would like to change.

---

## Author

Created by N. Alejandra Estevez for Cisco Incubator program - Python Track
twitter: @naestevez
github: @nestevez7
