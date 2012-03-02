(function(){
    farm.page_go({old_page: old_page, query: "{}", return_url: "/business"});
   

    $('#first_page').live('click', function(){
        location.href="/business";  
    });
    
    $('#search_button').click(function(){
        farm.search({
        url:"/business",
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
