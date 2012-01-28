//菜单高亮
(function(){
    
    var old_page, last_time;
    old_page = $('#old_page').val();
    last_time = $('#last_time').val();
    $("#menu_news").addClass("active");
    $("#send_news").live("click", function(){
        center_show("send_news_window");
    });
    $('#next_page').live('click', function(){
        location.href="/?old_page="+old_page+"&page="+(parseInt(old_page)+parseInt(1))+"";  
    });

    $('#pre_page').live('click', function(){
        if ((parseInt(old_page)-1) === 1){
            location.href = "/";
        }else{
           location.href="/?old_page="+old_page+"&page="+parseInt(old_page)-1+"";  
        }
    });
    $('#first_page').live('click', function(){
        location.href="/";  
    });

}).call(this);

