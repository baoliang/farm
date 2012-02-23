(function(){
    farm.get_city = function(_id, html_id){
        var option = "";
        $.get("/get_city?_id="+_id, function(data){
                var option = "";
                $.each(data.city_list, function(index, item){
                    
                    option += "<option value='"+item._id+"'>"+item.city_name+"</option>"
                });
                $('#'+html_id).html(option);
        });   
    }
    $("#province").change(function(){
        $('#city,#area').html("");
        farm.get_city($("#province").val(), 'city');
        
        if (!(this.value in ["1", "2", "9", "22"])){

	    
            setTimeout("farm.get_city($('#city').val(), 'area')", 3000); 
        }
    });
    $("#city").change(function(){
        $('#area').html("");
        farm.get_city($("#city").val(), 'area');
    });
}).call(this);
