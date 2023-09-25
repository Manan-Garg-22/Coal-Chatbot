function myFunction() { 
  document.getElementById("waving-hand").style.display="none"; 
  document.getElementById("chat-container").style.display="block"; 
}

let isWaving = true;

      function toggleWavingHand() {
        const emoji = document.getElementById("waving-hand");
        const chatContainer = document.getElementById("chat-container");

        if (isWaving) {
          emoji.style.animation = "none";
          chatContainer.style.display = "block";
        } else {
          emoji.style.animation = "waving-hand 2.5s infinite";
          chatContainer.style.display = "none";
        }

        isWaving = !isWaving;
        myFunction();
      }

        const chat = document.getElementById('chat');
        const userInput = document.getElementById('user-input');
        const sendButton = document.getElementById('send-button');
    
        sendButton.addEventListener('click', function () {
            const userMessage = userInput.value;
            displayUserMessage(userMessage);
            userInput.value = '';
    
            setTimeout(() => {
                const answer = 'This is a simple chatbot response.';
                displayBotMessage(answer);
            }, 1000);
        });
    
        function displayUserMessage(message) {
            const userdiv = document.createElement('div');
            userdiv.classList.add('user-bubble');
            userdiv.textContent = message;
            chat.appendChild(userdiv);
    
            setTimeout(() => {
                userdiv.style.opacity = 1;
                userdiv.style.transform = 'translateY(0)';
            }, 10); 
        }
    
        function displayBotMessage(message) {
            const ansdiv = document.createElement('div');
            ansdiv.classList.add('bot-bubble');
            ansdiv.textContent = message;
            chat.appendChild(ansdiv);
    
        
            setTimeout(() => {
                ansdiv.style.opacity = 1;
                ansdiv.style.transform = 'translateY(0)';
            }, 10);
        }
