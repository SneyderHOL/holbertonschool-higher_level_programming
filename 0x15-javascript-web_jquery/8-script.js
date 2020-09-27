const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, (data, textStatus) => {
  for (let i = 0; i < data.results.length; i++) {
    $('#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
