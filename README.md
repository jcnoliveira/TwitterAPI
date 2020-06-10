## Projeto - Ambiente de extração de dados do Twitter

Essa é uma aplicação que obtem dados do twitter e armazena as informações em um banco de dados.

## Documentação de arquitetura
![ECR Repo](https://github.com/jcnoliveira/TwitterAPI/blob/master/recursos/componetes.png)




## Rollout! Implantação

1. Para executar o ambiente, você deve ter os seguintes componetes:

* [Docker](https://docs.docker.com/docker-for-windows/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Postman](https://www.postman.com/downloads/)

2. Em um repositório de sua escolha, rode o seguinte comando para fazer download do prjeto
    ```
    git clone https://github.com/aws-samples/amazon-chime-sdk-recording-demo.git
    cd amazon-chime-sdk-recording-demo
    ```

3. Para preparar o docker a partir do dockerfile do projeto, execute o seguinte comando
    ```
    docker-compose build
    ```

4. Após o build, execute o seguinte comando para iniciar o ambiente
    ```
    docker-compose up -d
    ```
5. Após aguardar alguns instantes, enquanto os serviços são iniciados, você poderá ir para a proxima etapa


## Documentação das APIs

## Logs