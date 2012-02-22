(function(){
    var old_page = $('#old_page').val(),
        last_time = $('#last_time').val();
    farm.page_go({old_page: old_page, query: "{}", return_url: "/"});
   
    $("#menu_sell").addClass("active");

    $('#first_page').live('click', function(){
        location.href="/";  
    });
    farm.search({
        url:"/sell",
        query: {
            title: $("#search_value").val(),
            content: $("#search_value").val(),
            start_time: $("#start_time").val(),
            end_time: $("#end_time").val(),
            start_price: $("#start_price").val(),
            end_price: $("#end_price").val(),
            type: $("input:radio[name='type']:checked").val(),
            province: $("#province").find("option:selected").text(),
            city: $("#city").find("option:selected").text(),
            area: $("#area").find("option:selected").text()
        }
    });
}).call(this)
