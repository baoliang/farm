//菜单高亮
$("#menu_news").addClass("active");
$("#send_news").live("click", function(){
    center_show("send_news_window");
});
$('#pre_page').live('click', function(){
    location.href="/";  
});

