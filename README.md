# Morphle Labs
# Problem
PROBLEM


Create an account on https://github.com  
Create a codespace https://github.com/codespaces
Set Codespace timeout to 240 minutes. (maximum)
Start a codespace
Create a django or flask application with an /htop endpoint
Add a port with public visibility to serve the application
DO NOT STOP THE CODESPACE as the endpoint should keep working.
/htop endpoint should print the below data on the webpage.
Name - your full name
Username - system username
Server Time in IST
Top output
Example page would look like below. Test this endpoint in the incognito tab before submitting for the test.

# exapmle  of output 
System Info
Name: Akshata Laxman Pawar

Username: codespace

Server Time (IST): 2025-02-20 12:58:03 IST

top - 07:28:03 up  5:18,  0 users,  load average: 0.12, 0.47, 0.69
Tasks:  22 total,   1 running,  21 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   7929.6 total,    450.1 free,   2177.2 used,   5302.3 buff/cache
MiB Swap:      0.0 total,      0.0 free,      0.0 used.   5373.0 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
      1 codespa+  20   0    1136    128    128 S   0.0   0.0   0:00.05 docker-+
      6 codespa+  20   0    2616   1408   1408 S   0.0   0.0   0:00.32 sh
    156 root      20   0   12196   3352   2432 S   0.0   0.0   0:00.00 sshd
    283 root      20   0 1983004  82800  56704 S   0.0   1.0   0:00.24 dockerd
    553 root      20   0 1725116  49344  31104 S   0.0   0.6   0:00.82 contain+
   4089 codespa+  20   0    2616   1408   1408 S   0.0   0.0   0:00.01 sh
   4121 root      20   0    2616   1536   1536 S   0.0   0.0   0:00.00 sh
   4270 codespa+  20   0    2624   1408   1408 S   0.0   0.0   0:00.01 sh
   4279 codespa+  20   0   11.3g 164868  46336 S   0.0   2.0   0:43.20 node
   4327 codespa+  20   0   31.4g 260728  55296 S   0.0   3.2   0:17.25 node
   4342 codespa+  20   0   11.4g  90564  42880 S   0.0   1.1   0:07.25 node
   5996 codespa+  20   0   11.0g  68528  43776 S   0.0   0.8   0:01.10 node
   6014 codespa+  20   0   16808  11776   3456 S   0.0   0.1   0:00.11 bash
   6719 codespa+  20   0   11.1g 109360  44416 S   0.0   1.3   0:01.00 node
   6748 codespa+  20   0  994216  53496  40448 S   0.0   0.7   0:00.17 node
   6759 codespa+  20   0   16684  11520   3328 S   0.0   0.1   0:00.14 bash
   6867 codespa+  20   0   22.8g 756968  45940 S   0.0   9.3   0:30.48 node
   9424 codespa+  20   0   16816  11392   3200 S   0.0   0.1   0:00.10 bash
  12199 codespa+  20   0  188524  31740  11264 S   0.0   0.4   0:00.19 python
  12292 codespa+  20   0    7236   1920   1920 S   0.0   0.0   0:00.00 sleep
  12294 codespa+  20   0    2620   1408   1408 S   0.0   0.0   0:00.00 sh
  12295 codespa+  20   0   10884   3584   3200 R   0.0   0.0   0:00.00 top

