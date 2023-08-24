# APP BLX
### App para anúncio e vendas de produtos na vizinhança (bairro/cidades/municípios).

# Funcionalidades:
* Qualquer pessoa poderá anunciar produtos
* Qualquer pessoa poderá fazer pedidos dos produtos anunciados
* Uma pessoa tem:
  * nome
  * telefone whatsapp
  * senha(?)
* Um produto tem:
  * nome
  * detalhamento
  * preço
  * disponível? (sim/não)
  * fotos(?)
* Um Pedido tem:
  * Produto
  * Pessoa que está pedindo
  * Quantidade
  * Local de entrega
  * Entrega ou retirada
  * Observações(sabor,horáriode entrega, troco, etc)
* Cada usuário terá uma lista de pedidos recebidos e pedidos feitos
* O pedido deverá ser aceito pelo vendedor
* O comprador poderá acompanhar seus pedidos:
    * Status(Feito, Aceito)
 
# Arquitetura e Ferramentas
* Python + FastApi
* Será uma API REST
* Banco de Dados: Postgres
* MVC
* Domain Driven Design e Arquitetura Limpa (Clean Architecture)
