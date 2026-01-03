import socket
import sys

print("-" • 50)
print("-" • 50)
print(" Python Port Tarama Aracana Hos Geldiniz")
print("-" • 50)

# Kullanacsdan hadef IP veya donain alna
hedef - input("Tarama yapılacak IP veya Domain (örn: 127.0.0.1): )
try:
    # Eğer domain girildiyse IP*ye cevirir (örn: google-com -> 142.250...)
    hedef Jp - socket.gethostbyname(hedef)
except socket-galerror:
    print(" \n[|] Hata: Host cözülemedi. Lütfen gecerl1 bir adres girin.") sys-exit()
    # Kullanacadan port aralaga alma
try:
    baslangls_gort • Int(Input("Baslangıc V/u (örn: 1): ")
    bitis_port • imt(input("Bitis Portu (örn: 1000): "))
sys.exit()

    print(f"\n[ ] [hedef (p) taransyor... ")
    print(f"[*] Baslangic: (baslangic port) | Bitis: (bitis_port)\n")
try:
    for port in range(baslangic port, bitis port • 1):
    s - socket.socket(socket.AF_INET, socket.SOCK_STREAN)
    s.settimeout(0.5) * Tarama hazz için süre (saniye)
    
    sonuc - s-connect_ex((hedef_ip, port))
    
    if sonuc -- 0:
        print(f[+] Port (port): ACIK*)
        
    s.close()
    
except KeyboardInterrupt:
    print("\o[1] Tarama kullanaca tarafından durduruldu. ")
sys-exit()
    except socket.error:
    print("/n[1] Sunucuya bağlamlamada. ")

print(In--- Tarama Tamanlanda ...)
If _name, -"maln'
