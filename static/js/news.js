//菜单高亮
(function(){
    
    var old_page = $('#old_page').val(),
        last_time = $('#last_time').val();
    farm.page_go({old_page: old_page, query: "{}", return_url: "/"});
    $("#send_news").live("click", function(){
        center_show("send_news_window");
    });    

    $("#menu_news").addClass("active");

    $('#first_page').live('click', function(){
        location.href="/";  
    });

}).call(this);

