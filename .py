from genie.testbed import load

# load Testbed file
testbed = load('testbed.yaml')

# NAC config commands with multiple lines
nac_commands = '''
    switchport mode access
    authentication port-control auto
    dot1x pae authenticator
'''

def configure_nac(device, interface):
    print(f"configure NAC on {device.name}, Interface {interface}")
    device.connect(log_stdout=False)

    # config commands on specific interface
    config_commands = f'''
        interface {interface}
        {nac_commands}
        exit
    '''
    
    # send commands on device
    device.configure(config_commands)
    device.disconnect()

# configure commands on the specific interface for all devices
for device_name in testbed.devices:
    device = testbed.devices[device_name]
    configure_nac(device, 'Gi0/1')

print("802.1X config done!")
