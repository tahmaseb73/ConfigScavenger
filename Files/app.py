import pybase64
import base64
import requests
import binascii
import os
import time

TIMEOUT = 20
fixed_text = """#profile-title: base64:8J+GkyBHaXRodWIgfCBCYXJyeS1mYXIg8J+ltw==
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/tahmaseb73/v2ray-configs
#profile-web-page-url: https://github.com/Argh94/v2ray-configs
"""

def decode_base64(encoded):
    decoded = ""
    for encoding in ["utf-8", "iso-8859-1"]:
        try:
            decoded = pybase64.b64decode(encoded + b"=" * (-len(encoded) % 4)).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error):
            pass
    return decoded

def decode_links(links):
    decoded_data = []
    for link in links:
        for _ in range(3):  # ۳ بار تلاش
            try:
                response = requests.get(link, timeout=TIMEOUT)
                response.raise_for_status()
                encoded_bytes = response.content
                decoded_text = decode_base64(encoded_bytes)
                decoded_data.append(decoded_text)
                break
            except requests.RequestException:
                time.sleep(5)
                continue
    return decoded_data

def decode_dir_links(dir_links):
    decoded_dir_links = []
    for link in dir_links:
        for _ in range(3):  # ۳ بار تلاش
            try:
                response = requests.get(link, timeout=TIMEOUT)
                response.raise_for_status()
                decoded_text = response.text
                decoded_dir_links.append(decoded_text)
                break
            except requests.RequestException:
                time.sleep(5)
                continue
    return decoded_dir_links

def filter_for_protocols(data, protocols):
    filtered_data = []
    for line in data:
        if any(protocol in line for protocol in protocols):
            filtered_data.append(line)
    return filtered_data

def ensure_directories_exist():
    output_folder = os.path.abspath(os.path.join(os.getcwd(), ".."))
    base64_folder = os.path.join(output_folder, "Base64")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.exists(base64_folder):
        os.makedirs(base64_folder)
    return output_folder, base64_folder

def main():
    output_folder, base64_folder = ensure_directories_exist()
    protocols = ["vmess", "vless", "trojan", "ss", "ssr", "hy2", "tuic", "warp://"]
    links = [
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/mix",
        "https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt",
        "https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/reality",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vless",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vmess",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/trojan",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/shadowsocks",
        "https://raw.githubusercontent.com/ts-sf/fly/main/v2",
        "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2"
    ]
    dir_links = [
        "https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config",
        "https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Config",
        "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt",
        "https://raw.githubusercontent.com/itsyebekhe/HiN-VPN/main/subscription/normal/mix",
        "https://raw.githubusercontent.com/sarinaesmailzadeh/V2Hub/main/merged",
        "https://raw.githubusercontent.com/freev2rayconfig/V2RAY_SUBSCRIPTION_LINK/main/v2rayconfigs.txt",
        "https://raw.githubusercontent.com/Everyday-VPN/Everyday-VPN/main/subscription/main.txt",
        "https://raw.githubusercontent.com/C4ssif3r/V2ray-sub/main/all.txt",
        "https://raw.githubusercontent.com/10ium/V2Hub3/main/Split/Normal/vmess",
        "https://raw.githubusercontent.com/10ium/V2Hub3/main/Split/Normal/vless",
        "https://raw.githubusercontent.com/10ium/V2Hub3/main/Split/Normal/reality",
        "https://raw.githubusercontent.com/10ium/V2Hub3/main/Split/Normal/trojan",
        "https://raw.githubusercontent.com/10ium/V2Hub3/main/Split/Normal/shadowsocks",
        "https://raw.githubusercontent.com/SezarSec/sezarsubs/refs/heads/main/Sezar-sublink",
        "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/splitted/ss.txt",
        "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/splitted/vmess.txt",
        "https://raw.githubusercontent.com/miladtahanian/V2RayScrapeByCountry/refs/heads/main/output_configs/Hysteria2.txt",
        "https://raw.githubusercontent.com/miladtahanian/V2RayScrapeByCountry/refs/heads/main/output_configs/ShadowSocks.txt",
        "https://raw.githubusercontent.com/miladtahanian/V2RayScrapeByCountry/refs/heads/main/output_configs/ShadowSocksR.txt",
        "https://raw.githubusercontent.com/miladtahanian/V2RayScrapeByCountry/refs/heads/main/output_configs/Trojan.txt",
        "https://raw.githubusercontent.com/miladtahanian/V2RayScrapeByCountry/refs/heads/main/output_configs/Tuic.txt",
        "https://raw.githubusercontent.com/miladtahanian/V2RayScrapeByCountry/refs/heads/main/output_configs/Vless.txt",
        "https://raw.githubusercontent.com/miladtahanian/V2RayScrapeByCountry/refs/heads/main/output_configs/Vmess.txt",
        "https://raw.githubusercontent.com/miladtahanian/V2RayScrapeByCountry/refs/heads/main/output_configs/WireGuard.txt"
    ]

    decoded_links = decode_links(links)
    decoded_dir_links = decode_dir_links(dir_links)
    combined_data = decoded_links + decoded_dir_links
    merged_configs = filter_for_protocols(combined_data, protocols)

    output_filename = os.path.join(output_folder, "All_Configs_Sub.txt")
    filename1 = os.path.join(output_folder, "All_Configs_base64_Sub.txt")
    
    if os.path.exists(output_filename):
        os.remove(output_filename)
    if os.path.exists(filename1):
        os.remove(filename1)

    for i in range(20):
        filename = os.path.join(output_folder, f"Sub{i}.txt")
        if os.path.exists(filename):
            os.remove(filename)
        filename1 = os.path.join(base64_folder, f"Sub{i}_base64.txt")
        if os.path.exists(filename1):
            os.remove(filename1)

    with open(output_filename, "w") as f:
        f.write(fixed_text)
        for config in merged_configs:
            f.write(config + "\n")

    with open(output_filename, "r") as f:
        lines = f.readlines()

    num_lines = len(lines)
    max_lines_per_file = 500
    num_files = (num_lines + max_lines_per_file - 1) // max_lines_per_file

    for i in range(num_files):
        profile_title = f"🆓 Git:tahmaseb73 | Sub{i+1} 🔥"
        encoded_title = base64.b64encode(profile_title.encode()).decode()
        custom_fixed_text = f"""#profile-title: base64:{encoded_title}
        #profile-update-interval: 1
        #subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
        #support-url: https://github.com/tahmaseb73/v2ray-configs
        #profile-web-page-url: https://github.com/tahmaseb73/v2ray-configs
        """

        input_filename = os.path.join(output_folder, f"Sub{i + 1}.txt")
        with open(input_filename, "w") as f:
            f.write(custom_fixed_text)
            start_index = i * max_lines_per_file
            end_index = min((i + 1) * max_lines_per_file, num_lines)
            for line in lines[start_index:end_index]:
                f.write(line)

        with open(input_filename, "r") as input_file:
            config_data = input_file.read()
        
        output_filename = os.path.join(base64_folder, f"Sub{i + 1}_base64.txt")
        with open(output_filename, "w") as output_file:
            encoded_config = base64.b64encode(config_data.encode()).decode()
            output_file.write(encoded_config)

if __name__ == "__main__":
    main()u
