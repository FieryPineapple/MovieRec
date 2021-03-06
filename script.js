//TMDB 

const API_KEY = 'api_key=46478bd74bc72c1d05519b8a51dfed49';
const BASE_URL = 'https://api.themoviedb.org/3';
const API_URL = BASE_URL + '/discover/movie?sort_by=popularity.desc&'+API_KEY;
const IMG_URL = 'https://image.tmdb.org/t/p/w500';
const searchURL = BASE_URL + '/search/movie?'+API_KEY;

const genres = [
  {
    "id": 28,
    "name": "Action"
  },
  {
    "id": 12,
    "name": "Adventure"
  },
  {
    "id": 16,
    "name": "Animation"
  },
  {
    "id": 35,
    "name": "Comedy"
  },
  {
    "id": 80,
    "name": "Crime"
  },
  {
    "id": 99,
    "name": "Documentary"
  },
  {
    "id": 18,
    "name": "Drama"
  },
  {
    "id": 10751,
    "name": "Family"
  },
  {
    "id": 14,
    "name": "Fantasy"
  },
  {
    "id": 36,
    "name": "History"
  },
  {
    "id": 27,
    "name": "Horror"
  },
  {
    "id": 10402,
    "name": "Music"
  },
  {
    "id": 9648,
    "name": "Mystery"
  },
  {
    "id": 10749,
    "name": "Romance"
  },
  {
    "id": 878,
    "name": "Science Fiction"
  },
  {
    "id": 10770,
    "name": "TV Movie"
  },
  {
    "id": 53,
    "name": "Thriller"
  },
  {
    "id": 10752,
    "name": "War"
  },
  {
    "id": 37,
    "name": "Western"
  }
]

const main = document.getElementById('main');
const form =  document.getElementById('form');
const search = document.getElementById('search');
const tagsEl = document.getElementById('tags');

const prev = document.getElementById('prev')
const next = document.getElementById('next')
const current = document.getElementById('current')
const favorite = document.getElementById('favorite');
const favoritesTab = document.getElementById("faves");

var currentPage = 1;
var nextPage = 2;
var prevPage = 3;
var lastUrl = '';
var totalPages = 100;
var id = 0;
var storedFavorite = '';

var favArr = [];
var selectedGenre = [];
setGenre();
function setGenre() {
  tagsEl.innerHTML= '';
  genres.forEach(genre => {
      const t = document.createElement('div');
      t.classList.add('tag');
      t.id=genre.id;
      t.innerText = genre.name;
      t.addEventListener('click', () => {
          if(selectedGenre.length == 0){
              selectedGenre.push(genre.id);
          }else{
              if(selectedGenre.includes(genre.id)){
                  selectedGenre.forEach((id, idx) => {
                      if(id == genre.id){
                          selectedGenre.splice(idx, 1);
                      }
                  })
              }else{
                  selectedGenre.push(genre.id);
              }
          }
          console.log(selectedGenre)
          getMovies(API_URL + '&with_genres='+encodeURI(selectedGenre.join(',')))
          highlightSelection()
      })
      tagsEl.append(t);
  })
}

function highlightSelection() {
  const tags = document.querySelectorAll('.tag');
  tags.forEach(tag => {
      tag.classList.remove('highlight')
  })
  clearBtn()
  if(selectedGenre.length !=0){   
      selectedGenre.forEach(id => {
          const hightlightedTag = document.getElementById(id);
          hightlightedTag.classList.add('highlight');
      })
  }

}

function clearBtn(){
  let clearBtn = document.getElementById('clear');
  if(clearBtn){
      clearBtn.classList.add('highlight')
  }else{
          
      let clear = document.createElement('div');
      clear.classList.add('tag','highlight');
      clear.id = 'clear';
      clear.innerText = 'Clear x';
      clear.addEventListener('click', () => {
          selectedGenre = [];
          setGenre();            
          getMovies(API_URL);
      })
      tagsEl.append(clear);
  }
  
}

getMovies(API_URL);

