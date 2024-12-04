# Criar diretório para o projeto
mkdir my-vercel-project
cd my-vercel-project

# Inicialize o repositório
git init

# Crie o arquivo Python (verificar_nicks.py) e o arquivo requirements.txt
touch api/verificar_nicks.py
touch requirements.txt

# Adicione o código necessário no verificar_nicks.py
# E adicione 'requests' no requirements.txt

# Adicione os arquivos ao Git
git add .

# Faça o commit
git commit -m "Primeiro commit"

# Adicione o repositório remoto do GitHub
git remote add origin <url-do-repositorio-no-github>

# Envie para o GitHub
git push -u origin master
