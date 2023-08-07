"use strict"

$(document).ready(function () {
    $(document).on("click", "#edit-trigger", function (e) { 
        e.preventDefault();

        $("#username").removeAttr("disabled");
        $("#email").removeAttr("disabled");
        $("#depan").removeAttr("disabled");
        $("#belakang").removeAttr("disabled");
        $("#wa").removeAttr("disabled");
        $("#image").removeAttr("disabled");

        $("<button class='btn btn-outline-success' id='btn-img-change'>Change</button><button class='btn btn-outline-danger' id='btn-img-delete'>Remove</button>").appendTo("#trigger-container");
        $("<div class='d-flex gap-3 justify-content-end'><button class='btn btn-outline-success' id='btn-cancel'>Cancel</button><button class='btn btn-success' id='btn-update' type='submit'>Save Changes</button></div>").appendTo("form");
        
        $(this).remove();
    });

    $(document).on("click", "#btn-cancel" ,function (e) {
        e.preventDefault();

        $("#username").attr("disabled", true);
        $("#email").attr("disabled", true);
        $("#depan").attr("disabled", true);
        $("#belakang").attr("disabled", true);
        $("#wa").attr("disabled", true);
        $("#image").attr("disabled", true);

        $("#btn-img-change").remove();
        $("#btn-img-delete").remove();
        $("#btn-update").remove();

        $("<button class='btn btn-success' id='edit-trigger'>Edit</button>").appendTo("#trigger-container");

        $(this).remove();
    });
});