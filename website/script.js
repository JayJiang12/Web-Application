function IndexSubmit() {
    
    alert("Submit is checked");
    window.location = "results.html"
}

function result_table(){
    alert("item selected");
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
        if(document.getElementById('Suburb').checked){
            alert("Suburb is checked");
        }
        else{
            alert("Suburb is not checked");
        }
    }
    
    if (a == 'hot'){
        if(document.getElementById('Hot').checked){
            alert("hot is checked");
        }
        else{
            alert("hot is not checked");
        }
    }
    
    if (a == 'warm'){
        if(document.getElementById('Warm').checked){
            alert("warm is checked");
        }
        else{
            alert("warm is not checked");
        }
    }
    
    if (a == 'cold'){
        if(document.getElementById('Cold').checked){
            alert("cold is checked");
        }
        else{
            alert("Cold is not checked");
        }
    }
    
    if (a == 'pv300k'){
        if(document.getElementById('pv300k').checked){
            alert("PV300 is checked");
            PValue300k = 300;
        }
        else{
            alert("PV300 is not checked");
        }
        
    }
    
    if (a == 'PV999'){
        if(document.getElementById('PV999').checked){
            alert("PV999 is checked");
        }
        else{
            alert("PV999 is not checked");
        }
        
    }
    
    if (a == 'PV1M'){
        if(document.getElementById('PV1M').checked){
            alert("PV1M is checked");
        }
        else{
            alert("PV1M is not checked");
        }
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






