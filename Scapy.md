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
`youtube.com`, then display the reply source IP address: <br >
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
Below snipet specifies packet's source IP and then its destination IP. This type of information goes in the IP header, which is a layer 3 protocol according to the 0SI model:<br >

```python
>>> ip = IP(src="192.168.1.114")
>>> ip.dst="192.168.1.25"
>>> ip
<IP  src=192.168.1.114 dst=192.168.1.25 |>
```
If we want to add the header to the previous, we have to use operator ```/```.Below snipet, adds layer 4 protocol i.e. TCP.
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
Sending an ICMP packet.Scapy's method ```send()``` is used to send a single packet to the IP destination.Using show method, will give all the details of packet. <br >
```python
from scapy.all import *
packet = IP(dst="192.168.1.114")/ICMP()/"Hey,Rashmi!"
send(packet)
packet.show()

Sent 1 packets.
###[ IP ]###
  version   = 4
  ihl       = None
  tos       = 0x0
  len       = None
  id        = 1
  flags     =
  frag      = 0
  ttl       = 64
  proto     = icmp
  chksum    = None
  src       = 192.168.1.114
  dst       = 192.168.1.114
  \options   \
###[ ICMP ]###
     type      = echo-request
     code      = 0
     chksum    = None
     id        = 0x0
     seq       = 0x0
###[ Raw ]###
```
### TCP Three-way handshake
Firstly, create an instance of an IP header and then define a SYN instance of the TCP header and capture server's TCP sequence number from the server with SYNACK.seq, and increment it by 1.Finally, create the segment with no TCP flags and payload and send it.<br >
```python
ip = IP(src='192.168.1.114', dst='192.168.1.25')
SYN = TCP(sport=1024, dport=80, flags='S', seq=12345)
packet = ip/SYN
SYNACK = sr1(packet)
ack = SYNACK.seq + 1
ACK = TCP(sport=1024, dport=80, flags='A', seq=12346, ack=ack)
send(ip/ACK)
PUSH = TCP(sport=1024, dport=80, flags='', seq=12346, ack=ack)
data = "Hey,Rash!"
send(ip/PUSH/data)
```
### Fuzzing
Scapy's fuzz() method allows to craft fuzzing templates and send them in a loop.
```python
>>> send(IP(dst="192.168.1.114")/fuzz(UDP()/NTP(version=4)), loop=1)
................^C
Sent 16 packets.
```
