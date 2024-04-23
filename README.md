Esse trabalho é para vaga de Python/Django.

O site está hospedado em:

> http://34.136.163.239:5173/

user: admin
pass: admin

## Backend

O backend foi desenvolvimento em:
* Python
* Django
* Django Rest Framework

A arquitetura do backend foi baseada no Clean Architecture, com o objetivo de desacoplar o código, por exemplo:

O fluxo do processamento de cada requisição segue a seguinte order:

Cliente --> View --> UseCase --> Entity --> Dados

A `View` implementa a comunição com o cliente.
O `UseCase` possui as regras de negócios.
A `Entity` possui a interface com o banco de dados.

Neste projeto, eu criei apenas um tipo de Entity o `ORM` que é nativo do django. Mas note que se houver necessidade é possível criar uma outra Entity para buscar dados utilizando outra tecnologia, como o `GraphQL`, busca em Arquivo e etc, sem precisar alterar as camadas anteriores (`View` e `UseCases`).

Aqui estão alguns exemplos de como os dados JSON podem ser retornados desses endpoints:

1. `producer/`: Este endpoint retorna uma lista de todos os produtores. Um exemplo de resposta pode ser:
(POST, GET)

```json
[
    {
        "id": 1,
        "name": "Produtor 1",
        "cpfCnpj": "123.456.789-00"
    },
    {
        "id": 2,
        "name": "Produtor 2",
        "cpfCnpj": "987.654.321-00"
    }
]
```

2. `producer/<int:pk>`: Este endpoint retorna os detalhes de um produtor específico. Um exemplo de resposta pode ser:
(GET, PUT, DELETE)

```json
{
    "id": 1,
    "name": "Produtor 1",
    "cpfCnpj": "123.456.789-00"
}
```

3. `farm/`: Este endpoint retorna uma lista de todas as fazendas. Um exemplo de resposta pode ser:
(POST)

```json
[
    {
        "id": 1,
        "farm_name": "Fazenda 1",
        "producer_id": 1,
        "city": "Cidade 1",
        "state": "Estado 1",
        "total_area_hectares": 100
    },
    {
        "id": 2,
        "farm_name": "Fazenda 2",
        "producer_id": 2,
        "city": "Cidade 2",
        "state": "Estado 2",
        "total_area_hectares": 200
    }
]
```

4. `farm-list/<int:pk_producer>`: Este endpoint retorna uma lista de todas as fazendas de um produtor específico. Um exemplo de resposta pode ser:
(GET)

```json
[
    {
        "id": 1,
        "farm_name": "Fazenda 1",
        "producer_id": 1,
        "city": "Cidade 1",
        "state": "Estado 1",
        "total_area_hectares": 100
    }
]
```

5. `farm/<int:pk>`: Este endpoint retorna os detalhes de uma fazenda específica. Um exemplo de resposta pode ser:
(GET, PUT, DELETE)

```json
{
    "id": 1,
    "farm_name": "Fazenda 1",
    "producer_id": 1,
    "city": "Cidade 1",
    "state": "Estado 1",
    "total_area_hectares": 100
}
```

6. `area/`: Este endpoint retorna uma lista de todas as áreas. Um exemplo de resposta pode ser:
(GET, POST)

```json
[
    {
        "id": 1,
        "farm_id": 1,
        "area_type": "Plantada",
        "area_hectares": 50,
        "crops": "Milho"
    },
    {
        "id": 2,
        "farm_id": 2,
        "area_type": "Não Plantada",
        "area_hectares": 100,
        "crops": "Soja"
    }
]
```

7. `area-list/<int:pk_farm>`: Este endpoint retorna uma lista de todas as áreas de uma fazenda específica. Um exemplo de resposta pode ser:
(GET)

```json
[
    {
        "id": 1,
        "farm_id": 1,
        "area_type": "Plantada",
        "area_hectares": 50,
        "crops": "Milho"
    }
]
```

8. `area/<int:pk>`: Este endpoint retorna os detalhes de uma área específica. Um exemplo de resposta pode ser:
(GET, PUT, DELETE)

```json
{
    "id": 1,
    "farm_id": 1,
    "area_type": "Plantada",
    "area_hectares": 50,
    "crops": "Milho"
}
```

9. `dashboard/total-farm/`: Este endpoint retorna o total de fazendas. Um exemplo de resposta pode ser:
(GET)

```json
{
    "total_farm": 2
}
```

10. `dashboard/total-area/`: Este endpoint retorna o total de áreas. Um exemplo de resposta pode ser:
(GET)

```json
{
    "total_area": 2
}
```

11. `dashboard/total-state/`: Este endpoint retorna o total por estado. Um exemplo de resposta pode ser:
(GET)

```json
[
    {
        "state": "Estado 1",
        "total": 1
    },
    {
        "state": "Estado 2",
        "total": 1
    }
]
```

12. `dashboard/total-crop/`: Este endpoint retorna o total por cultura. Um exemplo de resposta pode ser:
(GET)

```json
[
    {
        "crop": "Milho",
        "total": 1
    },
    {
        "crop": "Soja",
        "total": 1
    }
]
```

13. `dashboard/total-type/`: Este endpoint retorna o total por tipo de área. Um exemplo de resposta pode ser:
(GET)

```json
[
    {
        "type": "Plantada",
        "total": 1
    },
    {
        "type": "Não Plantada",
        "total": 1
    }
]
```
### TESTES

O backend está com **97% do código coberto** por test

| Name                              | Stmts | Miss | Cover |   |
|-----------------------------------|-------|------|-------|---|
| backend/__init__.py               | 0     | 0    | 100%  |   |
| backend/settings.py               | 25    | 0    | 100%  |   |
| backend/urls.py                   | 6     | 0    | 100%  |   |
| farmer/__init__.py                | 0     | 0    | 100%  |   |
| farmer/admin.py                   | 5     | 0    | 100%  |   |
| farmer/apps.py                    | 4     | 0    | 100%  |   |
| farmer/entities/__init__.py       | 0     | 0    | 100%  |   |
| farmer/entities/entity_base.py    | 8     | 2    | 75%   |   |
| farmer/entities/orm.py            | 46    | 0    | 100%  |   |
| farmer/migrations/0001_initial.py | 6     | 0    | 100%  |   |
| farmer/migrations/__init__.py     | 0     | 0    | 100%  |   |
| farmer/models.py                  | 23    | 3    | 87%   |   |
| farmer/serializers.py             | 28    | 4    | 86%   |   |
| farmer/tests.py                   | 301   | 0    | 100%  |   |
| farmer/urls.py                    | 3     | 0    | 100%  |   |
| farmer/usecases/__init__.py       | 0     | 0    | 100%  |   |
| farmer/usecases/farm.py           | 57    | 0    | 100%  |   |
| farmer/usecases/producer.py       | 18    | 0    | 100%  |   |
| farmer/views.py                   | 122   | 9    | 93%   |   |
| manage.py                         | 12    | 2    | 83%   |   |
| TOTAL                             | 664   | 20   | 97%   |   |


Para executar os testes, execute:

> coverage run ./manage.py test

> coverage report

## Frontend

O frontend foi desenvolvimento em React + Redux + Bootstrap.

## Deploy

O app está hospedado em um cluster kubernetes no Google Cloud Platform.

