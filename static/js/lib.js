var farm = {};

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