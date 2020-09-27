const $ = window.$;
$('DIV#toggle_header').click(() => {
  const tag = $('HEADER').hasClass('green');
  if (tag === true) {
    $('HEADER').removeClass('green');
    $('HEADER').addClass('red');
  } else {
    $('HEADER').removeClass('red');
    $('HEADER').addClass('green');
  }
});
