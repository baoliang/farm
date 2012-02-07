(function(){

	
    $('#_id').live('blur', function(){
        $.get('/check_user?_id='+$('#_id').val(),function(data){
            
            if(data["success"] === false){
                $('#reg_tips').html("此用户名已被注册");
            }
            else{
                $('#reg_tips').html("");
            }
        });
        
    });
    
    $('#reg_user_action').live("click",function(){
        if($("#password").val() != $("#cpassword").val()){
            alert("确认密码跟密码不相符！");
            return;
        }
        if($('#reg_tips').html() === "" ){
            $("#reg_form").submit();
        }else{
            alert("用户名重复");
            return;
        }
    });
    $('#reg_user_cancel').live("click",function(){
        history.back();
    });    
    
}).call(this);
