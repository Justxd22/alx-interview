#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsChar (Id) {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + Id;
  let res = await (await request(url)).body;
  res = JSON.parse(res);
  const characters = res.characters;

  for (let x = 0; x < characters.length; x++) {
    const urlChar = characters[x];
    let character = await (await request(urlChar)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

starwarsChar(filmID);
