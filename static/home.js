$(document).ready(function(){
    $("img").attr("src", "https://icon-library.com/images/play-icon-png-transparent/play-icon-png-transparent-21.jpg");
    $("#machine").attr("src", "https://www.maketecheasier.com/assets/uploads/2021/12/morse-code-machine.jpeg")
    $("#butAccent").click(function() {
        window.location.href = "/learn"
    })
    $("#but").click(function() {
        window.location.href = "/quiz_home"
    })
});
function displayItems(data){
    //insert name data
    $.each(data, function(i, datum){
        let new_name= $("<div class='col-4 text-center'><a href='/view/"+datum["id"]+"'>"+datum["name"]+
            "<br><img class='small-img' img alt='" + datum["name"] + " logo' src='" + datum["logo"] + "'></a></div>")
        $("#popular_container").append(new_name)
    })
}
function play(name)
{
    let audio = new Audio('../static/audio/'+name+".wav");
    audio.play();
}
