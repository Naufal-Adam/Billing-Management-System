"use strict"

$(document).ready(function () {
    $(".choices-single").each(function (index, element) {
        // element == this
        new Choices(this)
    });

    flatpickr(".flatpickr-date", {
        enableTime: false,
        dateFormat: "d-m-Y",
    });

    flatpickr(".flatpickr-time", {
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
    });

    $("#btn-submit").click(function (e) { 
        e.preventDefault();
        
        Swal.fire(
            'Good job!',
            'You clicked the button!',
            'success'
        );
    });
});