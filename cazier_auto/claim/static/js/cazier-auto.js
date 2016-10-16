$(document).ready(function() {
  $('ul.nav li.dropdown').hover(function() {
      $('.dropdown-menu', this).stop(true, true).slideDown(300);
    }, function() {
      $('.dropdown-menu', this).stop(true, true).slideUp(300);
    });
});
