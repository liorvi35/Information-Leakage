
# Leakage of Information in Critical-Infrastructures

This project serves as the final assignment for the "Protection of Communication Protocols" course, focusing on the subject of "Leakage of Information in Critical-Infrastructures."<br/>
Within the context of the Network Protocols Security course, we embark on simulating critical information leakages from a factory that utilizes HMI & SCADA systems, all while staying undetected.<br/>
This simulation is achieved through a middle-man attack, where we manipulate a MITM proxy to intercept and manipulate communication.<br/><br/>
Key points:
1. Simulation of a Critical Factory: The project revolves around the simulation of a critical factory environment using two virtual machines. One virtual machine represents the HMI & Scada system, while the second virtual machine acts as a communication proxy.
2. Innovative MITM Attack: The proxy server we use also serves as an inline MITM attacker. Our primary objective is to attempt to leak critical information from the factory without raising suspicion from the HMI system.
3. Focused on Modbus Protocol: Our project focuses on exploring a unique protocol known as Modbus, which operates over TCP/IP. Understanding the intricacies of this protocol is essential for executing the successful leakage simulation.

By combining our knowledge of network protocols, security measures, and comprehensive security analysis methods, we aim to gain valuable insights into potential vulnerabilities within critical infrastructures.<br/>
Through this project, we aspire to contribute to the advancement of secure communication protocols in critical industrial settings.


## Authors

- [@Lior Vinman](https://www.github.com/liorvi35)
- [@Yoad Tamar](https://www.github.com/yoadtamar)


## Installation and Deployment

To get started with the project, follow these steps to set up the virtual environments and configure them:

0. Clone this repository using:
```bash
  $ git clone https://github.com/liorvi35/Information-Leakage.git
```
1. Download the Virtual Environments:
   - Inside the task.pdf, you will find two links to download the virtual environments. These environments are required for the project and are valid as of today's date. Use the provided credentials in the task.pdf to access these virtual machines.
2. Start the Virtual Machines:
   - Once the download is complete, extract the archives and load the virtual machines into your virtualization software (e.g., VirtualBox or VMware).
   - One of the machines will serve as an HMI & ScadaBR simulation for a factory, and the second machine will act as an inline MITM proxy.
3. Configure IP Addresses:
   - After starting both virtual machines, configure them to have valid IP addresses. Refer to the documentation or instructions in the task.pdf to set up the IP addresses properly.
4. Access HMI Web-Interface and Attacker's Development Enviroment:
   - Open your web browser and enter the following URL: `http://<HMI-IP>:8080/ScadaBR`, authenticate using the provided credentials found in the task.pdf.
   - Open Pycharm on the attaker's VM, the file to "play with" is the `malicious.py`.


## 🛠 Skills
- Cyber Security.
- Computer Networking.
- Scada & HMI.
- Python Programming.
- Version control with Git.
- Linux.

## Project Collaboration
This project was developed in association with Otorio cyber-company.<br/>
We would like to extend our appreciation to the team at Otorio (and of-course, Dr. Ran Dubin, the lecturer of the course) for entrusting us with this interesting assignment.
![Logo](https://images.crunchbase.com/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/phou3jdgmsdmphapdika)

