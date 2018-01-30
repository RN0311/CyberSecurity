<p align="center">
  <img src="docs/scapy_logo.png" width=200>
</p>

# Scapy #

[![Travis Build Status](https://travis-ci.org/secdev/scapy.svg?branch=master)](https://travis-ci.org/secdev/scapy)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/secdev/scapy?svg=true)](https://ci.appveyor.com/project/secdev/scapy)
[![Codecov Status](https://codecov.io/gh/secdev/scapy/branch/master/graph/badge.svg)](https://codecov.io/gh/secdev/scapy)
[![PyPI Version](https://img.shields.io/pypi/v/scapy.svg)](https://pypi.python.org/pypi/scapy/)
[![Python Versions](https://img.shields.io/pypi/pyversions/scapy.svg)](https://pypi.python.org/pypi/scapy/)
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](LICENSE)
[![Join the chat at https://gitter.im/secdev/scapy](https://badges.gitter.im/secdev/scapy.svg)](https://gitter.im/secdev/scapy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) <br > <br >
Scapy is a powerful Python-based interactive packet manipulation program and
library. It can handle tasks like scanning, tracerouting, probing,
unit tests, attacks or network discovery (it can replace `hping`, 85% of `nmap`,
`arpspoof`, `arp-sk`, `arping`, `tcpdump`, `wireshark`, `p0f`, etc.).<br >
### Interactive shell ###

Scapy can easily be used as an interactive shell to interact with the network.
The following example shows how to send an ICMP Echo Request message to
`youtube.com`, then display the reply source IP address:
```python
sudo ./run_scapy 
Welcome to Scapy
>>> p = IP(dst="youtube.com")/ICMP()
>>> r = sr1(p)
Begin emission:
.Finished to send 1 packets.
*
Received 2 packets, got 1 answers, remaining 0 packets
>>> r[IP].src
'192.30.253.113'
```
<br >

```python
>>> ip/TCP()
<IP  frag=0 proto=tcp src=192.168.0.1 dst=192.168.0.2 |<TCP  |>>
>>> tcp=TCP(sport=1025, dport=80)
>>> (tcp/ip).show()
###[ TCP ]###
  sport= 1025
  dport= www
  seq= 0
  ack= 0
  dataofs= None
  reserved= 0
  flags= S
  window= 8192
  chksum= None
  urgptr= 0
  options= {}
###[ IP ]###
     version= 4
     ihl= None
     tos= 0x0
     len= None
     id= 1
     flags=
     frag= 0
     ttl= 64
(...)
```
<br >
