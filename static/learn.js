$(document).ready(function() {
    $("#next_button").click(function() {
        if (data["next_lesson"] == "end") {
            window.location.href = "/quiz/1"
        }
        else {
            window.location.href = "/learn/" + data["next_lesson"]
        }
    })
})