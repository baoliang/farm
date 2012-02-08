(function(){
    $('#update_user_action').live("click",function(){
        if($("#password").val() != $("#cpassword").val()){
            alert("确认密码跟密码不相符！");
            return;
        }

        $("#update_form").submit();
      
    });
    $('#reuest_real_auth').live("click",function(){
        alert("暂时不提供认证!");
    });    
    
}).call(this);
