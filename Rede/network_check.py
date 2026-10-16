import socket
import sys

def check(host: str, port: int) -> None:
    try:
        addresses = sorted({item[4][0] for item in socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)})
        print("DNS:", ", ".join(addresses))
        with socket.create_connection((host, port), timeout=3):
            print(f"TCP {host}:{port}: conectado")
    except OSError as error:
        print(f"Falha de conexão: {error}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Uso: python network_check.py host porta")
    check(sys.argv[1], int(sys.argv[2]))
