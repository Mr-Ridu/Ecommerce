$(document).ready(function () {
    
    $("#ap").click(function(){
        $("#add_product").removeClass("d-none");
        // $(this).css("background-color", "yellow");
        
    });
    $("#op").click(function(){
        $("#orders").removeClass("d-none");
        
    });
    $("#vp").click(function(){
        $("#view_product").removeClass("d-none");
        
    });
    // $("#login-modal-close").click(function(){
    //     $("#login-modal").addClass("hidden");
    // });
   
   //for show cart product counter
//    if(localStorage.getItem('cart'))
   $(document).on("click", ".cart", function() {
    var theid = this.id.toString();
    console.log(theid);
    localStorage.setItem('productid:',theid)
    });

});