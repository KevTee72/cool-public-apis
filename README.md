# Cool Public APIs

<p align="center">
  <img src="assets/meme.png" alt="cool-public-apis" width="420" />
  <br />
</p>

A hand picked list of free public APIs that are actually pretty useful for non work related use :D Dog pictures, dad jokes, the ISS location, cocktail recipes, Pokémon stats, live earthquakes

**!Every one of them was tested before it went in this list!**

Most of them need **zero signup**. Every row has a **poke it** link to a real, working endpoint, so you can click it and see JSON in your browser before you write any code.

Good for side projects, hackathons, teaching someone their first `fetch()`, or just killing a Friday afternoon.

## How to read the tables

| Symbol | Meaning |
|---|---|
| 🆓 | No key. Just call it. |
| 🗝️ | Free key or demo key. Takes a minute to get. |
| **poke it** | A live example request. Click it. |

## Contents

- [The ten second tour](#the-ten-second-tour)
- [Animals, mostly good boys](#animals-mostly-good-boys)
- [Jokes, advice and pure nonsense](#jokes-advice-and-pure-nonsense)
- [Games, cards and nerd lore](#games-cards-and-nerd-lore)
- [Weather, space and planet Earth](#weather-space-and-planet-earth)
- [Money and crypto](#money-and-crypto)
- [Places, countries and time](#places-countries-and-time)
- [Words, books and knowledge](#words-books-and-knowledge)
- [Food and drinks](#food-and-drinks)
- [Art, music, TV and pictures](#art-music-tv-and-pictures)
- [Dev tools and fake data](#dev-tools-and-fake-data)
- [Science, health and open data](#science-health-and-open-data)
- [Sports and chess](#sports-and-chess)
- [Getting around](#getting-around)
- [Worth the signup](#worth-the-signup)
- [Be nice to free APIs](#be-nice-to-free-apis)
- [Is everything still alive?](#is-everything-still-alive)

## The ten second tour

Paste any of these into a terminal. No account needed.

```bash
# a random dog photo URL
curl -s https://dog.ceo/api/breeds/image/random

# a dad joke, as plain text
curl -s -H "Accept: text/plain" https://icanhazdadjoke.com/

# where is the International Space Station right now?
curl -s https://api.wheretheiss.at/v1/satellites/25544

# current weather in Berlin
curl -s "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true"

# a random cocktail you probably should not make on a Tuesday
curl -s https://www.thecocktaildb.com/api/json/v1/1/random.php

# weather as one line, made for terminals
curl -s "https://wttr.in/London?format=3"
```

## Animals, mostly good boys

| API | What you get | Key | Try |
|---|---|---|---|
| [Dog CEO](https://dog.ceo/dog-api/) | Random dog photos, filterable by more than 100 breeds | 🆓 | [poke it](https://dog.ceo/api/breeds/image/random) |
| [random.dog](https://random.dog/) | Random dog pics, gifs and the occasional video | 🆓 | [poke it](https://random.dog/woof.json) |
| [RandomFox](https://randomfox.ca/) | One fox picture. That is the whole API and it is perfect | 🆓 | [poke it](https://randomfox.ca/floof/) |
| [Cataas](https://cataas.com/) | Cat as a service. You can even write text on the cat | 🆓 | [poke it](https://cataas.com/cat?json=true) |
| [Cat Facts](https://catfact.ninja/) | Facts about cats plus a list of breeds | 🆓 | [poke it](https://catfact.ninja/fact) |
| [Meow Facts](https://github.com/wh-iterabb-it/meowfacts) | Even more cat facts, in many languages | 🆓 | [poke it](https://meowfacts.herokuapp.com/) |
| [HTTP Cats](https://http.cat/) | A cat picture for every HTTP status code | 🆓 | [poke it](https://http.cat/418) |
| [HTTP Dogs](https://http.dog/) | Same idea, dog edition. Diplomacy matters | 🆓 | [poke it](https://http.dog/418.jpg) |
| [The Cat API](https://thecatapi.com/) | Cat images, breeds, votes and favourites | 🗝️ | [poke it](https://api.thecatapi.com/v1/images/search) |
| [The Dog API](https://thedogapi.com/) | The dog twin of the one above | 🗝️ | [poke it](https://api.thedogapi.com/v1/images/search) |

The Cat API and The Dog API answer a few requests without a key, but a free key unlocks the full feature set.

## Jokes, advice and pure nonsense

| API | What you get | Key | Try |
|---|---|---|---|
| [icanhazdadjoke](https://icanhazdadjoke.com/api) | Dad jokes. Send `Accept: application/json` for JSON | 🆓 | [poke it](https://icanhazdadjoke.com/) |
| [Official Joke API](https://github.com/15Dkatz/official_joke_api) | Setup and punchline jokes, programming ones included | 🆓 | [poke it](https://official-joke-api.appspot.com/random_joke) |
| [JokeAPI](https://jokeapi.dev/) | Jokes by category with a safe mode filter | 🆓 | [poke it](https://v2.jokeapi.dev/joke/Programming?safe-mode) |
| [Chuck Norris](https://api.chucknorris.io/) | Chuck Norris facts. The API does not return errors, errors return the API | 🆓 | [poke it](https://api.chucknorris.io/jokes/random) |
| [Advice Slip](https://api.adviceslip.com/) | Random life advice, with search | 🆓 | [poke it](https://api.adviceslip.com/advice) |
| [Useless Facts](https://uselessfacts.jsph.pl/) | Facts you will repeat at dinner whether people like it or not | 🆓 | [poke it](https://uselessfacts.jsph.pl/api/v2/facts/random) |
| [yesno.wtf](https://yesno.wtf/) | Yes, no or maybe, plus a matching gif. Decision making, solved | 🆓 | [poke it](https://yesno.wtf/api) |
| [Bored API](https://bored-api.appbrewery.com/) | A random activity for when you have nothing to do | 🆓 | [poke it](https://bored-api.appbrewery.com/random) |
| [kanye.rest](https://kanye.rest/) | A random Kanye quote | 🆓 | [poke it](https://api.kanye.rest) |
| [Affirmations](https://www.affirmations.dev/) | A small dose of encouragement. Use after a failed deploy | 🆓 | [poke it](https://www.affirmations.dev/) |
| [GitHub Zen](https://docs.github.com/en/rest/meta/meta) | A line of GitHub design philosophy, as plain text | 🆓 | [poke it](https://api.github.com/zen) |
| [xkcd](https://xkcd.com/json.html) | Comic metadata and image links for every xkcd strip | 🆓 | [poke it](https://xkcd.com/info.0.json) |

## Games, cards and nerd lore

| API | What you get | Key | Try |
|---|---|---|---|
| [PokéAPI](https://pokeapi.co/) | Every Pokémon, move, type and evolution chain | 🆓 | [poke it](https://pokeapi.co/api/v2/pokemon/pikachu) |
| [Rick and Morty API](https://rickandmortyapi.com/) | Characters, locations and episodes, with GraphQL too | 🆓 | [poke it](https://rickandmortyapi.com/api/character/1) |
| [SWAPI](https://swapi.dev/) | Star Wars people, planets, ships and films | 🆓 | [poke it](https://swapi.dev/api/people/1/) |
| [Deck of Cards](https://deckofcardsapi.com/) | Shuffle, draw and keep piles. Build a card game with no backend | 🆓 | [poke it](https://deckofcardsapi.com/api/deck/new/draw/?count=2) |
| [Open Trivia DB](https://opentdb.com/api_config.php) | Thousands of trivia questions by category and difficulty | 🆓 | [poke it](https://opentdb.com/api.php?amount=1) |
| [D&D 5e API](https://www.dnd5eapi.co/) | Spells, monsters, classes and rules from the SRD | 🆓 | [poke it](https://www.dnd5eapi.co/api/spells/fireball) |
| [Scryfall](https://scryfall.com/docs/api) | Magic: The Gathering cards with prices and images | 🆓 | [poke it](https://api.scryfall.com/cards/random) |
| [Studio Ghibli API](https://ghibliapi.vercel.app/) | Films, characters and places from the Ghibli universe | 🆓 | [poke it](https://ghibliapi.vercel.app/films) |

## Weather, space and planet Earth

| API | What you get | Key | Try |
|---|---|---|---|
| [Open-Meteo](https://open-meteo.com/) | Forecasts, history and air quality for any coordinates | 🆓 | [poke it](https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true) |
| [wttr.in](https://github.com/chubin/wttr.in) | Weather made for the terminal, as text, PNG or JSON | 🆓 | [poke it](https://wttr.in/London?format=3) |
| [Sunrise Sunset](https://sunrise-sunset.org/api) | Sunrise, sunset and twilight times for a location | 🆓 | [poke it](https://api.sunrise-sunset.org/json?lat=40.71&lng=-74.00) |
| [Where the ISS at?](https://wheretheiss.at/w/developer) | Live position, speed and altitude of the ISS | 🆓 | [poke it](https://api.wheretheiss.at/v1/satellites/25544) |
| [Launch Library 2](https://thespacedevs.com/llapi) | Upcoming rocket launches from every agency | 🆓 | [poke it](https://ll.thespacedevs.com/2.2.0/launch/upcoming/?limit=1) |
| [Spaceflight News](https://www.spaceflightnewsapi.net/) | Space news articles, blogs and reports | 🆓 | [poke it](https://api.spaceflightnewsapi.net/v4/articles/?limit=1) |
| [NASA Image Library](https://images.nasa.gov/) | Search NASA's photo and video archive, no key needed | 🆓 | [poke it](https://images-api.nasa.gov/search?q=moon&media_type=image&page_size=1) |
| [NASA EPIC](https://epic.gsfc.nasa.gov/about/api) | Fresh full disc photos of Earth taken from a million miles away | 🆓 | [poke it](https://epic.gsfc.nasa.gov/api/natural) |
| [USGS Earthquakes](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) | Every earthquake in the last hour, day or week as GeoJSON | 🆓 | [poke it](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson) |
| [UK Carbon Intensity](https://carbonintensity.org.uk/) | How green the UK power grid is right now | 🆓 | [poke it](https://api.carbonintensity.org.uk/intensity) |

Want the Astronomy Picture of the Day or Mars rover photos? Those live behind the free NASA key in [Worth the signup](#worth-the-signup).

## Money and crypto

| API | What you get | Key | Try |
|---|---|---|---|
| [Frankfurter](https://frankfurter.dev/) | Currency rates published by the European Central Bank | 🆓 | [poke it](https://api.frankfurter.app/latest) |
| [ExchangeRate open access](https://www.exchangerate-api.com/docs/free) | Daily rates for 160 currencies | 🆓 | [poke it](https://open.er-api.com/v6/latest/USD) |
| [CoinGecko](https://www.coingecko.com/en/api) | Crypto prices, market caps and history | 🆓 | [poke it](https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd) |
| [Coinbase prices](https://docs.cdp.coinbase.com/coinbase-app/docs/api-prices) | Spot, buy and sell prices for crypto pairs | 🆓 | [poke it](https://api.coinbase.com/v2/prices/BTC-USD/spot) |

## Places, countries and time

| API | What you get | Key | Try |
|---|---|---|---|
| [REST Countries](https://restcountries.com/) | Flags, capitals, currencies, languages and borders | 🆓 | [poke it](https://restcountries.com/v3.1/name/japan) |
| [Nominatim](https://nominatim.org/) | Turn an address into coordinates and back, using OpenStreetMap | 🆓 | [poke it](https://nominatim.openstreetmap.org/search?q=eiffel+tower&format=json) |
| [Zippopotam.us](https://www.zippopotam.us/) | Postal code lookups for dozens of countries | 🆓 | [poke it](https://api.zippopotam.us/us/90210) |
| [Nager.Date](https://date.nager.at/) | Public holidays for more than 100 countries | 🆓 | [poke it](https://date.nager.at/api/v3/PublicHolidays/2026/US) |
| [TimeAPI](https://timeapi.io/) | Current time by time zone, plus conversions | 🆓 | [poke it](https://timeapi.io/api/Time/current/zone?timeZone=Europe/London) |
| [ipify](https://www.ipify.org/) | Your public IP address, nothing else | 🆓 | [poke it](https://api.ipify.org?format=json) |
| [ipapi](https://ipapi.co/) | IP to country, city and time zone | 🆓 | [poke it](https://ipapi.co/json/) |
| [ipinfo](https://ipinfo.io/) | IP details including the network that owns it | 🆓 | [poke it](https://ipinfo.io/json) |

Nominatim asks every app to send a real `User-Agent` and stay under one request per second. Read their usage policy before you build on it.

## Words, books and knowledge

| API | What you get | Key | Try |
|---|---|---|---|
| [Free Dictionary](https://dictionaryapi.dev/) | Definitions, phonetics, audio and examples | 🆓 | [poke it](https://api.dictionaryapi.dev/api/v2/entries/en/serendipity) |
| [Datamuse](https://www.datamuse.com/api/) | Rhymes, synonyms and words that sound alike. A songwriter's cheat code | 🆓 | [poke it](https://api.datamuse.com/words?rel_rhy=pizza) |
| [MyMemory](https://mymemory.translated.net/doc/spec.php) | Free translation memory for short strings | 🆓 | [poke it](https://api.mymemory.translated.net/get?q=hello&langpair=en%7Ces) |
| [Open Library](https://openlibrary.org/developers/api) | Books, authors and cover images | 🆓 | [poke it](https://openlibrary.org/search.json?q=dune&limit=1) |
| [Gutendex](https://gutendex.com/) | Metadata and download links for Project Gutenberg's free ebooks | 🆓 | [poke it](https://gutendex.com/books/1342/) |
| [PoetryDB](https://poetrydb.org/) | Classic poems by author, title or line count | 🆓 | [poke it](https://poetrydb.org/random) |
| [ZenQuotes](https://zenquotes.io/) | Inspirational quotes, one per call | 🆓 | [poke it](https://zenquotes.io/api/random) |
| [Wikipedia REST](https://en.wikipedia.org/api/rest_v1/) | Page summaries, random articles and more | 🆓 | [poke it](https://en.wikipedia.org/api/rest_v1/page/random/summary) |
| [Hacker News](https://github.com/HackerNews/API) | Top stories, comments and users, live | 🆓 | [poke it](https://hacker-news.firebaseio.com/v0/topstories.json) |

## Food and drinks

| API | What you get | Key | Try |
|---|---|---|---|
| [TheMealDB](https://www.themealdb.com/api.php) | Recipes with ingredients, steps and photos | 🆓 | [poke it](https://www.themealdb.com/api/json/v1/1/random.php) |
| [TheCocktailDB](https://www.thecocktaildb.com/api.php) | Cocktail recipes by name, ingredient or glass | 🆓 | [poke it](https://www.thecocktaildb.com/api/json/v1/1/random.php) |
| [Open Food Facts](https://world.openfoodfacts.org/data) | Ingredients and nutrition by barcode | 🆓 | [poke it](https://world.openfoodfacts.org/api/v2/product/737628064502.json) |
| [Open Brewery DB](https://www.openbrewerydb.org/) | Breweries, cideries and taprooms worldwide | 🆓 | [poke it](https://api.openbrewerydb.org/v1/breweries/random) |
| [Fruityvice](https://www.fruityvice.com/) | Nutrition facts for fruit. Very niche, very wholesome | 🆓 | [poke it](https://www.fruityvice.com/api/fruit/banana) |
| [Sample APIs coffee](https://sampleapis.com/api-list/coffee) | Coffee drinks with ingredients and photos | 🆓 | [poke it](https://api.sampleapis.com/coffee/hot) |

## Art, music, TV and pictures

| API | What you get | Key | Try |
|---|---|---|---|
| [Art Institute of Chicago](https://api.artic.edu/docs/) | Over 100k artworks with high resolution images | 🆓 | [poke it](https://api.artic.edu/api/v1/artworks?limit=1) |
| [The Met Collection](https://metmuseum.github.io/) | The Metropolitan Museum of Art's open collection | 🆓 | [poke it](https://collectionapi.metmuseum.org/public/collection/v1/objects/436535) |
| [iTunes Search](https://performance-partners.apple.com/search-api) | Songs, albums, podcasts and apps from Apple | 🆓 | [poke it](https://itunes.apple.com/search?term=daft+punk&limit=1) |
| [TVmaze](https://www.tvmaze.com/api) | TV shows, episodes, cast and schedules | 🆓 | [poke it](https://api.tvmaze.com/singlesearch/shows?q=severance) |
| [Lorem Picsum](https://picsum.photos/) | Placeholder photos at any size, with blur and grayscale | 🆓 | [poke it](https://picsum.photos/400/300) |
| [DiceBear](https://www.dicebear.com/) | Avatars generated from any seed string | 🆓 | [poke it](https://api.dicebear.com/9.x/bottts/svg?seed=kevtee) |
| [RoboHash](https://robohash.org/) | Turns any text into a unique robot, monster or cat | 🆓 | [poke it](https://robohash.org/kevtee) |
| [EmojiHub](https://github.com/cheatsnake/emojihub) | Emojis by category with HTML codes and Unicode | 🆓 | [poke it](https://emojihub.yurace.pro/api/random) |

## Dev tools and fake data

| API | What you get | Key | Try |
|---|---|---|---|
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | Fake posts, users and todos for prototypes and tutorials | 🆓 | [poke it](https://jsonplaceholder.typicode.com/todos/1) |
| [DummyJSON](https://dummyjson.com/) | Fake products, carts, users and logins | 🆓 | [poke it](https://dummyjson.com/products/1) |
| [Random User](https://randomuser.me/) | Realistic fake people with photos and addresses | 🆓 | [poke it](https://randomuser.me/api/) |
| [httpbin](https://httpbin.org/) | Echoes your request back. Great for debugging headers and auth | 🆓 | [poke it](https://httpbin.org/get) |
| [httpbin UUID](https://httpbin.org/#/Dynamic_data) | A fresh UUID v4 on every call | 🆓 | [poke it](https://httpbin.org/uuid) |
| [Agify](https://agify.io/) | Guesses an age from a first name. Usually wrong in a fun way | 🆓 | [poke it](https://api.agify.io?name=michael) |
| [Nationalize](https://nationalize.io/) | Guesses nationality from a name | 🆓 | [poke it](https://api.nationalize.io?name=nathaniel) |
| [Genderize](https://genderize.io/) | Guesses gender from a name, with a probability score | 🆓 | [poke it](https://api.genderize.io?name=alex) |
| [QR Server](https://goqr.me/api/) | Makes a QR code image from any text | 🆓 | [poke it](https://api.qrserver.com/v1/create-qr-code/?data=hello&size=200x200) |
| [Microlink](https://microlink.io/) | Link previews, metadata and screenshots for any URL | 🆓 | [poke it](https://api.microlink.io/?url=https://github.com) |
| [Shields.io](https://shields.io/) | Those little badges at the top of every README | 🆓 | [poke it](https://img.shields.io/badge/apis-cool-ff69b4) |
| [GitHub REST](https://docs.github.com/en/rest) | Public users, repos and gists without auth | 🆓 | [poke it](https://api.github.com/users/octocat) |

## Science, health and open data

| API | What you get | Key | Try |
|---|---|---|---|
| [openFDA](https://open.fda.gov/apis/) | Drug, device and food data from the US FDA | 🆓 | [poke it](https://api.fda.gov/drug/event.json?limit=1) |
| [disease.sh](https://disease.sh/) | Open disease statistics by country | 🆓 | [poke it](https://disease.sh/v3/covid-19/all) |
| [World Bank](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589) | Population, GDP and thousands of indicators per country | 🆓 | [poke it](https://api.worldbank.org/v2/country/US/indicator/SP.POP.TOTL?format=json&per_page=1) |
| [GBIF](https://techdocs.gbif.org/en/openapi/) | Global biodiversity records and species names | 🆓 | [poke it](https://api.gbif.org/v1/species/match?name=Puma%20concolor) |
| [iNaturalist](https://api.inaturalist.org/v1/docs/) | Wildlife sightings photographed by real people | 🆓 | [poke it](https://api.inaturalist.org/v1/observations?per_page=1) |

## Sports and chess

| API | What you get | Key | Try |
|---|---|---|---|
| [Jolpica F1](https://github.com/jolpica/jolpica-f1) | Formula 1 results back to 1950, the community home of the old Ergast API | 🆓 | [poke it](https://api.jolpi.ca/ergast/f1/current/last/results.json) |
| [NHL Web API](https://api-web.nhle.com/v1/standings/now) | Live NHL standings, scores and schedules. Unofficial docs only | 🆓 | [poke it](https://api-web.nhle.com/v1/standings/now) |
| [Chess.com](https://www.chess.com/news/view/published-data-api) | Player profiles, ratings and game archives | 🆓 | [poke it](https://api.chess.com/pub/player/hikaru) |
| [Lichess](https://lichess.org/api) | Games, puzzles, tournaments and live TV | 🆓 | [poke it](https://lichess.org/api/puzzle/daily) |

## Getting around

| API | What you get | Key | Try |
|---|---|---|---|
| [CityBikes](https://api.citybik.es/v2/) | Bike share stations in hundreds of cities | 🆓 | [poke it](https://api.citybik.es/v2/networks) |
| [TfL Unified API](https://api.tfl.gov.uk/) | London Tube status, arrivals and journey planning | 🆓 | [poke it](https://api.tfl.gov.uk/Line/Mode/tube/Status) |

## Worth the signup

These need a free key, but they are so useful that the two minute signup pays for itself.

| API | Why bother | Free tier |
|---|---|---|
| [NASA APIs](https://api.nasa.gov/) | Astronomy Picture of the Day, Mars rover photos, near Earth asteroids | Yes, `DEMO_KEY` for quick tests |
| [Semantic Scholar](https://api.semanticscholar.org/) | Millions of research papers and citations. Works keyless, but a key gets you real rate limits | Yes |
| [OpenWeatherMap](https://openweathermap.org/api) | The weather API everyone learns on | Yes |
| [WeatherAPI](https://www.weatherapi.com/) | Forecasts, astronomy and marine weather | Yes |
| [TMDB](https://developer.themoviedb.org/docs) | Movies and TV with posters, cast and ratings | Yes |
| [OMDb](https://www.omdbapi.com/) | Movie lookups by title or IMDb id | Yes |
| [Unsplash](https://unsplash.com/developers) | Gorgeous free photos for your app | Yes |
| [GIPHY](https://developers.giphy.com/) | Gif search and stickers. Every chat app needs it | Yes |
| [NewsAPI](https://newsapi.org/) | Headlines from thousands of sources | Yes, for development |
| [Alpha Vantage](https://www.alphavantage.co/) | Stock prices, forex and indicators | Yes |
| [Spotify Web API](https://developer.spotify.com/documentation/web-api) | Tracks, playlists and audio metadata | Yes, OAuth |
| [YouTube Data API](https://developers.google.com/youtube/v3) | Search videos, channels and playlists | Yes, quota based |

## Be nice to free APIs

Most of these are run by one person, a museum, or a public agency, paying the server bill out of pocket. A few rules keep them alive:

1. **Cache everything you can.** Country data does not change every second. Store it.
2. **Send a real `User-Agent`.** Something like `my-app/1.0 (you@example.com)`. Some APIs reject requests without one.
3. **Read the rate limit and stay under it.** Getting banned from a free API is a speedrun nobody should attempt.
4. **Handle failures.** Free services go down. Show a fallback instead of a white screen.
5. **Keep keys out of the frontend.** If a key ships in your JavaScript bundle, it is public. Put a tiny server in between.
6. **Say thanks.** Star their repo, sponsor them, or credit them in your app.

## Is everything still alive?

APIs die. It happens. This repo ships a small script that calls every **poke it** link in this README and reports what is down. No dependencies, just Python 3.

```bash
python ping.py
```

Sample output:

```text
200  dog.ceo        https://dog.ceo/api/breeds/image/random
200  pokeapi.co     https://pokeapi.co/api/v2/pokemon/pikachu
503  example.com    https://example.com/broken

96 alive, 1 down
```

A `429` means the API is up but you have called it too often today, so it counts as alive. The script exits with code 1 only if something is actually down, so you can drop it into a scheduled CI job.

## Contributing

Found an API that made you smile? Open a pull request. The rules are short and live in [CONTRIBUTING.md](CONTRIBUTING.md). The main one: it has to be free to try, and you have to include a working **poke it** link.

## Credits

Big respect to [public-apis/public-apis](https://github.com/public-apis/public-apis), the giant list that got a whole generation of developers building. This repo is a smaller, opinionated cousin: fewer entries, a live example on every row, and a script to check the list is not lying to you.

Meme courtesy of the internet. Code and list under the [MIT License](LICENSE).
