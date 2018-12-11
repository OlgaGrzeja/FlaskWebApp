
let alexa = window.SpeechRecognition 

function sluchaj(){
    console.log("wiem co powiedziałeś")
    alexa.start();
}

alexa.addEventListener('result', sluchaj);
alexa.start()

