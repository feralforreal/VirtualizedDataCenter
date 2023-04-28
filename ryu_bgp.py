import os    
if __name__ == '__main__':
    with open("/home/vishal/Documents/poc/nsot/bgp_conf.config","r") as bgpfile:
        data = bgpfile.read()
        data = data.replace('LOCALASNUMBER',"2")
        data = data.replace('LOCALROUTERID','"7.0.200.12"')
        data = data.replace('REMOTEADDRESS','"7.0.200.4"')
        data = data.replace('REMOTEAS',"1")
        #print(data)
        with open("/home/vishal/Documents/poc/nsot/bgp_conf_temp.config","w") as bgpfile2:
            bgpfile2.write(data)
