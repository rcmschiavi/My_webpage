var pedidos
var produtos
var evento

var selectedOrderId
var selectedItemId

var nonAddedItemsId
var productsIdAtOrder

function loadOrderData(produtos, pedidos){

    pedidos = pedidos
    produtos = produtos 

    var select = document.getElementById('select-order');
    select.innerHTML = ""

    for (var i = 1; i <= pedidos.length; i++) {
        var option = '<option value="'+ i + '" >Pedido ' + pedidos[i-1].order_id + '</option>';
        select.insertAdjacentHTML( 'beforeend', option );
    }
    onSelectOrderChange();
}

function onSelectOrderChange(){
    var selectOrder = document.getElementById('select-order');
    var selectItem = document.getElementById('select-item');
    var selectItemAdd = document.getElementById('select-item-add');
    selectItem.innerHTML = ""
    selectItemAdd.innerHTML = ""
    productsIdAtOrder = []
    nonAddedItemsId = []
    for (var k = 0; k < pedidos[selectOrder.value -1].order_details.length; k++) {
        var option = '<option value="'+ k + '" >' + pedidos[selectOrder.value -1].order_details[k].item + '</option>';
        selectItem.insertAdjacentHTML( 'beforeend', option );
        productsIdAtOrder.push(pedidos[selectOrder.value -1].order_details[k].product_id)
    }
    for(var i = 0; i < produtos.length; i++){
        var isAtOrder = false;
        for(var k = 0; k < productsIdAtOrder.length; k++){
            if(produtos[i].id === productsIdAtOrder[k]){
                isAtOrder = true;
            }
        }
        if(!isAtOrder){
            var option = '<option value="'+ i + '" >' + produtos[i].item + '</option>';
            selectItemAdd.insertAdjacentHTML( 'beforeend', option );
            nonAddedItemsId.push(i)
        }
    }
    onSelectEditItemChange();
    onSelectAddItemChange();
}

function onSelectEditItemChange(){
    var selectOrder = document.getElementById('select-order');
    var selectItem = document.getElementById('select-item');
    var selectItemAdd = document.getElementById('select-item-add');
    try {
    selectedOrderId = pedidos[selectOrder.value - 1].order_id
    selectedItemId = pedidos[selectOrder.value - 1].order_details[selectItem.value].product_id
    var priceField = document.getElementById('price-input-item-selected');
    var amountField = document.getElementById('amount-input-item-selected');
    priceField.value = pedidos[selectOrder.value - 1].order_details[selectItem.value].price
    amountField.value = pedidos[selectOrder.value - 1].order_details[selectItem.value].amount
    amountField.step = produtos[selectedItemId - 1].multiplier
    amountField.min = produtos[selectedItemId - 1].multiplier
    }
    catch(err) {
        console.log("Sem itens no pedido")
    }
}

function onSelectAddItemChange(){
    var selectOrder = document.getElementById('select-order');
    var selectItem = document.getElementById('select-item');
    var selectItemAdd = document.getElementById('select-item-add');
    //selectedOrderId = pedidos[selectOrder.value - 1].order_id
    //selectedItemId = pedidos[selectOrder.value - 1].order_details[selectItemAdd.value].product_id
    var priceField = document.getElementById('price-input-item-selected-add');
    var amountField = document.getElementById('amount-input-item-selected-add');
    priceField.value = produtos[selectItemAdd.value].suggested_price
    amountField.value = produtos[selectItemAdd.value].multiplier
    amountField.step = produtos[selectItemAdd.value].multiplier
    amountField.min = produtos[selectItemAdd.value].multiplier

}

function addItemToOrder(){
    var selectItemAdd = document.getElementById('select-item-add');
    var priceField = document.getElementById('price-input-item-selected-add');
    var amountField = document.getElementById('amount-input-item-selected-add');
    var selectOrder = document.getElementById('select-order');
    orderId = selectOrder.value;
    itemId = parseInt(selectItemAdd.value) + 1;
    price = priceField.value;
    amount = amountField.value;
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url:'add_item',
        type: "POST",
        data: JSON.stringify({order_id: orderId , item_id: itemId, price: price, amount: amount}),
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success:function(response){
            window.alert("Item adicionado! Atualize a página para carregar as alterações.");
        },
        complete:function(){},
        error:function (xhr, textStatus, thrownError){window.alert('Erro');}
            });
}

function removeItem(){
    var selectItem = document.getElementById('select-item');
    var priceField = document.getElementById('price-input-item-selected-add');
    var amountField = document.getElementById('amount-input-item-selected-add');
    var selectOrder = document.getElementById('select-order');
    orderId = selectOrder.value - 1;
    orderDetails = pedidos[orderId].order_details;
    itemOrderId = orderDetails[selectItem.value].item_order_id;
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url:'remove_item',
        type: "POST",
        data: JSON.stringify({item_order_id: itemOrderId}),
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success:function(response){
            window.alert("Item removido! Atualize a página para carregar as alterações.");
        },
        complete:function(){},
        error:function (xhr, textStatus, thrownError){window.alert('Erro');}
            });
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