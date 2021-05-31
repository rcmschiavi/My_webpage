var clientes
var produtos
image_list = ["milenium.svg","x-wing.svg", "death-star-bold.svg", "TIE_fighter.svg", "lightsaber.svg", "dlt-19.png", "DL-44.png"] 
profilePicList = ["dart.jpg","obiwan.jpg", "luke.png", "palpatine.jpg", "solo.png"]
returnRatePics = ["bad_rate.png", "good_rate.jpg", "great_rate.jpeg"]

function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

function load_itens(clientes, produtos){
    clientes = clientes
    produtos = produtos

    var select = document.getElementById('select-client');
    for (var i = 1; i <= clientes.length; i++) {
        var option = '<option value="'+ i + '" >' + clientes[i-1].name + '</option>';
        select.insertAdjacentHTML( 'beforeend', option );
    }
    var select = document.getElementById('list-products');
    for (var i = 1; i <= produtos.length; i++) {
        var option = '<tr id="product-row-'+ String(i) + '"><td><img style="max-height: 200px;" src="/static/pedidos/images/products/' + image_list[i-1] +'" alt="">'+produtos[i-1].item+'</td><td><input class="w3-input points" type="number" id="price-input-'+ i +'" name="points" step="0.01" value="'+produtos[i-1].suggested_price+'" onchange="checkReturnRate('+ produtos[i-1].id +','+ i + ')"></td><td><input class="w3-input points" onkeypress="return false;" type="number" id="points" name="points" step="'+produtos[i-1].multiplier+'" value="0" min="0"></td><td><img class="img-rate" id=return-rate-img-' +String(i) + ' src="/static/pedidos/images/extras/good_rate.jpg" alt=""><h6 id=return-rate-text-' +String(i) + '>Boa!</h6></td></tr>';
        select.insertAdjacentHTML( 'beforeend', option );
        checkReturnRate(produtos[i-1].id, i)
    }
}

function onSelectionChange(){
    var image = document.getElementById('profile-pic');
    var select = document.getElementById('select-client');
    image.src = "/static/pedidos/images/clients/"+ profilePicList[select.value-1]
}

function checkReturnRate(item_id, product_row){
    
    var image_cell_rate = document.getElementById('return-rate-img-'+String(product_row));
    var return_rate_text = document.getElementById('return-rate-text-'+String(product_row));
    var price = parseFloat(document.getElementById('price-input-'+String(product_row)).value);
    var product_row_component = document.getElementById('product-row-'+String(product_row));
    if(price >= produtos[product_row - 1].return_rate.great){
        image_cell_rate.src = "/static/pedidos/images/extras/"+ returnRatePics[2];
        return_rate_text.innerHTML = "Rentabilidade ótima!";
        product_row_component.className = "great"
    }
    else if(price >= produtos[product_row - 1].return_rate.good){
        image_cell_rate.src = "/static/pedidos/images/extras/"+ returnRatePics[1];
        return_rate_text.innerHTML = "Rentabilidade boa!";
        product_row_component.className = ""
    }
    else{
        image_cell_rate.src = "/static/pedidos/images/extras/"+ returnRatePics[0];
        return_rate_text.innerHTML = "Rentabilidade ruim!";
        product_row_component.className = "bad"
    }
    
    console.log(produtos[product_row-1].return_rate, price);
}

function validateOrder(evt){
    console.log(produtos)
}

/* Referencias:

https://www.w3schools.com/howto/howto_js_tabs.asp

https://stackoverflow.com/questions/49461343/how-can-i-add-an-html-option-element-dynamically-to-a-select

https://www.w3schools.com/tags/att_input_step.asp

*/