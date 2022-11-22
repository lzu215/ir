$(function(){
    $("#searchBox").keyup(function(event){
        if(event.which == 13){
            search();
        }
    });
});


function search(){
    keywords = $("#searchBox").val();
    if(!keywords){return;}
    $.ajax({url: "search/search1", 
        method: "POST", 
        data: {
            "keywords": keywords,
            "start": 0
        }, 
        timeout: 10000})
        .then(function(response){
            alert(response);
        },
        function(){
            popupMsg("Connection Failed", msgRed, "exclamation");
        })
        .always(function(){
            
        });
}