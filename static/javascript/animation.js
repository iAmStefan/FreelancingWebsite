$(function() {
   $(document).on("scroll", function() {
     if($(document).scrollTop()>10) {
       $(".menu").addClass("shrink");
       $(".logo img").addClass("shrinkLogo");
     } else {
       $(".menu").removeClass("shrink");
       $(".logo img").removeClass("shrinkLogo");
     }
   });
});
