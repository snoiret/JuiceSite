$(document).ready(function () {
    $(".test").click(function () {
        $("#thedialog").attr('src', $(this).attr("href"));
        $("#somediv").dialog({
            width: 400,
            height: 450,
            modal: true,
            close: function () {
                $("#thedialog").attr('src', "about:blank");
            }
        });
        return false;
    });
});
    //$("#about-btn").click( function(event) {
      //  alert("You clicked the button using JQuery! And it worked!");
    //});
	


/*
//create all the dialogue
	$(".dialog").dialog({
    	autoOpen: false
	});

	//opens the appropriate dialog
$	(".dialogButton").click(function () {
    	//takes the ID of appropriate dialogue
    	var id = $(this).data('id');
   		//open dialogue
    	$(id).dialog("open");
	});

	$('.buttonDialog').each(function() {
		$.data(this, 'dialog', 
			$(this).next('.filterDialog').dialog({
	        autoOpen: false, 
	        modal: true,  
	        width: 600,  
	        height: 400
	      })
	    );  
	}).click(function(each){
		$.data(this, 'dialog').dialog('open');
		return false;
	});

	 $(".buttonDialog").click(function () {
        $("#theFilter").attr('src', $(this).attr("href"));
        $("#filterDialog").dialog({
            width: 400,
            height: 450,
            modal: true,
            close: function () {
                $("#theFilter").attr('src', "about:blank");
            }
        });
        return false;
    });
});

*/
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}


