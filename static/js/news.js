//菜单高亮
(function(){
    
    var old_page = $('#old_page').val(),
        last_time = $('#last_time').val();
    farm.page_go({old_page: old_page, query: "{}", return_url: "/"});
   
    $("#menu_news").addClass("active");

    $('#first_page').live('click', function(){
        location.href="/";  
    });
    farm.search({
        url:"/",
        query: {
            title: $("#search_value").val(),
            content: $("#search_value").val()
        }
    });
}).call(this);

