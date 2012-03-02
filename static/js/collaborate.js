(function(){
    farm.page_go({old_page: old_page, query: "{}", return_url: "/collaborate"});
   

    $('#first_page').live('click', function(){
        location.href="/collaborate";  
    });
    
    $('#search_button').click(function(){
        farm.search({
        url:"/collaborate",
        query: {
            search_value: $("#search_value").val(),
            
           
            type: $("input:radio[name='type']:checked").val(),
            province: $("#province").find("option:selected").text(),
            city: $("#city").find("option:selected").text(),
            area: $("#area").find("option:selected").text()
        }
        });
    });
}).call(this)
