# Definir a imagem base
FROM node

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar package.json e package-lock.json
COPY package*.json ./

# Instalar dependências
RUN npm install

# Copiar o restante dos arquivos do projeto
COPY . .

# Expor a porta 3000
EXPOSE 3000

# Comando para iniciar o aplicativo
CMD [ "npm", "start" ]