import scapy.all as scapy
import optparse

def access():
    agh = optparse.OptionParser()
    agh.add_option("-i","--ipaddress",dest="ip_adresi",help="-i veya --ipaddress yazaraq ip adresi girin:")

    (user_giris,arguments) = agh.parse_args()

    if not user_giris.ip_adresi:
        print("bir IP de gire bilmedin! :)")
        return user_giris.ip_adresi
def skaner(ip):
    istek_paket = scapy.ARP(pdst="10.0.2.1/24")
    #scapy.ls(scapy.ARP())
    yayin_paket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    paket = istek_paket/yayin_paket

    (esilpaket,cavabsizpaket) = scapy.srp(paket,timeout=1)
    print(list(esilpaket))
    esilpaket.summary()

ipadresim = access()
skaner(ipadresim)