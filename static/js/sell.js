(function(){
    farm.page_go({old_page: old_page, query: "{}", return_url: "/"});
   
    $("#menu_sell").addClass("active");

    $('#first_page').live('click', function(){
        location.href="/";  
    });
    
    $('#search_button').click(function(){
        farm.search({
        url:"/sell",
        query: {
            search_value: $("#search_value").val(),
            start_price: $("#start_price").val(),
            end_price: $("#end_price").val(),
            type: $("input:radio[name='type']:checked").val(),
            province: $("#province").find("option:selected").text(),
            city: $("#city").find("option:selected").text(),
            area: $("#area").find("option:selected").text()
        }
        });
    });
}).call(this)
