import uuid, os
if os.name == "nt": os.system("title Rovio Activation Script")
print("Rovio Activation Script v1.0.0 by PRO100KatYT\n")
# Not using f-strings for compatibility with Python 3.2+

def main():
    try:
        macAddress = '-'.join('{:012X}'.format(uuid.getnode())[i:i+2] for i in range(0, 12, 2))
        
        xmlContent = '''<?xml version="1.0" encoding="utf-8"?>
<data>
<Boolean key="BDPGS12FL" value="True" />
<String key="BDPGS12FL_hardwareID" value="{macAddress}" />
</data>'''.format(macAddress=macAddress)

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
