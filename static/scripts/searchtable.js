function searchTable() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("search-input");
    filter = input.value.toUpperCase();
    table = document.getElementById("tableInfo");
    tr = table.getElementsByTagName("tr");

    var noResultsMessage = document.getElementById("no-results-message");
    var resultsFound = false;

    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0]; // берем первую ячейку строки (Зав. № машины)

        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
                resultsFound = true;
            } else {
                tr[i].style.display = "none";
            }
        }
    }

    // Показываем или скрываем сообщение об отсутствии результатов
    noResultsMessage.style.display = resultsFound ? "none" : "block";
}