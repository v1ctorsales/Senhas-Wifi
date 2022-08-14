import subprocess

def get_wifi_profiles():
    print("Olá, essa aplicação foi desenvolvida por Victor Sales.\n\n Redes Wi-fi conectadas e senhas:" "\n")
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    data = meta_data.decode("utf-8", errors='replace')
    data = data.split("\n")
    names = []
    for line in data:
        if "Todos os Perfis de" in line:
            name = line.split(":")[1]
            names.append(name[1:-1])
    return names

for name in get_wifi_profiles():
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', name, 'key=clear'])
    data = meta_data.decode("utf-8", errors='replace')
    data = data.split("\n")
    names =[]
    for line in data:
        if "da Chave" in line:
            password = line.split(":")[1]
    print (name , " : " , password)

print("\n" "Para mais informações acesse: www.victorsales.com.br" "\n")
input()
