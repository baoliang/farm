window.farm = {};
$('#alert_close').click(function(){
    $('#alert').hide();
});
farm.page_go = function(params){
    var old_page = params['old_page']
    $('#next_page').live('click', function(){
        location.href="/?old_page="+old_page+"&page="+(parseInt(old_page)+parseInt(1))+"";  
    });

    $('#pre_page').live('click', function(){
        if ((parseInt(old_page)-1) === 1){
            location.href = params["return_url"];
        }else{
        
           location.href="/?old_page="+old_page+"&page="+(parseInt(old_page)-1)+"";  
        }
    });
}

farm.search = function(params){
        var query = "";
        $.each(params['query'], function(index, value){
            
            if ( value === "不限"){
                value = "";
            }
            query +=  index + "=" +value+ "&"
        });
        
        $.ajax({
            "url": params['url'] + "?" + query +"ajax=true",
            "type": "POST",
            "success": function(data){
                $("#list").html(data);
            }
        })
}
function alert(content){
	$("#alert_content").html("<strong>提示!&nbsp</strong>"+content);
	center_show("alert");
}
function center_show(id){
    function center(id){
        var windowWidth = document.documentElement.clientWidth;   
        var windowHeight = document.documentElement.clientHeight;   
        var popupHeight = $('#'+id+'').height();   
        var popupWidth = $('#'+id+'').width(); 	
        $('#'+id+'').css({   
            "position": "absolute",   
            "top": (windowHeight/2-popupHeight/2)+100,   
            "left": windowWidth/2-popupWidth/2   
        }); 
    }
        center(id);
        $('#'+id+'').show();
}



