$(document).ready(function() {
    $("#next_button").click(function() {
        if (data["next_lesson"] == "end") {
            window.location.href = "/quiz/0"
        }
        else {
            window.location.href = "/learn/" + data["next_lesson"]
        }
    })
    $("img").attr("src", "https://icon-library.com/images/play-icon-png-transparent/play-icon-png-transparent-21.jpg");
})
function play()
{
    let audio = new Audio('../static/audio/'+data["letter"]+".wav");
    audio.play();
}
function play1()
{
    let audio = new Audio('../static/audio/'+data["word1"]+".wav");
    audio.play();
}
function play2()
{
    let audio = new Audio('../static/audio/'+data["word2"]+".wav");
    audio.play();
}
function play3()
{
    let audio = new Audio('../static/audio/'+data["word3"]+".wav");
    audio.play();
}
