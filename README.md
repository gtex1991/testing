************************************************

# TABLE OF CONTENTS
* [INTRODUCTTION](#INTRODUCTTION)
* [PREREQUISITE](#tPREREQUISITE)
* [SETUP](#SETUP)
* [LAUNCH](#LAUNCH)

# INTRODUCTTION

The puporse of this program is to Retrieve the contents of the contact list from the
[API](https://www.senate.gov/general/contact_information/senators_cfm.xml) in the raw XML format to JSON.
For the data contained inside the Member fields in the XML file, convert the data into
the JSON format listed below.

```
{
	“firstName”: “First”,
	“lastName”: “Last”,
	“fullName”: “First Last”,
	“chartId”: “:Contents of bioguide_id:”,
	“mobile”: “Phone”,
	“address”: [
		{
			“street”: “123 Main Street”,
			“city”: “Orlando”,
			“state”: “FL”,
			“postal”: 32825
				]
		}
}
```


## PREREQUISITE

1. OS : Mac OS X
2. Language: Python 3.7.2
3. pip (For installing python packages/modules)

**NOTE THIS CAN RUN ON ANY MACHINE THAT IS COMPATIBLE WITH PYTHON3**

## SETUP
**Make sure the following modules are installed for python3**

1. in mac os x terminal,	type : python3
2. in the python console	type : import requests
3. if you get an error
	install requests package  - > Ctrl c (back to terminal), type: $ sudo pip3 install requests


## LAUNCH
1. download the project folder from github into the desktop folder
2. open terminal in mac: Cmd + 'spacebar' type terminal
3. Navigate to the projects location
	for my location machine its "/Users/gastonmulisanga/Desktop/Mend_Pro"
4. to run the program, in terminal type : python3 API.py
5. check the output of the program, it should be JSON output from the api link.
