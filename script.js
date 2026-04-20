function startVoice() {

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert("Voice recognition not supported. Please use Google Chrome.");
        return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.start();

    const output = document.getElementById("voice-output");
    output.innerHTML = "Listening... 🎧";

    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;
        output.innerHTML = "You said: " + text;
    };

    recognition.onerror = function() {
        output.innerHTML = "Error detecting voice. Try again.";
    };
}