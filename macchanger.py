import subprocess
import optparse
import re

def access():
    parse=optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="interface change :)")
    parse.add_option("-m","--mac",dest="mac_address",help="New mac address")

    return parse.parse_args()

def mac(inter,mac_adress):
    subprocess.call(["ifconfig",inter,"down"])
    subprocess.call(["ifconfig",inter,"hw","ether",mac_adress])
    subprocess.call(["ifconfig",inter,"up"])

def control(interface):
    ifconfig=subprocess.check_output(["ifconfig",interface])
    Nmac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",'ifconfig')

    if Nmac:
        return Nmac.group(0)
    else:
        return None

print("Mac deyisdirici basladildi !!!")

(userInput,arguments)=access()
mac(userInput.interface,userInput.mac_address)
Omac = control(userInput.interface)

if Omac == userInput.mac_address:
    print("Mac adresi deyisdirme ugursuz oldu")
else:
    print("Mac adresi ugurla deyisdirildi")
