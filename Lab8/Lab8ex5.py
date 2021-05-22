#Ben Stobie
#26 March 2021

def main():
    ipInfo = makeDict()
    for i in ipInfo:
        print(i)
        print("Eth 1 - Ip address:", ipInfo[i]["Eth1"])
        print("Eth 2 - Ip address:", ipInfo[i]["Eth2"])

def makeDict():
    ipInfo = {"R1":{"Eth1":"", "Eth2":""},"R2":{"Eth1":"", "Eth2":""},"R3":{"Eth1":"", "Eth2":""}}
    i = 0
    x = 0
    for i in ipInfo:
        ipIn1 = input("Please enter an IP address for Eth1: ")
        y = 0
        while y != 1:
            for x in ipInfo:
                if ipIn1 in ipInfo[x]["Eth1"]:
                    print("***ERROR Duplicate IP***")
                    ipIn1 = input("Please enter another IP address for Eth1: ")
                elif ipIn1 in ipInfo[x]["Eth2"]:
                    print("***ERROR Duplicate IP***")
                    ipIn1 = input("Please enter another IP address for Eth1: ")
                else:
                    y = 1
        ipIn2 = input("Please enter an IP address for Eth2: ")
        ipInfo[i]["Eth1"] = ipIn1
        y = 0
        while y != 1:   
            for x in ipInfo:
                if ipIn2 in ipInfo[x]["Eth1"]:
                    print("***ERROR Duplicate IP***")
                    ipIn2 = input("Please enter another IP address for Eth2: ")
                elif ipIn2 in ipInfo[x]["Eth2"]:
                    print("***ERROR Duplicate IP***")
                    ipIn2 = input("Please enter another IP address for Eth2: ")
                else:
                    y = 1
        ipInfo[i]["Eth2"] = ipIn2    
    
    return ipInfo
        
    
    
main()
