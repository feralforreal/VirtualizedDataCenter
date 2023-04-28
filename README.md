# VitrualizedDataCenter

The Data Center design adheres to the following considerations:
1. Security First approach – The data center network must be protected from both external and internal security vulnerabilities.
According to Verizon Data Breach investigations – Insider threats accounted for 30% of data breaches while outsider threats accounted for 70%
2. I followed Fully Automated and Pipelined Development Cycle
3. The data center is designed to be fully modifiable and managed from the management connection. The management connection requires multiple unit tests to be ran, and code approvals before the changes can be made.
4. Fully modular Design – The data center must be fully modular, this allows for any service to be added or removed without affecting any other service.
5. On Demand Testing Scenario – Dynamic on-demand creation of a testing playground, where new features can be tested before being deployed. 


All the networking deployed in the data center is virtualized, this provides for multiple advantages over traditional networking:
1.No physical links interconnecting networking equipment – Lesser chance of layer 1 failure
2. A Scalable solution given its takes < 10 mins to spin up new machines to meet growing demands
3. No requirement of transporting network equipment – The only physical purchase would be the server racks and underlay switching
4. The CPU , RAM, Storage constraints of physical equipment doesn’t apply – We can automatically provision more XYZ components to the virtualized equipment, instantly increasing it capabilities.
5. Its highly flexible, scalable and secure. They can be isolated and segmented as needed. Its scalable as XYZ components for servers are a lot cheaper and readily available. 


Tech stack : 
Linux (Ubuntu), Docker, Python, Shell Scripting, Promethus, Jenkins, Github, Jinja2, Ansible, Netmiko, OpenFlow, Grafana

All the customer edge and private edge routers are built on Docker Images 
![DC1](https://user-images.githubusercontent.com/132085748/235200084-07f8ff2f-b5ef-4db2-9595-aa6ebc8dbdb5.png)

The Customer Edge network connects to the Internet and peering ISPS
![DC2](https://user-images.githubusercontent.com/132085748/235199848-d1c8a910-3710-4878-b197-fd12c39b9f58.png)

Any egress and ingress traffic to and from the network is firewall protected.
![DC3](https://user-images.githubusercontent.com/132085748/235199892-3c52539b-317b-4597-bebe-56abb86946e4.png)

The out-of-band network is used for CI/CD, Promethus and Network Management and Configuration
![DC4](https://user-images.githubusercontent.com/132085748/235199914-193c2ec6-52cf-4961-8b71-d5b1ac35aaf4.png)

![DC5](https://user-images.githubusercontent.com/132085748/235199954-3bcd1cf0-1eec-4466-934b-8c84ae9e6aaf.png)

![image](https://user-images.githubusercontent.com/132085748/235204235-df9e76b7-97a2-4987-864f-369fc637c3cc.png)



