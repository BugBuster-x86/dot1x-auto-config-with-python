# dot1X Configuration Automation Script

This Python script automates the configuration of 802.1X Network Access Control (NAC) on Cisco switches. The script utilizes the pyATS framework to connect to devices specified in a testbed.yaml file and applies the 802.1X configuration to a specific interface.
Table of Contents

    Overview
    Prerequisites
    Installation
    Usage
    Configuration
    Execution
    License

Overview

802.1X is a network protocol used to authenticate devices attempting to connect to a network. This script simplifies the process of applying 802.1X configurations across multiple Cisco devices by automating the repetitive task of configuring network interfaces.
Prerequisites

Before you begin, ensure you have the following:

    Python 3.6+: The script requires Python version 3.6 or later.
    pyATS Library: The script leverages the pyATS library for network device interactions.
    Network Access: Ensure you have network access to the Cisco devices you intend to configure.
    Credentials: You will need valid credentials to access the devices.

Installation

Follow these steps to set up the environment:

    Install Python: Ensure you have Python 3.6+ installed on your system. You can download it from the official Python website.

    Set up a virtual environment (optional but recommended):

    bash

python -m venv pyats-env
source pyats-env/bin/activate  # On Windows use `pyats-env\Scripts\activate`

Install pyATS:

bash

    pip install pyats

    Prepare your testbed.yaml file:
        Create a testbed.yaml file that includes the devices you want to configure. See the pyATS documentation for details on how to create this file.

Usage

    Configure the script:
        Ensure the script is updated to point to your testbed.yaml file.
        Update the nac_commands variable with the desired 802.1X configuration commands if needed.

    Define your testbed:
        The script references a testbed.yaml file to know which devices to connect to. Make sure this file is correctly set up with the device details.

Configuration

    Testbed File: The script loads device information from a testbed.yaml file. This file should define your devices and their connection details. Below is an example structure of a testbed.yaml file:

yaml

devices:
  switch1:
    os: ios
    type: switch
    connections:
      cli:
        protocol: ssh
        ip: 192.168.1.1
    credentials:
      default:
        username: admin
        password: password

    NAC Commands: The nac_commands variable in the script holds the 802.1X configuration commands that will be applied to the interfaces. You can customize these commands as needed for your specific network configuration.

python

nac_commands = '''
    switchport mode access
    authentication port-control auto
    dot1x pae authenticator
'''

Execution

    Run the script:
        Execute the script using Python. This will connect to each device in the testbed.yaml file and configure the specified interface.

    bash

python configure_8021x.py

Monitor the output:

    The script will print the configuration steps and any errors encountered during the process.
