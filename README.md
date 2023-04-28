# VitrualDataCenter

The Data Center design adheres to the following considerations:
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
Linux (Ubuntu), Docker,Python, Shell Scripting, Promethus, Jenkins, Github, Jinja2, Ansible, Netmiko 

![image](https://user-images.githubusercontent.com/132085748/235199800-fcf42ed6-0e0f-46d1-8111-b52ff13c0184.png)

![DC2](https://user-images.githubusercontent.com/132085748/235199848-d1c8a910-3710-4878-b197-fd12c39b9f58.png)

![DC3](https://user-images.githubusercontent.com/132085748/235199892-3c52539b-317b-4597-bebe-56abb86946e4.png)

![DC4](https://user-images.githubusercontent.com/132085748/235199914-193c2ec6-52cf-4961-8b71-d5b1ac35aaf4.png)

![DC5](https://user-images.githubusercontent.com/132085748/235199954-3bcd1cf0-1eec-4466-934b-8c84ae9e6aaf.png)




