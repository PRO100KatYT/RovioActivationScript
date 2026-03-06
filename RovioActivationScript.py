import uuid, os, subprocess
if os.name == "nt": os.system("title Rovio Activation Script")
print("Rovio Activation Script v1.0.1 by PRO100KatYT\n")
# Not using f-strings for compatibility with Python 3.2+

def getMacAddressesInString():
    macAddresses = []
    try:
        output = subprocess.check_output("getmac /fo csv /nh", universal_newlines=True)
        for line in output.splitlines():
            if not line.strip(): continue
            parts = line.split(",")
            if len(parts) > 0:
                macAddress = parts[0].replace("\"", "").upper()
                if len(macAddress) == 17 and macAddress.count("-") == 5:
                    if macAddress not in macAddresses:
                        macAddresses.append(macAddress)
    except: pass
    if not macAddresses: # Use the old method of getting the address just in case something goes wrong
        mac_int = uuid.getnode()
        macAddresses.append("-".join("{:012X}".format(mac_int)[i:i+2] for i in range(0, 12, 2)))
    return ";".join(macAddresses)

def main():
    try:
        xmlContent = '''<?xml version="1.0" encoding="utf-8"?>
<data>
<Boolean key="BDPGS12FL" value="True" />
<String key="BDPGS12FL_hardwareID" value="{macAddress}" />
</data>'''.format(macAddress=getMacAddressesInString())

        appDataRoamingPath = os.environ['APPDATA']
        appDataPath = os.path.dirname(appDataRoamingPath)
        targetDir = os.path.join(appDataPath, 'LocalLow', 'Rovio', 'Bad Piggies')
        os.makedirs(targetDir, exist_ok=True)
        filePath = os.path.join(targetDir, 'Settings.xml')

        with open(filePath, 'w', encoding='utf-8') as f: f.write(xmlContent)
        
        input("Settings.xml file has successfully been generated and saved in:\n{filePath}\n\nBad Piggies should now be activated!\n\nPress ENTER to close the program.".format(filePath=filePath))

    except KeyError:
        print("Can't find the AppData folder. Are you sure you are on Windows?")
    except Exception as e:
        print("Unexpected error: {}".format(e))

try:
    main()
except ValueError as e:
    input("Error: {}\nPress ENTER to close the program.".format(e))
