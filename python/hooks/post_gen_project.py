import subprocess
import sys
import os

GREEN = "\033[0;32m"
RESET = "\033[0m"

def run_command(command, description):
    print(f"{GREEN}--> {description}...{RESET}")
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Aviso: Falha ao executar '{command}'. Erro: {e}")

if __name__ == "__main__":
    # 1. Iniciar o Git
    run_command("git init", "A inicializar repositório Git")
    
    # 2. Adicionar ficheiros iniciais ao staging
    run_command("git add .", "A adicionar ficheiros ao Git")

    print(f"\n{GREEN}Projeto criado com sucesso!{RESET}")