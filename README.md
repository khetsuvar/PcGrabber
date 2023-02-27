
    <header>
        <h1>Python PC Data Collector</h1>
    </header>

    <div class="container">
        <h2>About</h2>
        <p>This is a simple Python script that collects various information about the computer it's run on, including IP address, CPU count, memory usage, disk usage, and network information.</p>

        <h2>Requirements</h2>
        <p>This script requires the <code>psutil</code> and <code>socket</code> modules to be installed.</p>
        <pre><code>pip install psutil socket</code></pre>

        <h2>How to Use</h2>
        <p>To use this script, simply run it using Python:</p>
        <pre><code>python pc_data_collector.py</code></pre>
        <p>The script will generate a text file named <code>pcdata_&lt;hostname&gt;.txt</code> in the same directory as the script, where <code>&lt;hostname&gt;</code> is the hostname of the computer. The file will contain the following information:</p>
        <ul>
            <li>Hostname</li>
            <li>IP address</li>
            <li>CPU count</li>
            <li>Total memory</li>
            <li>Available memory</li>
            <li>Used memory</li>
            <li>Percentage of memory usage</li>
            <li>Total disk space</li>
            <li>Used disk space</li>
            <li>Free disk space</li>
            <li>Percentage of disk usage</li>
            <li>Network information</li>
        </ul>
    <h2>Sample Output</h2>
    <pre><code>Hostname: DESKTOP-ABC123
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
    IP Address: 192.168.56.1</code></pre>
    </body>
    </html>
