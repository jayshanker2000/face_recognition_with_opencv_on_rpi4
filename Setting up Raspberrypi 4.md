* Download Raspbian Buster from : https://www.raspberrypi.org/downloads/raspbian/  
Download Balena Etcher from : https://www.balena.io/etcher/

* Insert your SD Card and Flash the image.  
Boot your pi in headless mode.

* In CMD type: ```ssh pi@raspberrypi.local```  
Password : ```raspberry```  
*If there is an error :* ```ssh-keygen -R raspberrypi.local```

* **Internet Connectivity** : ```ping www.google.com```  
If there is Error : go to Netork and Sharing Center > Wi-fi > Disable and then Enable sharing

* **Expand Filesystem** : ```sudo raspi-config``` > Advanced Options > A1 expand filesystem  
```sudo reboot```

```sudo apt update && sudo apt upgrade```  
```sudo apt install realvnc-vnc-server realvnc-vnc-viewer```  
```sudo reboot```
