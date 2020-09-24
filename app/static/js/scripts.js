$(document).ready(function(){
    // show the crust  div when hidden
    $("#crust").click(function(){
      $("#initiallyHidden1").hide();
      $("#initiallyHidden2").hide();
      $("#stuffed").removeClass("active");
      $("#gluten").removeClass("active");
      $("#crust").addClass("active");
      $("#initiallyShown").show();
  })
  // show the stuffed hidden div
  $("#stuffed").click(function(){
      $("#initiallyShown").hide();
      $("#initiallyHidden2").hide();
      $("#crust").removeClass("active");
      $("#gluten").removeClass("active");
      $("#stuffed").addClass("active");
      $("#initiallyHidden1").show();
  })
  // show the glutten free hidden div
  $("#gluten").click(function(){
      $("#initiallyShown").hide();
      $("#initiallyHidden1").hide();
      $("#crust").removeClass("active");
      $("#stuffed").removeClass("active");
      $("#gluten").addClass("active");
      $("#initiallyHidden2").show();
  }) 
 
//  end of jQury document
});


  function myFunction() {
      // price of Large pizza 
      var largePizza = document.getElementById("customRadio1").checked;
      if(largePizza === true){
          largePizza = 1000
       }
      // price of Large pizza 
      var mediumPizza = document.getElementById("customRadio2").checked;
      if(mediumPizza === true){
          mediumPizza = 900
       }
      // price of Large pizza 
      var smallPizza = document.getElementById("customRadio3").checked;
      if(smallPizza === true){
          smallPizza = 800
       }
//********************************************************************** */
      // price of crispy crust
      var crispyCrust = document.getElementById("customRadioInline1").checked;
      if(crispyCrust === true){
          crispyCrust = 250
       }
      //price of stuffed crust
      var stuffedCrust = document.getElementById("customRadioInline2").checked;
      if(stuffedCrust === true){
          stuffedCrust = 200
       }
      //price of glutten crust
      var gluttenCrust = document.getElementById("customRadioInline3").checked;
      if(gluttenCrust === true){
          gluttenCrust = 150
       }
// *******************************************************************
      // price of bacon
      var bacon = document.getElementById("customCheck1").checked;
      if(bacon === true){
          bacon = 100
          myBacon = "Bacon"
       }
      // price of basil
      var basil = document.getElementById("customCheck2").checked;
      if(basil === true){
          basil = 90
          myBasil = "Basil"
       }
      // price of mushroom
      var mushroom = document.getElementById("customCheck3").checked;
      if(mushroom === true){
          mushroom = 80
          myMushroom = "Mushroom"
       }
      // price of peppers
      var peppers = document.getElementById("customCheck4").checked;
      if(peppers === true){
          peppers = 70
          myPeppers = "Peppers"
       }
      // price of pesto
      var pesto = document.getElementById("customCheck5").checked;
       if(pesto === true){
          pesto = 60
          myPesto = "Pesto"
        }
      // price of pineaple
      var pineaple = document.getElementById("customCheck6").checked;
      if(pineaple === true){
          pineaple = 50
          myPineaple = "Pineaple"
       }
      // display cost od delivery
      var i = document.getElementById("deliverySelected");
      var myDeliveryCost = parseInt(i.options[i.selectedIndex].value);
      // number of pizza
      var numberOfPizza = parseInt(document.getElementById("numberOfPizza").value);
     
      //Multiply number of pizza
      largetotal = largePizza * numberOfPizza;
      mediumTotal = mediumPizza * numberOfPizza;
      smallTotal = smallPizza * numberOfPizza ;
      // multiply crust with number of pizza
      crispyTotal = crispyCrust * numberOfPizza;
      stuffedTotal = stuffedCrust * numberOfPizza;
      gluttenTotal = gluttenCrust * numberOfPizza ;
      //compile total cost of toppings
      var myPizzaPrice = largePizza + mediumPizza + smallPizza
      var pizzaPrice = largetotal + mediumTotal + smallTotal;
      document.getElementById("pizzaCost").innerHTML = "$ "+ pizzaPrice; //append pizza price to the table
      var crustPrice = crispyCrust +  stuffedCrust + gluttenCrust;
      var crustTotal = crispyTotal +  stuffedTotal + gluttenTotal;
      document.getElementById("crustCost").innerHTML = "$ "+ crustTotal; //append crust price to the table
      var toppingsPrice = bacon + basil + mushroom + peppers + pesto + pineaple;
      document.getElementById("costOfToppings").innerHTML = "$ "+ toppingsPrice; //append toppings price to the table
      var totalCost = pizzaPrice + crustTotal + toppingsPrice + myDeliveryCost ; 
      document.getElementById("totalCost").innerHTML = "$ "+ totalCost; //append total price to the table
        // determine size of pizza 
      if(myPizzaPrice ==1000){
          document.getElementById("pizzaSize").innerHTML = "Large Pizza"
      }else if(myPizzaPrice==900){
          document.getElementById("pizzaSize").innerHTML = "Medium Pizza"
      }else{
          document.getElementById("pizzaSize").innerHTML = "Small Pizza"
      }
      // Determine type of crust
      if(crustPrice ==250){
          document.getElementById("typeOfCrust").innerHTML = " Crispy Crust"
      }else if(crustPrice==200){
          document.getElementById("typeOfCrust").innerHTML = "Stuffed Crust"
      }else{
          document.getElementById("typeOfCrust").innerHTML = "Glutten-free Crust"
      }
      // Determine the selected toppings
      var myBacon,myBasil,myMushroom,myPeppers,myPesto,myPineaple
      if(bacon == 1050){
           myBacon = "Bacon, "
      }else {
           myBacon = " "
      }
       if(basil == 950){
           myBasil = " Basil, "
      }else{
           myBasil = " "
      }
       if(mushroom == 850){
           myMushroom = "Mushroom, "
      }else {
           myMushroom = " "
      }
       if(peppers == 700){
           myPeppers = " Peppers, "
      }else {
           myPeppers = " "  
      }
      if(pesto == 700){
           myPesto = " Pesto, "
      }else {
          myPesto = " "
      } if(pineaple == 350){
           myPineaple = " Pineaple "
      }else {
          myPineaple = " "
      }
      var allToppings = myBacon + myBasil + myMushroom + myPeppers + myPesto + myPineaple;
      document.getElementById("typesOfToppings").innerHTML = allToppings;
     
      //  The delivery location
       document.getElementById("deliveryCost").innerHTML = "$ " + myDeliveryCost;
      //  order location
       var orderLocation = document.getElementById("town").value;
       if(myDeliveryCost == 0){
          document.getElementById("deliveryLocation").innerHTML = "No delivery selected! ";
       }else if(myDeliveryCost == 100 || myDeliveryCost == 200 ||myDeliveryCost == 300 ||myDeliveryCost == 400 ){
          document.getElementById("deliveryLocation").innerHTML = orderLocation;
       }else{
          document.getElementById("deliveryLocation").innerHTML = " ";
       }
} 

// function to return the pizza shop for delivery

function deliveryPlace(){
  var town = document.getElementById("town").value;
  document.getElementById("townOutput").innerHTML = "Your order will be delivered at " + town + " (Cost of delivery is in the receipt )";
  alert("Your order will be delivered at " + town);
}
// alert user that the order has been placed
function myMessage(){
   document.getElementById("message").innerHTML = "Your order has bee placed."
   alert("Your order has bee placed.")
}
function myMap() {
    var mapProp= {
      center:new google.maps.LatLng(51.508742,-0.120850),
      zoom:5,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
    }