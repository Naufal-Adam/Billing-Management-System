"use strict"

$(document).ready(function () {
    $("#datatables-ajax").DataTable({
        // "ajax": "tables-datatables-ajax.json"
        responsive: true,
    });

    $(".choices-single").each(function (index, element) {
        // element == this
        new Choices(this)
    });
});