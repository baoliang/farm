(function(){
    farm.page_go({old_page: old_page, query: "{}", return_url: "/invest"});
   

    $('#first_page').live('click', function(){
        location.href="/invest";  
    });
    
    $('#search_button').click(function(){
        farm.search({
        url:"/invest",
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
