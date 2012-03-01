(function(){
    farm.get_city = function(_id, html_id){
        var option = "";
        $.get("/get_city?_id="+_id, function(data){
                var option = "<option value=''>不限</option>";
                $.each(data.city_list, function(index, item){
                    
                    option += "<option value='"+item._id+"'>"+item.city_name+"</option>"
                });
                $('#'+html_id).html(option);
        });   
    }
    $("#province").change(function(){
        $('#city,#area').html("");
        farm.get_city($("#province").val(), 'city');
        
       
    });
    $("#city").change(function(){
        $('#area').html("");
        farm.get_city($("#city").val(), 'area');
    });
}).call(this);
