"use strict"

$(document).ready(function () {
    setInterval(() => {
        let target = "January 24, 2023"
        $(".flatpickr-day").each(function () {
            // console.log($(this).attr("aria-label"));
            if($(this).attr("aria-label") == target) {
                $(this).attr("class", "flatpickr-day selected");
            }
        })
    }, 0);
});