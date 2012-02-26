//菜单高亮
(function(){
    
    var old_page = $('#old_page').val(),
        last_time = $('#last_time').val();
    farm.page_go({old_page: old_page, query: "{}", return_url: "/"});
   
    $("#menu_news").addClass("active");

    $('#first_page').live('click', function(){
        location.href="/";  
    });

    $('#search_button').click(function(){
        farm.search({
        url:"/",
        query: {
            search_value: $("#search_value").val()  
        }
        });
    });
}).call(this);

