(function(){
    farm.get_city(name){
    var option = "";
    $.get("/get_city",function(data){
            
            $.each(data, function(index, value){
               option += "<option value='"+value+"'>"+value+"</option>"
            });
        });
    }
    $("#provice").change(function(){
        farm.get_city($("#provice").val());
    });
    
}).call(this);