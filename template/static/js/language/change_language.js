function changePt(){
      console.log("Entrou")
      	    $.ajax({
        url: 'change_to_pt', //The URL you defined in urls.py
        success: function(data) {
        location.reload();
          //If you wish you can do additional data manipulation here.
        }

    	});
      }

function changeEn(){
      console.log("Entrou")
      	    $.ajax({
        url: 'change_to_en', //The URL you defined in urls.py
        success: function(data) {
        location.reload();
          //If you wish you can do additional data manipulation here.
        }

    	});
      }
