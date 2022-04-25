$(document).ready(function() {
    $("#letters").click(function() {
        window.location.href = "/learn"
    })
})
function play(num)
{
    let audio = new Audio('../static/audio/'+data[num].audio);
    audio.play();
}