class Movie {
    constructor(title, director, year){
        this.title = title;
        this.director = director;
        this.year = year 
    }
}


let submitmovie = (Movie) =>{
list = document.getElementById("tb") 
row = document.createElement("tr")
row.innerHTML = "<td>" + Movie.title + "</td>  <td>" + Movie.director + "</td> <td>" +  Movie.year + "</td>"
list.appendChild(row)

}

document.querySelector("formid").addEventListener("submit", addmovie)


function addmovie(e){
    e.preventDefault()
    title= document.querySelector("titleimp").value;
    director= document.querySelector("directorimp").value;
    year= document.querySelector("yearimp").value;
    const movie = new Movie(title, director,year)
    submitmovie(movie)
}