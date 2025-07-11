import os
import time
from datetime import datetime, timedelta
import pytz

def get_country_configs(configs, country_codes):
    country_data = {}
    for country, code in country_codes.items():
        country_configs = [c for c in configs if code.lower() in c.lower() or country.lower() in c.lower()]
        if country_configs:
            country_data[country] = country_configs
    return country_data

def count_configs_in_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return sum(1 for line in f if line.strip() and not line.startswith("#"))
    except FileNotFoundError:
        return 0

def main():
    # مسیرها
    output_folder = os.path.abspath(os.path.join(os.getcwd(), ".."))
    protocol_folder = os.path.join(output_folder, "Splitted-By-Protocol")
    country_folder = os.path.join(output_folder, "Countries")
    os.makedirs(country_folder, exist_ok=True)

    # پروتکل‌ها
    protocols = ["vmess", "vless", "trojan", "ss", "ssr", "hy2", "tuic", "warp://"]
    protocol_files = {
        protocol: os.path.join(protocol_folder, f"{protocol}.txt") for protocol in protocols
    }

    # خواندن تمام کانفیگ‌ها
    all_configs_file = os.path.join(output_folder, "All_Configs_Sub.txt")
    configs = []
    try:
        with open(all_configs_file, "r", encoding="utf-8") as f:
            configs = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        print("فایل All_Configs_Sub.txt پیدا نشد")
        return

    # کد کشورها (پرچم و نام)
    country_codes = {
        "Afghanistan": "af", "Albania": "al", "Argentina": "ar", "Armenia": "am", "Australia": "au",
        "Austria": "at", "Bahrain": "bh", "Belarus": "by", "Belgium": "be", "Belize": "bz",
        "Bolivia": "bo", "Brazil": "br", "Bulgaria": "bg", "Cambodia": "kh", "Canada": "ca",
        "CentralAfricanRepublic": "cf", "Chile": "cl", "China": "cn", "Colombia": "co",
        "CostaRica": "cr", "Cyprus": "cy", "Czechia": "cz", "Denmark": "dk", "Ecuador": "ec",
        "EquatorialGuinea": "gq", "Estonia": "ee", "Finland": "fi", "France": "fr", "Georgia": "ge",
        "Germany": "de", "Greece": "gr", "Hungary": "hu", "Iceland": "is", "India": "in",
        "Indonesia": "id", "Iran": "ir", "Iraq": "iq", "Ireland": "ie", "Israel": "il",
        "Italy": "it", "Japan": "jp", "Kazakhstan": "kz", "Laos": "la", "Latvia": "lv",
        "Lithuania": "lt", "Luxembourg": "lu", "Malaysia": "my", "Malta": "mt", "Mauritius": "mu",
        "Mexico": "mx", "Moldova": "md", "Montenegro": "me", "Namibia": "na", "Netherlands": "nl",
        "NorthMacedonia": "mk", "Norway": "no", "Oman": "om", "Peru": "pe", "Philippines": "ph",
        "Poland": "pl", "Portugal": "pt", "Romania": "ro", "Russia": "ru", "Samoa": "ws",
        "Seychelles": "sc", "Singapore": "sg", "Slovakia": "sk", "Slovenia": "si", "SouthAfrica": "za",
        "SouthKorea": "kr", "SouthSudan": "ss", "Spain": "es", "Sweden": "se", "Switzerland": "ch",
        "Taiwan": "tw", "Thailand": "th", "TrinidadAndTobago": "tt", "Turkey": "tr"
    }
    country_names_fa = {
        "Afghanistan": "افغانستان", "Albania": "آلبانی", "Argentina": "آرژانتین", "Armenia": "ارمنستان",
        "Australia": "استرالیا", "Austria": "اتریش", "Bahrain": "بحرین", "Belarus": "بلاروس",
        "Belgium": "بلژیک", "Belize": "بلیز", "Bolivia": "بولیوی", "Brazil": "برزیل",
        "Bulgaria": "بلغارستان", "Cambodia": "کامبوج", "Canada": "کانادا", "CentralAfricanRepublic": "جمهوری آفریقای مرکزی",
        "Chile": "شیلی", "China": "چین", "Colombia": "کلمبیا", "CostaRica": "کاستاریکا",
        "Cyprus": "قبرس", "Czechia": "جمهوری چک", "Denmark": "دانمارک", "Ecuador": "اکوادور",
        "EquatorialGuinea": "گینه استوایی", "Estonia": "استونی", "Finland": "فنلاند", "France": "فرانسه",
        "Georgia": "گرجستان", "Germany": "آلمان", "Greece": "یونان", "Hungary": "مجارستان",
        "Iceland": "ایسلند", "India": "هند", "Indonesia": "اندونزی", "Iran": "ایران",
        "Iraq": "عراق", "Ireland": "ایرلند", "Israel": "اسرائیل", "Italy": "ایتالیا",
        "Japan": "ژاپن", "Kazakhstan": "قزاقستان", "Laos": "لائوس", "Latvia": "لتونی",
        "Lithuania": "لیتوانی", "Luxembourg": "لوکزامبورگ", "Malaysia": "مالزی", "Malta": "مالت",
        "Mauritius": "موریس", "Mexico": "مکزیک", "Moldova": "مولداوی", "Montenegro": "مونته‌نگرو",
        "Namibia": "نامیبیا", "Netherlands": "هلند", "NorthMacedonia": "مقدونیه شمالی", "Norway": "نروژ",
        "Oman": "عمان", "Peru": "پرو", "Philippines": "فیلیپین", "Poland": "لهستان",
        "Portugal": "پرتغال", "Romania": "رومانی", "Russia": "روسیه", "Samoa": "ساموآ",
        "Seychelles": "سیشل", "Singapore": "سنگاپور", "Slovakia": "اسلواکی", "Slovenia": "اسلوونی",
        "SouthAfrica": "آفریقای جنوبی", "SouthKorea": "کره جنوبی", "SouthSudan": "سودان جنوبی",
        "Spain": "اسپانیا", "Sweden": "سوئد", "Switzerland": "سوئیس", "Taiwan": "تایوان",
        "Thailand": "تایلند", "TrinidadAndTobago": "ترینیداد و توباگو", "Turkey": "ترکیه"
    }

    # تولید فایل‌های کشورها
    country_data = get_country_configs(configs, country_codes)
    for country, country_configs in country_data.items():
        country_file = os.path.join(country_folder, f"{country}.txt")
        with open(country_file, "w", encoding="utf-8") as f:
            for config in country_configs:
                f.write(config + "\n")

    # شمارش تعداد کانفیگ‌ها برای پروتکل‌ها
    protocol_counts = {protocol: count_configs_in_file(file) for protocol, file in protocol_files.items()}

    # شمارش تعداد کانفیگ‌ها برای کشورها
    country_counts = {country: count_configs_in_file(os.path.join(country_folder, f"{country}.txt"))
                     for country in country_data}

    # منابع
    sources = [
        "https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/mix",
        "https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt",
        "https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/reality",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vless",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vmess",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/trojan",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/shadowsocks",
        "https://raw.githubusercontent.com/ts-sf/fly/main/v2",
        "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2",
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

    # تولید لینک‌های SubX.txt
    sub_links = []
    for i in range(8):  # تا Sub8.txt
        sub_file = os.path.join(output_folder, f"Sub{i+1}.txt")
        if os.path.exists(sub_file):
            sub_links.append(f"https://raw.githubusercontent.com/tahmaseb73/ConfigScavenger/main/Sub{i+1}.txt")

    # تولید README
    tehran_tz = pytz.timezone("Asia/Tehran")
    current_time = datetime.now(tehran_tz).strftime("%Y-%m-%d %H:%M:%S %z")
    readme_content = f"""# 📊 نتایج استخراج (آخرین به‌روزرسانی: {current_time})

این فایل به صورت خودکار ایجاد شده است.

**توضیح:** فایل‌های کشورها فقط شامل کانفیگ‌هایی هستند که نام/پرچم کشور (با رعایت مرز کلمه برای مخفف‌ها) در **اسم کانفیگ** پیدا شده باشد. اسم کانفیگ ابتدا از بخش `#` لینک و در صورت نبود، از نام داخلی (برای Vmess/SSR) استخراج می‌شود.

**نکته:** کانفیگ‌هایی که به شدت URL-Encode شده‌اند (حاوی تعداد زیادی `%25`، طولانی یا دارای کلمات کلیدی خاص) از نتایج حذف شده‌اند.

## 📁 فایل‌های پروتکل‌ها

| پروتکل | تعداد کل | لینک |
|---|---|---|
"""
    for protocol in protocols:
        count = protocol_counts.get(protocol, 0)
        if count > 0:
            readme_content += f"| {protocol.capitalize()} | {count} | <a href=\"https://raw.githubusercontent.com/tahmaseb73/ConfigScavenger/main/Splitted-By-Protocol/{protocol}.txt\" onclick=\"navigator.clipboard.writeText(this.href);alert('لینک کپی شد!')\">`{protocol}.txt`</a> |\n"

    readme_content += """
## 🔗 لینک‌های اشتراک

لینک‌های عضویت در اینجا در اختیار شما قرار دارد:

**تمام پیکربندی‌های جمع‌آوری‌شده:**  
<a href="https://raw.githubusercontent.com/tahmaseb73/ConfigScavenger/main/All_Configs_Sub.txt" onclick="navigator.clipboard.writeText(this.href);alert('لینک کپی شد!')">`All_Configs_Sub.txt`</a>

**اگر لینک بالا کار نکرد، پیکربندی‌های پایه ۶۴ بیتی را امتحان کنید:**  
<a href="https://raw.githubusercontent.com/tahmaseb73/ConfigScavenger/main/All_Configs_base64_Sub.txt" onclick="navigator.clipboard.writeText(this.href);alert('لینک کپی شد!')">`All_Configs_base64_Sub.txt`</a>

**تقسیم بر اساس پروتکل:**  
"""
    protocol_names_fa = {
        "vless": "vless", "vmess": "vmess", "ss": "ss", "ssr": "ssr",
        "trojan": "trojan", "hy2": "hy2", "tuic": "tuic", "warp://": "warp"
    }
    for protocol in protocols:
        if protocol_counts.get(protocol, 0) > 0:
            readme_content += f"**{protocol_names_fa.get(protocol, protocol.capitalize())}:**  \n<a href=\"https://raw.githubusercontent.com/tahmaseb73/ConfigScavenger/main/Splitted-By-Protocol/{protocol}.txt\" onclick=\"navigator.clipboard.writeText(this.href);alert('لینک کپی شد!')\">`{protocol}.txt`</a>\n\n"

    readme_content += "**تقسیم بر ۵۰۰ تعداد پیکربندی:**  \n"
    for i, sub_link in enumerate(sub_links, 1):
        readme_content += f"**فهرست پیکربندی {i}:**  \n<a href=\"{sub_link}\" onclick=\"navigator.clipboard.writeText(this.href);alert('لینک کپی شد!')\">`Sub{i}.txt`</a>\n\n"

    readme_content += """
## 🌍 فایل‌های کشورها (حاوی کانفیگ)

| کشور | تعداد کانفیگ مرتبط | لینک |
|---|---|---|
"""
    for country in sorted(country_counts.keys()):
        count = country_counts[country]
        if count > 0:
            flag = f'<img src="https://flagcdn.com/w20/{country_codes[country]}.png" width="20" alt="{country} flag">'
            readme_content += f"| {flag} {country} ({country_names_fa[country]}) | {count} | <a href=\"https://raw.githubusercontent.com/tahmaseb73/ConfigScavenger/main/Countries/{country}.txt\" onclick=\"navigator.clipboard.writeText(this.href);alert('لینک کپی شد!')\">`{country}.txt`</a> |\n"

    readme_content += """
## 🔗 منابع

| منبع | نوع |
|---|---|
"""
    for source in sources:
        source_type = "Base64" if source in sources[:10] else "متنی"
        readme_content += f"| [{source}]({source}) | {source_type} |\n"

    # ذخیره README
    with open(os.path.join(output_folder, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    main()
