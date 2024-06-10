import os
import subprocess

def install_software():
    software_map = {
        "Office 365": "office365proplus",
        "AnyDesk": "anydesk",
        "Chrome": "googlechrome",
        "Kaspersky": "kaspersky",
        "MicroSIP": "microsip",
        "Teams": "teams"
    }

    try:
        subprocess.check_call(["choco", "-v"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        choco_installed = True
    except subprocess.CalledProcessError:
        choco_installed = False

    if not choco_installed:
        print("Chocolatey não está instalado. Instalando Chocolatey...")
        os.system('@"%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\\chocolatey\\bin"')
        try:
            subprocess.check_call(["choco", "-v"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            print("Erro na instalação do Chocolatey. Saindo do script.")
            return

    for software, package in software_map.items():
        print(f"Instalando {software} ({package})...")
        try:
            subprocess.check_call(["choco", "install", package, "-y"])
            print(f"{software} instalado com sucesso.")
        except subprocess.CalledProcessError:
            print(f"Erro ao instalar {software} ({package}). Verifique o nome do pacote ou sua conexão com a internet.")

    print("Instalação concluída.")

if __name__ == "__main__":
    install_software()
