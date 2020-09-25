const url = 'https://fourtonfish.com/hellosalut/?lang=frK';
document.addEventListener('DOMContentLoaded', function () {
  $.get(url, (data, textStatus) => {
    $('DIV#hello').html(data.hello);
  });
});
