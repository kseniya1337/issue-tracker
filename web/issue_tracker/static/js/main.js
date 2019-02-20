jQuery(function($) {
  $('*[data-toggle="tooltip"]').tooltip();

  $('.avatar__edit_avatar').click(function () {
      $('#id_avatar').click();
  });

  $('#id_avatar').change(function () {
      $(this).closest('form').submit();
  });

});