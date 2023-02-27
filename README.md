<h1>PC Data Collector </h1>
This Python script collects and outputs information about your computer's hardware and network. It uses the psutil and socket modules to gather the following information:

    Hostname
    IP address
    CPU count
    Total memory
    Available memory
    Used memory
    Percentage of memory usage
    Total disk space
    Used disk space
    Free disk space
    Percentage of disk usage
    Network information
The script writes this information to a text file named pcdata_{hostname}.txt in the same directory as the script.
Usage
To run the script, simply execute it with Python:

    $ pip install -r requierements.txt
    $ python pcgrabber.py

Sample Output :

    Hostname: DESKTOP-ABC123
    IP address: 192.168.1.10
    CPU count: 4
    Total memory: 8589934592
    Available memory: 3300351488
    Used memory: 5288793088
    Percentage of memory usage: 61.6%
    Total disk space: 256060514304
    Used disk space: 8578347520
    Free disk space: 247482166784
    Percentage of disk usage: 3.3%
    Interface: Ethernet
    IP Address: 192.168.1.10
    Interface: VirtualBox Host-Only Network
    IP Address: 192.168.56.1
