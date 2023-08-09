"use strict"

$(document).ready(function () {
    $(document).on("click", "#edit-trigger", function (e) { 
        e.preventDefault();

        window.location.href = "edit"
    });

    $(document).on("click", "#btn-cancel" ,function (e) {
        e.preventDefault();

        let previousPageUrl = document.referrer;
        let target = "edit/"

        previousPageUrl = previousPageUrl.replace(target, "");
        window.location.href = previousPageUrl;
    });

    $("#upload-button").click(function (e) { 
        e.preventDefault();
        $("#file").click()
    });

    $("#file").change(function (e) { 
        if (this.value) {
            $("#custom-msg").html(
                this.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1]
            )
            
        }else {
            $("#custom-msg").html("No file chosen, yet.")
        }
    });
});