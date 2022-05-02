$(document).ready(function() {
    $("#but").click(function() {
        window.location.href = "/learn"
    })
    $("img").attr("src", "https://icon-library.com/images/play-icon-png-transparent/play-icon-png-transparent-21.jpg");
})
function play(num)
{
    let audio = new Audio('../static/audio/'+data[num].audio);
    audio.play();
}