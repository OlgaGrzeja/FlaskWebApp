window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

//Dodajemy speech recogniton
let alexa = new SpeechRecognition();
let przycisk = document.querySelector('input')

function listen(e){
    console.log("Działam")
    console.dir(e)
}

alexa.addEventListener('result', listen)
przycisk.addEventListener('click', () => alexa.start() )
