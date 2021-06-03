var clientes
var produtos

var orderRegistered = false;
/* Salvar o nome das imagens como uma coluna no respectivo item pode ser interessante*/
image_list = ["milenium.svg","x-wing.svg", "death-star-bold.svg", "TIE_fighter.svg", "lightsaber.svg", "dlt-19.png", "DL-44.png"] 
profilePicList = ["dart.jpg","obiwan.jpg", "luke.png", "palpatine.jpg", "solo.png"]
returnRatePics = ["bad_rate.png", "good_rate.jpg", "great_rate.jpeg"]

function loadData(clientes, produtos){
    /* Popula os elementos com as informações enviadas pelo Django na interface 
        - Popula a lista de seleção de clientes
        - Cria a tabela com os itens e imagens referentes
    */
    clientes = clientes
    produtos = produtos


    var select = document.getElementById('select-client');
    select.innerHTML = ""
    for (var i = 1; i <= clientes.length; i++) {
        var option = '<option value="'+ i + '" >' + clientes[i-1].name + '</option>';
        select.insertAdjacentHTML( 'beforeend', option );
    }
    var tableElement = document.getElementById('list-products');
    tableElement.innerHTML = ""
    for (var i = 1; i <= produtos.length; i++) {
        var image = '<img style="max-height: 200px;" src="/static/pedidos/images/products/' + image_list[i-1] +'" alt="">';
        var imageTextCell = '<td>'+image+produtos[i-1].item+'</td>'
        var priceCell = '<td><input class="w3-input points" type="number" id="price-input-'+ i +'" name="item-'+produtos[i-1].id+'-price"" step="0.01" value="'+produtos[i-1].suggested_price+'" onchange="checkReturnRate('+ i + ')"></td>'
        var amountCell = '<td><input class="w3-input points" onkeydown="return false;" type="number" id="points" name="item-'+produtos[i-1].id+'-amount" step="'+produtos[i-1].multiplier+'" value="0" min="0"></td>'
        var returnRateCell = '<td><img class="img-rate" id=return-rate-img-' +String(i) + ' src="/static/pedidos/images/extras/good_rate.jpg" alt=""><h6 id=return-rate-text-' +String(i) + '>Boa!</h6></td>'
        var table = '<tr id="product-row-'+ String(i) + '">'+ imageTextCell + priceCell + amountCell + returnRateCell + '</tr>';
        
        tableElement.insertAdjacentHTML( 'beforeend', table );
        checkReturnRate(i)
    }

}

function onSelectClientChange(){
    /* Altera a imagem de perfil para adequar ao cliente selecionado */
    var image = document.getElementById('profile-pic');
    var select = document.getElementById('select-client');
    image.src = "/static/pedidos/images/clients/"+ profilePicList[select.value-1]
}

function checkReturnRate(productRow){
    /* Verifica a categoria de rentabilidade e aplica as propriedades para distinguir */

    var imageCellRate = document.getElementById('return-rate-img-'+String(productRow));
    var returnRateText = document.getElementById('return-rate-text-'+String(productRow));
    var price = parseFloat(document.getElementById('price-input-'+String(productRow)).value);
    var productRowComponent = document.getElementById('product-row-'+String(productRow));
    if(price >= produtos[productRow - 1].return_rate.great){
        imageCellRate.src = "/static/pedidos/images/extras/"+ returnRatePics[2];
        returnRateText.innerHTML = "Rentabilidade ótima!";
        productRowComponent.className = "great"
    }
    else if(price >= produtos[productRow - 1].return_rate.good){
        imageCellRate.src = "/static/pedidos/images/extras/"+ returnRatePics[1];
        returnRateText.innerHTML = "Rentabilidade boa!";
        productRowComponent.className = ""
    }
    else{
        imageCellRate.src = "/static/pedidos/images/extras/"+ returnRatePics[0];
        returnRateText.innerHTML = "Rentabilidade ruim!";
        productRowComponent.className = "bad"
    }
    
}

function createOrder(){
    /* 
        Função que cria o pedido verificando se os itens estão com a rentabilidade "good" ou superior

        Optei por não usar Forms no html pois da forma como o front foi feito
    a integração com o Forms do django dependeria de estrutura de mensagem que 
    o URL encode não permite.[5]

        A garantia de que não será enviado nenhum item com quantidade multipla 
    fora do padrão está escrita nas propriedades dos inputs com a propriedade
    onkeydown="return false;".

        Caso o usuário tente alterar a requisição, o manage_orders.py possui regras para impedir a 
    inserção do item fora do padrão no db. 

        Idealmente deveria ser realizada uma requisição com forms, para o backend validar os itens inseridos
    e retornar se a operação foi concluída ou possui erros e informar o usuário.
    */
    var itensTable = document.getElementById('list-products');
    var orderItemList = []
    var orderHasLowPriceItem = false; 
    for (var i = 0; i < itensTable.rows.length; i++) {
        var itemAmount = itensTable.rows.item(i).cells.item(2).childNodes[0].value
        if (itemAmount>0){
            var itemPrice = itensTable.rows.item(i).cells.item(1).childNodes[0].value
            if (itemPrice>=produtos[i].return_rate.good){
                var productId = produtos[i].id
                var orderDescription = {"id":productId, "price": itemPrice, "amount": itemAmount}
                orderItemList.push(orderDescription)
            }
            else{
                window.alert("Você possui itens com valor de rentabilidade Ruim. Revise os itens em vermelho.");
                orderHasLowPriceItem = true
                break;
            }
        }
    }
    if(!orderHasLowPriceItem){
        if(orderItemList.length === 0){
            window.alert("O pedido não foi finalizado pois nenhum item foi adicionado.");
        }
        else{
            var select = document.getElementById('select-client');
            var client = clientes[select.value-1];
            var csrftoken = getCookie('csrftoken');
            $.ajax({
                url:'save_order',
                type: "POST",
                data: JSON.stringify({client_id: client.id , order_list: orderItemList}),
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                },
                success:function(response){
                    window.alert("Pedido registrado!");
                    // Para evitar que o pedido seja realizado duas vezes, os itens são recarregados com o valor default
                    loadData(clientes, produtos, pedidos);
                    onSelectClientChange();
                },
                complete:function(){},
                error:function (xhr, textStatus, thrownError){window.alert('Erro: ' + xhr.responseJSON['err']);}
                    });
            
        }
    }
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/* Referências:

[1]-https://www.w3schools.com/howto/howto_js_tabs.asp

[2]-https://stackoverflow.com/questions/49461343/how-can-i-add-an-html-option-element-dynamically-to-a-select

[3]-https://www.w3schools.com/tags/att_input_step.asp

[4]-https://www.w3schools.com/jsref/coll_table_cells.asp

[5]-https://www.w3schools.com/jsref/coll_table_rows.asp

[6]-https://stackoverflow.com/questions/28774746/sending-nested-formdata-on-ajax

[7]-https://docs.djangoproject.com/en/1.10/ref/csrf/#ajax

[8]-https://stackoverflow.com/questions/37734658/how-to-send-a-failure-response-from-django-to-ajax



*/