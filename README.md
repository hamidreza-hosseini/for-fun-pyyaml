**Introduction**
This repository is related to fstab entries with python script using pyyaml module.
Results tested on centos7,but same script can be executed on any linux distribution also build docker image with used commands.
 
**Prerequisities** 
1). Install python3 libraries on base OS.
2). Install yaml package using pip repository.
3). fstab input file as YAML format(Example: fstab.yaml)

**Installtion**
1). # yum install pyhton3 -y
2). pip install pyyaml -y

**Execution**
1). copy fstab.yaml and main.py script on any directory.
2). Run main.py script with python3.
    execution command: 
     # python3 main.py
	
**Results**
1). After script execution fatab.yaml entries present in /etc/fstab directory.
2). For results you can refer resultfstab.
