const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, (data, textStatus) => {
  $('DIV#character').html(data.name);
});
