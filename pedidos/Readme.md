# O repositório

Esse arquivo é destinado à equipe técnica da Mercus.

Criei esse repositório para desenvolver minha página de portfólio e tenho implementado algumas coisas no meu tempo livre.
Desenvolvi algumas aplicações de IoT com aquisição de dados de sensores, e no momento estou organizando o frontend da página
para disponibilizar os apps e posts. Posso mostrar um pouco, caso venhamos a conversar

# O teste

Busquei me organizar para entregar a aplicação funcionando na minha página em desenvolvimento. 
[Link da aplicação](https://rodolfoschiavi.pythonanywhere.com/portfolio/app/pedidos).


Durante a semana que desenvolvi, pude me dedicar em média 2h por dia em 6 dias.

## O que utilizei na aplicação

- Django
- HTML
- CSS
- Javascript 

## Recursos

- [x] Criação de pedidos
  - [x] Seleção do cliente
  - [x] Seleção dos itens 
  - [x] Recurso de verificação e notificação de rentabilidade
- [ ] Edição de pedidos
  - [x] Adição de novos intens
  - [x] Remoção de itens
  - [ ] Recurso de verificação e notificação de rentabilidade
- [ ] Testes unitários
  - [x] Testes das queries mais complexas do banco
  - [ ] Testes gerais


## Estrutura da aplicação

```
My_webpage
│
└───Pedidos - Pasta da aplicação
|    │
|    |    insert_itens.py - Script para inserir os itens das tabelas no DB
|    |    manage_orders.py - Regras e métodos de inserção e queries 
|    |    tests.py - Testes unitários referentes à queries no DB
|    │    ... Arquivos autogerados pelo Django
|    |  
│
└───template - Arquivos do front 
|    │
|    └─── pedidos
|    |    |    index.html
|    |
|    └───static - Recursos da interface
|    │
|    |    └─── pedidos - Pasta dos arquivos estáticos do front 
|    |    │    |
|    |    |    └─── css
|    |    |    |
|    |    |    └─── imgs
|    |    |    |
|    |    |    └─── js
```

Diagrama do banco de dados: 

![data_base_diagram](/docs/pedidos_models.png)

# TODO

- [ ] Usar Forms nos inputs do HTML para envio dos pedidos;
- [ ] Utilizar serializers para formatação dos dados para envio para o front;
- [ ] Implementar verificação de rentabilidade na tela de edição de pedidos;
- [ ] Criar a tela de resultados.
