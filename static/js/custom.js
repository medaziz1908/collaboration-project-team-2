$(document).ready(function(){
  $('.increment-btn').click(function(e){
    e.preventDefault();
    var inc_value = $(this).closest('.product_data').find('.qty-input').val();
    var value = parseInt(inc_value, 10); 
    value = isNaN (value) ? 0 : value;
    if(value < 10)
    {
      value++;
      $(this).closest('.product_data').find('.qty-input').val(value);

    }

  });

  $('.decrement-btn').click(function(e){
    e.preventDefault();
    var dec_value = $(this).closest('.product_data').find('.qty-input').val();
    var value = parseInt(dec_value, 10); 
    value = isNaN (value) ? 0 : value;
    if(value > 1)
    {
      value--;
      $(this).closest('.product_data').find('.qty-input').val(value);

    }

  });


  $('.add_btn').click(function(e){
    e.preventDefault();
    var product_id = $(this).closest('.product_data').find('.id_prod').val();
    var product_qty = $(this).closest('.product_data').find('.qty-input').val();
    var price = $(this).closest('.product_data').find('.pricee').val();
    var token= $('input[name=csrfmiddlewaretoken]').val();
  
    $.ajax({
            
      method: "POST",
      //type: "POST",
      url: "/add-to-cart",
      data:{
            'product_id': product_id,
            'product_qty':product_qty,
            'price':price,
            csrfmiddlewaretoken: token
        },
        //dataType: "JSON",
        success: function (response) {
            console.log(response)
            alertify.success(response.status)
            
        }
    });
  });

  $('.add_wishlist').click(function(e){
    e.preventDefault();
    var product_id = $(this).closest('.product_data').find('.id_prod').val();
    var token= $('input[name=csrfmiddlewaretoken]').val();
  
    $.ajax({
            
      method: "POST",
      url: "/add-to-wishlist",
      data:{
            'product_id': product_id,
            csrfmiddlewaretoken: token
        },
        //dataType: "JSON",
        success: function (response) {
            console.log(response)
            alertify.success(response.status)
            
        }
    });
  });

  $('.change-qty').click(function(e){
    e.preventDefault();
    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    var product_qty = $(this).closest('.product_data').find('.qty-input').val();
    var token= $('input[name=csrfmiddlewaretoken]').val();
  
    $.ajax({
            
      method: "POST",
      url: "/update_card",
      data:{
            'product_id': product_id,
            'product_qty':product_qty,
            csrfmiddlewaretoken: token
        },
        success: function (response) {
            console.log(response)
            //alertify.success(response.status)
            
        }
    });
  });

  $(document).on('click','.btn-delete',function(e){
    e.preventDefault();
    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    var token= $('input[name=csrfmiddlewaretoken]').val();
  
    $.ajax({
            
      method: "POST",
      url: "delete-card-item",
      data:{
            'product_id': product_id,
            csrfmiddlewaretoken: token
           },
        success: function (response) 
        {
          alertify.success(response.status)
          $('.cartdata').load(location.href + " .cartdata");
        
          
          }
    });
  });
  
  $(document).on('click','.btn-delete-wish',function(e){
  
    e.preventDefault();
    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    var token= $('input[name=csrfmiddlewaretoken]').val();
  
    $.ajax({
            
      method: "POST",
      url: "delete-wish-item",
      data:{
            'product_id': product_id,
            csrfmiddlewaretoken: token
           },
        success: function (response) 
        {
          alertify.success(response.status)
          $('.wishdata').load(location.href + " .wishdata");
        
          
          }
    });
  });













 

});



