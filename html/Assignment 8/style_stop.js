let [seconds, minutes, hours] = [0,0,0];
let display_time = document.getElementById("time_display");
let timer = null;


function stopwatch(){
    seconds++;

    if( seconds == 60){
        seconds = 0;
        minutes++;
        
        if( minutes == 60){
            minutes = 0;
            hours++;
        }
    }

    
    
    let h = hours < 10 ? "0"+hours : hours;
    let min = minutes < 10 ? "0"+minutes : minutes;
    let sec = seconds < 10 ? "0"+seconds : seconds;

    display_time.innerHTML = h + ":" + min + ":" + sec;
}

function func_10(){
    if( timer !== null){
        clearInterval(timer)
    }
    timer = setInterval(stopwatch, 1000)
    setTimeout(()=>{
        clearInterval(timer)
    }, "10000"
    )
    // clearInterval(timer);
    // document.getElementById("time_display").innerHTML = "00:00:00";

}

function func_30(){
    watchReset()
    if( timer !== null){
        clearInterval(timer)
    }
    timer = setInterval(stopwatch, 1000)
    setTimeout(()=>{
        clearInterval(timer)
    }, "30000"
    )
}

function func_60(){
    watchReset()
    if( timer !== null){
        clearInterval(timer)
    }
    timer = setInterval(stopwatch, 1000)
    setTimeout(()=>{
        clearInterval(timer)
    }, "60000"
    )
}

function func_180(){
    watchReset()
    if( timer !== null){
        clearInterval(timer)
    }
    timer = setInterval(stopwatch, 1000)
    setTimeout(()=>{
        clearInterval(timer)
    }, "1800000"
    )
}

function watchReset(){
    clearInterval(timer);
    [seconds, minutes, hours] = [0,0,0];
    display_time.innerHTML = "00:00:00";
}

