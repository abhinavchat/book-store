// IIFE Module for Book app
var app = (function(){
    console.log('hello');
    var searchBooks = function() {
        // Declare variables
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("tblSearch");
        filter = input.value.toUpperCase();
        table = document.getElementById("tblBooks");
        tr = table.getElementsByTagName("tr");

        // Loop through all table rows, and hide those who don't match the search query
        for (i = 0; i < tr.length; i++) {
            tdTitle = tr[i].getElementsByTagName("td")[1];
            tdAuthor = tr[i].getElementsByTagName("td")[3];
            if (tdTitle || tdAuthor) {
            if (tdTitle.textContent.toUpperCase().indexOf(filter) > -1 || tdAuthor.textContent.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
            }
        }
    };

    return {
        searchBooks: searchBooks
    }
})();