function getMovies(url) {
  lastUrl = url;
    fetch(url).then(res => res.json()).then(data => {
        console.log(data.results)
        if(data.results.length !== 0){
            showMovies(data.results);
            currentPage = data.page;
            nextPage = currentPage + 1;
            prevPage = currentPage - 1;
            totalPages = data.total_pages;

            current.innerText = currentPage;

            if(currentPage <= 1){
              prev.classList.add('disabled');
              next.classList.remove('disabled')
            }else if(currentPage>= totalPages){
              prev.classList.remove('disabled');
              next.classList.add('disabled')
            }else{
              prev.classList.remove('disabled');
              next.classList.remove('disabled')
            }

            tagsEl.scrollIntoView({behavior : 'smooth'})

        }else{
            main.innerHTML= `<h1 class="no-results">No Results Found</h1>`
        }
       
    })

}

function showMovies(data) {
    main.innerHTML = '';
    console.log(data)
    console.log('hi')

    data.forEach(movie => {
        const {title, poster_path, vote_average, overview, id} = movie;
        const movieEl = document.createElement('div');
        movieEl.classList.add('movie');
        movieEl.innerHTML = `
             <img src="${poster_path? IMG_URL+poster_path: "http://via.placeholder.com/1080x1580" }" alt="${title}">
            <div class="movie-info">
                <h3>${title}</h3>
                <span class="${getColor(vote_average)}">${vote_average}</span>
            </div>
            <div class="overview">
                <h3>Overview</h3>
                ${overview.replace(/^(.{300}[^\s]*).*/, "$1")}...
                <br/> 
                <button class="know-more" id="${id}">Know More</button
            </div>
        
        `

        main.appendChild(movieEl);

        document.getElementById(id).addEventListener('click', () => {
          console.log(id)
          openNav(movie)
        })
    })
}


const overlayContent = document.getElementById('overlay-content');
/* Open when someone clicks on the span element */
function openNav(movie) {
  id = movie.id;
  var cast = [];
  var castChar = [];
  var providers = [];
  fetch(BASE_URL + '/movie/'+id+'/watch/providers?'+API_KEY).then(res => res.json()).then(providerData => {
    console.log(providerData);
    providers = [];
    if(providerData.results.US.rent != null){
      providerData.results.US.rent.forEach(provider => {
        providers.push(provider.provider_name);
      })
    }
    else if(providerData.results.US.buy != null){
      providerData.results.US.buy.forEach(provider => {
        providers.push(provider.provider_name);
      })
    }
    else if(providerData.results.US.flatrate != null){
      providerData.results.US.flatrate.forEach(provider => {
        providers.push(provider.provider_name);
      })
    }
    else{
      providers.push("Not available");
    }
  })
  fetch(BASE_URL + '/movie/'+id+'/credits?'+API_KEY).then(res => res.json()).then(castData => {
    console.log(castData);
    cast = [];
    castChar = [];
    castData.cast.forEach(person => {
      cast.push(person.name);
      castChar.push(person.character);
    })
  })
  fetch(BASE_URL + '/movie/'+id+'?'+API_KEY).then(res => res.json()).then(videoData => {
    console.log(videoData);
    if(videoData){
      document.getElementById("myNav").style.width = "100%";
      if(videoData !== null){
        var content = `
        <div class="row">
          <div class="col-md-4">
          <h1 style="color:white;">${movie.original_title}</h1>
            <img src="${movie.poster_path? 'https://image.tmdb.org/t/p/w300'+movie.poster_path: "https://via.placeholder.com/300x450" }" alt="${movie.original_title}"
          </div>
        <div class="col-md-8">
          <u1 class="list-group">
            <li style="color:white;" class="listgroup-item"><strong>Movie Rating:</strong> ${videoData.vote_average}</li>
            <li style="color:white;" class="listgroup-item"><strong>Movie Genres:</strong> ${videoData.genres[0].name}, ${videoData.genres[1].name}</li>
            <li style="color:white;" class="listgroup-item"><strong>Movie Production Company:</strong> ${videoData.production_companies[0].name}</li>
            <li style="color:white;" class="listgroup-item"><strong>Movie runtime:</strong> ${videoData.runtime} minutes </li>
            <li style="color:white;" class="listgroup-item"><strong>Release Date:</strong> ${videoData.release_date} </li>
            <li style="color:white;" class="listgroup-item"><strong>Movie runtime:</strong> ${videoData.runtime} minutes </li>
            <li style="color:white;" class="listgroup-item"><strong>Providers:</strong> ${providers[0]}, ${providers[1]}, ${providers[2]}</li>
          </ul>
          </div>
        </div>
        <div class="row">
          <div class="well">
            <h3 style="color:white;">Plot</h3>
            <p style="color:white;">${movie.overview}</p>
            <h3 style="color:white;">Cast</h3>
              <p style="color:white;"><strong>${cast[0]}</strong> (${castChar[0]})</p>
              <p style="color:white;"><strong>${cast[1]}</strong> (${castChar[1]})</p>
              <p style="color:white;"><strong>${cast[2]}</strong> (${castChar[2]})</p>
              <p style="color:white;"><strong>${cast[3]}</strong> (${castChar[3]})</p>
              <p style="color:white;"><strong>${cast[4]}</strong> (${castChar[4]})</p>
            </h3>          
          </div>
          <button class="addFav" onclick="addToFavorite()">Add to Favorites</button>
          <div>
            <p>
            <br>
            </p>
          </div>
        </div>
        `;
        overlayContent.innerHTML = content;
      }else{
        overlayContent.innerHTML = `<h1 class="no-results">No Results Found</h1>`
      }
    }
  })
}

