import os
import base64

ptt = os.path.abspath(os.path.join(os.getcwd(), '..'))
os.makedirs(os.path.join(ptt, 'Splitted-By-Protocol'), exist_ok=True)

vmess_file = os.path.join(ptt, 'Splitted-By-Protocol/vmess.txt')
vless_file = os.path.join(ptt, 'Splitted-By-Protocol/vless.txt')
trojan_file = os.path.join(ptt, 'Splitted-By-Protocol/trojan.txt')
ss_file = os.path.join(ptt, 'Splitted-By-Protocol/ss.txt')
ssr_file = os.path.join(ptt, 'Splitted-By-Protocol/ssr.txt')
reality_file = os.path.join(ptt, 'Splitted-By-Protocol/reality.txt')
Hysteria2_file = os.path.join(ptt, 'Splitted-By-Protocol/Hysteria2.txt')
Tuic_file = os.path.join(ptt, 'Splitted-By-Protocol/Tuic.txt')
WireGuard_file = os.path.join(ptt, 'Splitted-By-Protocol/WireGuard.txt')

open(vmess_file, "w").close()
open(vless_file, "w").close()
open(trojan_file, "w").close()
open(ss_file, "w").close()
open(ssr_file, "w").close()
open(reality_file, "w").close()
open(Hysteria2_file, "w").close()
open(Tuic_file, "w").close()
open(WireGuard_file, "w").close()

vless = ""
trojan = ""
ss = ""
ssr = ""
reality = ""
Hysteria2 = ""
Tuic = ""
WireGuard = ""
with open(os.path.join(ptt, 'All_Configs_Sub.txt'), "r") as f:
    respnse = f.read()
for config in respnse.splitlines():
    if config.startswith("vmess"):
        open(vmess_file, "a").write(config + "\n")     
    if config.startswith("vless"):
        vless += config + "\n"  
    if config.startswith("trojan"):
        trojan += config + "\n"   
    if config.startswith("ss"):   
        ss += config + "\n"
    if config.startswith("ssr"):
        ssr += config + "\n"
    if config.startswith("reality"):
        reality += config + "\n"
    if config.startswith("Hysteria2"):
        Hysteria2 += config + "\n"
    if config.startswith("Tuic"):
        Tuic += config + "\n"
    if config.startswith("WireGuard"):
        WireGuard += config + "\n"
      
open(vless_file, "w").write(base64.b64encode(vless.encode("utf-8")).decode("utf-8"))
open(trojan_file, "w").write(base64.b64encode(trojan.encode("utf-8")).decode("utf-8"))
open(ss_file, "w").write(base64.b64encode(ss.encode("utf-8")).decode("utf-8"))
open(ssr_file, "w").write(base64.b64encode(ssr.encode("utf-8")).decode("utf-8"))
open(reality_file, "w").write(base64.b64encode(reality.encode("utf-8")).decode("utf-8"))
open(Hysteria2_file, "w").write(base64.b64encode(Hysteria2.encode("utf-8")).decode("utf-8"))
open(Tuic_file, "w").write(base64.b64encode(Tuic.encode("utf-8")).decode("utf-8"))
open(WireGuard_file, "w").write(base64.b64encode(WireGuard.encode("utf-8")).decode("utf-8"))
