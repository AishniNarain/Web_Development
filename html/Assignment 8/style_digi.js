function showTime(){
    var currtime = new Date();

    var hour = currtime.getHours();
    var min = currtime.getMinutes();
    var sec = currtime.getSeconds();
    var session = "AM";

    

    if(hour >= 12){
        session = "PM";
    }
    else{
        session = "AM";
    }

    if(hour > 12){
        hour = hour- 12;
    }

    hour = hour < 10 ? "0"+hour : hour;
    min = min < 10 ? "0"+min : min;
    sec = sec < 10 ? "0"+sec : sec;

    var time = hour + " : " + min + " : "+ sec + "  " + session;
    document.getElementById("time").innerText = time;
}

setInterval(showTime, 1000)