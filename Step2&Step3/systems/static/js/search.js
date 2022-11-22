function search(){
    $.ajax({url: "api/search1", 
        method: "POST", 
        data: {
            "keywords": $("#searchBox").val(),
            "start": 0
        }, 
        timeout: 10000})
        .then(function(response){
            alert(response);
        },
        function(){
            popupMsg("发送失败  请稍后重试", msgRed);
        })
        .always(function(){
            
        });
}