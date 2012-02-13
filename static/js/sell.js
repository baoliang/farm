(function(){
    farm.search({
        url:"/sell",
        query: {
            title: $("#search_value").val(),
            content: $("#search_value").val()
        }
    });
}).call(this)