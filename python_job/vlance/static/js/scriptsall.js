
(function( $ ) {

    $.fn.guidding = function(options) {
        
//        count so buoc
        var getObjectSize = function(obj) {
            var len = 0, key;
            for (key in obj) {
                if (obj.hasOwnProperty(key)) len++;
            }
            return len;
        };
        

        return this.each(function() {
            if($.cookie('nextcookie') == null || $.cookie('nextcookie') == ''){
                $.cookie('nextcookie', JSON.stringify(1) , { expires: 7, path: '/' });
                $.cookie('curentcookie', JSON.stringify(0) , { expires: 7, path: '/' });
            }
            for(var i=1 ; i <= getObjectSize(options) ; i++){
//                add attr curent and next step
                    if(i == getObjectSize(options)){
                        $('.popover-next',this).text('Kết thúc');
                    }
//                else{
                    $('.popover-next',this).attr({
                        'data-curentstep': i,
                        'data-nextstep': options[i].data_nextstep,
                        'data-url': options[i].data_url,
                        'data-countsizeOj': getObjectSize(options),
                    });
//                }
                
                
                    $('.popover-pre',this).attr({
                        'data-curentstep': i,
                        'data-prestep': options[i].data_prestep,
                        'data-countsizeOj': getObjectSize(options),
                    });
                
//                end add attr curent and next step
//                
//                get string content
                $('.content-popover',this).html(options[i].data_content);
                var htmlString = $( this ).html();
                
                $('' + options[i].data_target + '').attr({
                    'data-toggle': 'popover',
                    'data-placement': 'bottom',
                    'data-html': 'true',
                    'data-curentstep-popover': i,
                    'data-next-popover': options[i].data_nextstep,
                    'data-pre-popover': options[i].data_prestep,
                    'data-content': htmlString,
                });
                               
                if($.cookie('nextcookie') == null)
                {
//                    neu ko co cookie thy cho cai dau tien hien thi
                    if(i==1){
                        $(options[i].data_target).popover('show');
                    }
                }else{
                    var next_step_click = parseInt($.parseJSON($.cookie('nextcookie')));
//                    hien thi menu
                    if(next_step_click == 1){
                        $('.account-menu').addClass('open_menu');
                        $('body').find('[data-curentstep-popover="' + next_step_click + '"]').addClass('hover');
                    }else{
                        $('.account-menu').removeClass('open_menu');
                        $('body').find('[data-curentstep-popover="' + next_step_click + '"]').removeClass('hover');
                    }
//                    end hien thi menu
                    $('body').find('[data-curentstep-popover="' + next_step_click + '"]').popover('show');
                }
            }
//            cai dau tien thi add class cho an nut pre
            if($.cookie('nextcookie') == 1){
                $('body').find('.popover-pre').addClass('first');
            }
        });
    };
    
}( jQuery ));