## Projeto - Ambiente de extração de dados do Twitter

Essa é uma aplicação que obtem dados do twitter e armazena as informações em um banco de dados.

## Documentação de arquitetura

![Arquitetura](https://github.com/jcnoliveira/TwitterAPI/blob/master/recursos/componetes.png)

1. Flask API - http://localhost:5050

API desenvolvida em Python com flask. Roda em cima de um container dorcker.

2. MongoDB - localhost:27017

MongoDB, utilizado como banco NoSQL para armazenar e resgatar informações do projeto.

3. Mongo Express - http://localhost:8081

IDE Mongo Web que pode ser acessada vara verificar informações armazenadas.

4. Elasticsearch - http://localhost:9200/

Servidor elasticsearch utilizado para armazenamento de logs do projeto.

5. Kibana - http://localhost:5601/

Servidor kibana utilizado para vizualizar os logs de forma amigavel.

6. Prometheus - localhost:9090

Servidor aplicado armazenar metricas de execução [Não finalizado]

7. Grafana - http://localhost:3060/

Servidor de vizualização de metricas do Prometheus [Nao finalizado]




## Rollout! Implantação

1. Para executar o ambiente, você deve ter os seguintes componetes:

* [Docker](https://docs.docker.com/docker-for-windows/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Postman](https://www.postman.com/downloads/)

2. Em um repositório de sua escolha, rode o seguinte comando para fazer download do prjeto

    ```
    git clone https://github.com/jcnoliveira/TwitterAPI.git
    cd TwitterAPI
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

O microserviço desse projeto está configurado para responder na seguinte URL


    ```
    http://localhost:5050
    ```

Na pasta "postman/" deste projeto você encontrará um arquivo json que pode ser importado para o seu Postman

Abaixo detalharemos a função de cada método desse serviço.

### POST

1. Busca tweets - /buscatweets

Esse recurso, utilizando o método POST, é responsabel por carregar dos dados no MongoDB de acordo com as Hashtags do projeto.
A url é

    ```
    http://localhost:5050/buscatweets
    ```

Em caso de sucesso, o seguinte retorno será devolvido:

    ```
    {
        "jobStatus": "string",
        "statusCode": int,
        "timestamp": "datetime"
    }
    ```

![buscatweet](https://github.com/jcnoliveira/TwitterAPI/blob/master/recursos/buscatweet.png)


### Get

1. Tweets por Hora - /relatorio/tweetbyhour/
 
    ```
    {
        "Query": "tweets_by_hour",
        "items": [
            {
                "_id": int (hora), 
                "soma": int
            }, 
            ...
        ]
    }
    ```

![buscatweet](https://github.com/jcnoliveira/TwitterAPI/blob/master/recursos/porhora.png)

2. Tweets por Pais e Assunto - /relatorio/tweetsbycountry/

    ```
    {
        "Query": "tweets_by_country",
        "items": [
            {
                "_id": "string" (hashtag), 
                "lang": 
                [
                    {
                        "lang": "string", 
                        "count": int
                    }, 
                    ...
                ]
            }
        ]
    }
    ```

![buscatweet](https://github.com/jcnoliveira/TwitterAPI/blob/master/recursos/idioma.png)

4. Top 5 Usuários Populares - /relatorio/top5/

    ```
    {
        "Query": "followers_count",
        "items": [
            {
                "username": "string",
                "followers_count": int
            },
            ...
        ]
    }
    ```
![buscatweet](https://github.com/jcnoliveira/TwitterAPI/blob/master/recursos/top.png)

## Logs

Para realizar a parte de logging estou utilizando uma stack elastic.
Abaixo temos duas queries basicas para filtrar dados e seus respectivos comandos curl

As queries podem ser testadas no kibana, através do link
    ```
    http://localhost:5601/app/kibana#/dev_tools/console
    ```

Exemplo de query e comando curl para buscar logs do tipo INFO

    ```
    GET /_search
    {
    "query": {
        "query_string": {
        "query": "INFO",
        "default_field": "levelname"
        }
    }
    }
    curl -XGET "http://es01:9200/_search" -H 'Content-Type: application/json' -d'{  "query": {    "query_string": {      "query": "INFO",      "default_field": "levelname"    }  }}'
    ```

Exemplo de query e comando curl para buscar logs do tipo ERROR

    ```
    GET /_search
    {
    "query": {
        "query_string": {
        "query": "ERROR",
        "default_field": "levelname"
        }
    }
    }
    curl -XGET "http://es01:9200/_search" -H 'Content-Type: application/json' -d'{  "query": {    "query_string": {      "query": "ERROR",      "default_field": "levelname"    }  }}'
    ```

Após acessar a url do kibana, urilize uma das queries acima. O resultado deve ser conforme o print abaixo.

![kibana](https://github.com/jcnoliveira/TwitterAPI/blob/master/recursos/kibana.png)
