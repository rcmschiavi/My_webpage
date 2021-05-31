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

function load_itens(clientes, pedidos){
    image_list = ["milenium.svg","x-wing.svg", "death-star-bold.svg", "TIE_fighter.svg", "lightsaber.svg", "dlt-19.png", "DL-44.png"] 

    var select = document.getElementById('select-client');
    for (var i = 1; i <= clientes.length; i++) {
        var option = '<option value="'+ i + '" >' + clientes[i-1] + '</option>';
        select.insertAdjacentHTML( 'beforeend', option );
    }
    var select = document.getElementById('list-products');
    for (var i = 1; i <= produtos.length; i++) {
        var option = '<tr><td><img style="max-height: 200px;" src="/static/pedidos/images/products/' + image_list[i-1] +'" alt="">'+produtos[i-1].item+'</td><td><input class="w3-input" type="number" id="points" name="points" step="0.01" value="'+produtos[i-1].suggested_price+'"></td><td><input class="w3-input" onkeypress="return false;" type="number" id="points" name="points" step="'+produtos[i-1].multiplier+'" value="0" min="0"></td></tr>';
        select.insertAdjacentHTML( 'beforeend', option );
    }
}

function onSelectionChange(){
    profilePicList = ["dart.jpg","obiwan.jpg", "luke.png", "palpatine.jpg", "solo.png"]
    var image = document.getElementById('profile-pic');
    var select = document.getElementById('select-client');
    console.log()
    image.src = "/static/pedidos/images/clients/"+ profilePicList[select.value-1]
}


/* Referenciass:

https://www.w3schools.com/howto/howto_js_tabs.asp

https://stackoverflow.com/questions/49461343/how-can-i-add-an-html-option-element-dynamically-to-a-select

https://www.w3schools.com/tags/att_input_step.asp

*/