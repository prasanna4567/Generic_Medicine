$(document).ready(function () {
    $(function () {
        $("#searchBox").autocomplete({
            source: function (request, response) {
                $.ajax({
                    type: "POST",
                    url: "http://localhost:5000/search",
                    dataType: "json",
                    cache: false,
                    data: {
                        q: request.term
                    },
                    success: function (data) {
                        response(data);
                    },
                    error: function (jqXHR, textStatus, errorThrown) {
                        console.log(textStatus + " " + errorThrown);
                    }
                });
            },
            minLength: 1
        });
    });
});