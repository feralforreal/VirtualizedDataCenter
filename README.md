# VitrualDataCenter

Data Center must adheres to the following considerations:
Security First approach – The data center network must be protected from both external and internal security vulnerabilities.
According to Verizon Data Breach investigations – Insider threats accounted for 30% of data breaches while outsider threats accounted for 70%
Fully Automated and Pipelined Development Cycle
The data center is designed to be fully modifiable and managed from the management connection. The management connection requires multiple unit tests to be ran, and code approvals before the changes can be made.
Fully modular Design – The data center must be fully modular, this allows for any service to be added or removed without affecting any other service.
On Demand Testing Scenario – Dynamic on-demand creation of a testing playground, where new features can be tested before being deployed. 


All the networking deployed in the data center is virtualized, this provides for multiple advantages over traditional networking:
No physical links interconnecting networking equipment – Lesser chance of layer 1 failure
A Scalable solution given its takes < 10 mins to spin up new machines to meet growing demands
No requirement of transporting network equipment – The only physical purchase would be the server racks and underlay switching
The CPU , RAM, Storage constraints of physical equipment doesn’t apply – We can automatically provision more XYZ components to the virtualized equipment, instantly increasing it capabilities.
Its highly flexible, scalable and secure. They can be isolated and segmented as needed. Its scalable as XYZ components for servers are a lot cheaper and readily available. 

Tech stack : 
Linux (Ubuntu)
Docker
Python
Shell Scripting
Ansible 


