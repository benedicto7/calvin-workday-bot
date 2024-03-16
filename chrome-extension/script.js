// Add event listener to the chatbot input field
const API_URL = 'https://api-inference.huggingface.co/models';
const HUGGINGFACEHUB_API_TOKEN = "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"
const MODEL_NAME = "flan-ul2"

// Send a request to the Hugging Face's API
// const sendMessage = () => {
//   // Get the user's message from the input field
//   const message = document.getElementById('user-input').value;
//   document.getElementById('user-input').value = '';
//   document.getElementById('bot-response').innerHTML = `<p>${message}/p>`;

//   const body = JSON.stringify({
//     inputs: message,
//     parameters: {
//       "return_tensors": "pt",
//       "max_length": 1280,
//     },
//   });

//   const headers = {
//     'Content-Type': 'application/json',
//     Authorization: `Bearer ${API_KEY}`,
//   };

//   // Send the request to the Hugging Face's API
//   const response = await fetch(`${API_URL}/${MODEL_NAME}/predict`, {
//     method: 'POST',
//     headers: headers,
//     body: body,
//   });

//   const data = await response.json();
//   const responseText = data.predictions[0];

//   // Display the response in the Chrome extension
//   const botResponse = document.getElementById('bot-response');
//   botResponse.textContent = responseText;

//   return responseText;
// };

// sendButton.addEventListener('click', sendMessage);

const userInput = document.getElementById('user-input');
userInput.addEventListener('keyup', (event) => {
  if (event.key === 'Enter') {
    const message = document.getElementById('user-input').value;
    document.getElementById('user-input').value = '';
    document.getElementById('bot-response').innerHTML = message;
  }
});

var sendButton = document.getElementById("send-button");
sendButton.onclick = () => {
  // Get the user's message from the input field
  const message = document.getElementById('user-input').value;
  document.getElementById('user-input').value = '';
  document.getElementById('bot-response').innerHTML = message;
}