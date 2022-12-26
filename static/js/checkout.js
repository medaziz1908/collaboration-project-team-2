$(document).ready(function(){
  
  $('.razpay-btn').click(function(e){
    e.preventDefault();
    var fname = $("[name='fname']").val();
    var lname = $("[name='lname']").val();
    var email = $("[name='email']").val();
    var phone = $("[name='phone']").val();
    var addresse = $("[name='addresse']").val();
    var city = $("[name='city']").val();
    var state = $("[name='state']").val();
    var country = $("[name='country']").val();
    var pin_code = $("[name='pin_code']").val();

    if(fname=="" || lname=="" || email=="" || phone=="" || addresse=="" || city=="" || state=="" || country=="" || pin_code=="")
    {   
      //alert("All fields are mandatory");
      Swal.fire("Alert!","All fields are mandatory!","error");
      return false;
    }
    else
    {
      $.ajax({
            
        method: "GET",
        url: "/proced-to-pay",
        success: function (response) {
          //console.log(response)
          var options = {
            "key": "rzp_test_oRfSzsSGPgUAwU", // Enter the Key ID generated from the Dashboard
            "amount": response.total_price, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
            "currency": "INR",
            "name": "med aziz",
            "description": "Thank u fro using us",
            "image": "https://example.com/your_logo",
            //"order_id": "order_IluGWxBm9U8zJ8", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
            "handler": function (response){
                alert(response.razorpay_payment_id);
                
                },
            "prefill": {
                "name": fname+" "+lname,
                "email": email,
                "contact": phone
              },
            
            "theme": {
                "color": "#3399cc"
              }
          };
          var rzp1 = new Razorpay(options);
          rzp1.open();

        }
            
              
          
      });
     
    }
    



  });












});