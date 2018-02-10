## Malicious Traffic Detection Tools

## [MalTrail](https://github.com/stamparm/maltrail)
Maltrail is a malicious traffic detection system,which monitors the passing traffic for "blacklisted" items/trails.It's based on traffic -> Sensor <-> Servor -> Client architecture.<br >
Below screenshot depicts it's default interface.<br >
Default **username** : *admin* & Default **password** : *changeme!*<br >
![architecture diagram](https://github.com/RN0311/CyberSecurity/blob/master/img/maltrail_2.png)
<br >
### Suspicious HTTP requests 
Maltrail detects suspicious requests coming from outer web application and the internal user malicious attempts toward unknown web sites,threats like the following could be found (real case of attackers trying to exploit Joomla! CMS CVE-2015-7297, CVE-2015-7857, and CVE-2015-7858 vulnerabilities):
![http requests](https://github.com/RN0311/CyberSecurity/blob/master/img/maltrail_1.png)
<br >
If you click on the bubble icon (i.e. Ellipsis) for details then you can copy paste the whole content to a text file, & can see all suspicious HTTP requests.Below snapshot depicts that.
![snapshot3](https://github.com/RN0311/CyberSecurity/blob/master/img/maltrail_3.png)
<br >
We can apply filter ```ipinfo``` to get list of all potentially infected computers in a network range which share that kind of suspicious behaviour.<br >
Also, it uses (optional) advanced heuristic mechanisms that can help in the discovery of unknown threats (e.g. new malware).
<br >
**Nota Bene:**<br >
When you'll run ZAP(i.e. send malicious http requests from it) and simulataneously start Maltrail, then you can clearly see number of threats, trails etc. features of Maltrail will be updated.<br >
To get better understanding of the working mechanics of Maltrail, checkout resources.
<br ><br >

## [CapTipper](https://github.com/omriher/CapTipper)
CapTipper is a Python tool which is used to analyze, explore and revive HTTP malicious traffic.It contains internal tools, with a powerful interactive console, to draw analysis and inspection of the hosts, objects.
```sh
Usage: sudo python ./CapTipper.py <PCAP_file> [-p] [web_server_port=70]
```
![defaultimage](https://github.com/RN0311/CyberSecurity/blob/master/img/captipper_4.png)
<br >
To get bird's eye view on the traffic, use ```hosts``` command and you'll get similar results.<br >
![hosts](https://github.com/RN0311/CyberSecurity/blob/master/img/hosts.png) <br >
We can also, get head and body of the page by typing ```head``` and ```body```.<br >
![body](https://github.com/RN0311/CyberSecurity/blob/master/img/captipper_1.png)
<br >
![head](https://github.com/RN0311/CyberSecurity/blob/master/img/captipper_2.png)
<br >
To get more information on object 60 use command ```info 60```: <br >
![info](https://github.com/RN0311/CyberSecurity/blob/master/img/captipper_3.png)
<br >
To get shortened URI paths, use command ``` sudo python ./CapTipper.py <PCAP_FILE> [-p] [web_server_port=3091] --ungzip -short```
![info](https://github.com/RN0311/CyberSecurity/blob/master/img/short.png)
<br >
To view traffic flow, use command ``` hosts ```
![info](https://github.com/RN0311/CyberSecurity/blob/master/img/latest_hosts.png)

## Resources
1) https://github.com/stamparm/maltrail 
2) https://www.terena.org/activities/tf-csirt/meeting47/M.Stampar-Maltrail.pdf
3) https://github.com/omriher/CapTipper
4) http://www.omriher.com/2015/01/captipper-malicious-http-traffic.html

