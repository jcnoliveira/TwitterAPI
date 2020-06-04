FROM ubuntu:18.04

# Copia .Jar para dentro da imagem
# COPY . /opt/java

# Define a diretorio que será usado como referencia no EntryPoint
WORKDIR /opt/python

# Executa update e instalação de softwares essencias 
RUN apt-get -y update && \
    apt-get install -y software-properties-common && \
    apt -y autoclean && \
    apt -y dist-upgrade && \
    apt-get install -y build-essential

# Ajusta TimeZone
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

# Instala python e outras dependencias
RUN apt-get install python3 python3-pip groff  -y

# Instala bibliotecas Python
RUN pip3 install awscli && \
    pip3 install boto3 && \
    pip3 install pymysql && \
    pip3 install mysql-connector-python 

# Limpeza de arquivos de instalação
RUN apt-get autoclean && \
    apt-get clean

####################################
RUN apt-get install nano -y && \
    apt-get install curl -y && \
    mkdir log && \
    touch log/teste.txt

# ENTRYPOINT python3 teste_script.py