/* Close when someone clicks on the "x" symbol inside the overlay */
function closeNav() {
  document.getElementById("myNav").style.width = "0%";
}

function addToFavorite() {
  console.log(id)
  if (favArr.includes(id)) {
    console.log("already favorited")
  } else {
    favArr.push(id);
    console.log("added to favorites");
  }
  localStorage.setItem('Favorites', JSON.stringify(favArr));
  favorite.innerHTML = ``
  getFavorite()
}

function getFavorite() {
  storedFavorite = JSON.parse(localStorage.getItem("Favorites"));
  console.log(storedFavorite)
  if(storedFavorite == undefined || storedFavorite.length == 0){
    console.log("No favorites yet");
  }
  else {
    for (let i = 0; i < storedFavorite.length; i++) {
      fetch(BASE_URL + '/movie/'+storedFavorite[i]+'?'+API_KEY).then(res => res.json()).then(favData => {
        console.log(favData);
        showFavorite(favData)
      })
    }
  }
}

function showFavorite(data) {
    if (data !== null) {
      const movieEl2 = document.createElement('div');
      movieEl2.classList.add('movie');
      movieEl2.innerHTML = `
             <img src="${data.poster_path? 'https://image.tmdb.org/t/p/w300'+data.poster_path: "https://via.placeholder.com/300x450" }" alt="${data.title}">
            <div class="movie-info">
                <h3>${data.title}</h3>
                <span class="${getColor(data.vote_average)}">${data.vote_average}</span>
            </div>
            <div class="overview">
                <h3>Overview</h3>
                ${data.overview}
                <br/> 
                <button class="know-more" id="${data.id}">Know More</button>
            </div>
        `;
        favorite.appendChild(movieEl2);
    } else {
      favorite.innerHTML = `<h1 class="no-results">No Results Found</h1>`
    }
}

favorite.innerHTML = getFavorite();

function getColor(vote) {
    if(vote>= 8){
        return 'green'
    }else if(vote >= 5){
        return "orange"
    }else{
        return 'red'
    }
}

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const searchTerm = search.value;
    selectedGenre=[];
    setGenre();
    if(searchTerm) {
        getMovies(searchURL+'&query='+searchTerm)
    }else{
        getMovies(API_URL);
    }

})

prev.addEventListener('click', () => {
  if(prevPage > 0){
    pageCall(prevPage);
  }
})

next.addEventListener('click', () => {
  if(nextPage <= totalPages){
    pageCall(nextPage);
  }
})

favoritesTab.addEventListener('click', () => {
  console.log('clicked');
  showFavorite(favArr)
});

function pageCall(page){
  let urlSplit = lastUrl.split('?');
  let queryParams = urlSplit[1].split('&');
  let key = queryParams[queryParams.length -1].split('=');
  if(key[0] != 'page'){
    let url = lastUrl + '&page='+page
    getMovies(url);
  }else{
    key[1] = page.toString();
    let a = key.join('=');
    queryParams[queryParams.length -1] = a;
    let b = queryParams.join('&');
    let url = urlSplit[0] +'?'+ b
    getMovies(url);
  }
}

function openAccountForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeAccountForm() {
  document.getElementById("myForm").style.display = "none";
}
