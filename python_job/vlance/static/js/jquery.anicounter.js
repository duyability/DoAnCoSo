(function($){
    $.fn.anicounter = function(options){
        var options = $.extend({
            number: parseInt(this.text()),
            suffix: '',
            step: 20, // 3% of the rest
            delay: 5, // 1ms
            thousands: "."
        }, options);

        this.each(function(){
            var i=0;
            var $t = $(this);

            function timer(){
                if(i<options.number){
                    $t.delay(options.delay).html(thousandSep(i) + options.suffix);
                    if((options.number-i)*options.step/100>=1){
                        add = (options.number-i)*options.step/100;
                    } else{
                        add = 1;
                    }
                    i+=add;
                    i=Math.round(i);
                    setTimeout(timer, options.delay);
                }
                else{
                    $t.delay(options.delay).html(thousandSep(options.number) + options.suffix);
                }
            }

            function thousandSep(val) {
                return String(val).split("").reverse().join("")
                              .replace(/(\d{3}\B)/g, "$1" + options.thousands)
                              .split("").reverse().join("");
            }

            timer();
        });
        return this;
    };

})(jQuery);