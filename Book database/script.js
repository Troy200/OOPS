class Book {
    constructor(name, author, date){
        this.name = name;
        this.author = author;
        this.date = date;
    }
}

let submitbook = (Book) => {
    list = document.getElementById("tb")
    row = document.createElement("tr")
    row.innerHTML = "<td>" + Book.name + "</td>  <td>" + Book.author + "</td> <td>" + Book.date + "</td>"
    list.appendChild(row)
}

document.querySelector("#formid").addEventListener("submit", addbook)

function addbook(e){
    e.preventDefault()
    name = document.querySelector("#nameimp").value;
    author = document.querySelector("#authorimp").value;
    date = document.querySelector("#dateimp").value;
    const book = new Book(name, author, date)
    submitbook(book)
}