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
