function IndexSubmit() {
    
    alert("Submit is checked");
    window.location = "results.html"
}

function handleSubmit() {
    
    alert("Submit is checked");
    
    var testData = document.getElementById("testQuery").value;
    $.ajax({
           url: "/getPoints",
           //make an AJAX request to the py script
           type: "POST",
           //pass query params below
           data: { param: testData },
           success: callbackFunc
           });
}

function callbackFunc(response) {
    //handle response here
    console.log(response);
    /**
     var positions = JSON.parse(response);
     positions.forEach(function(element) {
     console.log(element);
     var marker = new google.maps.Marker({
     position: {lat: element[0], lng: element[1]},
     map: map
     });
     });
     **/
}

/**
 ** button functions and passing value between html using
 ** javascript
 **/

var urbanValue;
var PValue300k;

function toggleCheck(a){

    if(a == 'demorate'){
        
        if(document.getElementById('Demorate').checked){
            alert("Demorate is checked");
        }
        else{
            alert("Demorate is not checked");
        }
    }
    if (a == 'republican'){
        if(document.getElementById('Republican').checked){
            alert("Republican is checked");
        }
        else{
            alert("Republican is not checked");
        }
    }
    if (a == 'urban'){
        if(document.getElementById('Urban').checked){
            alert("urban is checked");
         //   urbanValue = document.getElementById('urban')
        }
        else{
            alert("urban is not checked");
        }
    }
    
    if (a == 'suburb'){
        alert("Population under 1 million is checked");
    }
    
    if (a == 'hot'){
        alert("Hot Climate is checked");
    }
    
    if (a == 'warm'){
        alert("Warm Climate is checked");
    }
    
    if (a == 'cold'){
        alert("Cold Climate is checked");
    }
    
    if (a == 'pv300k'){
        if(document.getElementById('pv300k').checked){
            alert("PV is checked");
            PValue300k = 300;
        }
        else{
            alert("PV is not checked");
        }
        
    }
    
    if (a == 'COL35K'){
        alert("Cost of Living 3K - 5K is checked");
    }
    
    if (a == 'COL5K'){
        alert("Cost of Living 5K is checked");
    }
}


function getValue(){
  //  if(value == 'urban'){
    //    return urbanValue;
   // }
   // else if(value == 'pv300k')
   // {
        return 300;
   // }
   // else{
    //    alert("wrong value" +  urban);
   // }
}






