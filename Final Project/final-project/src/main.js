import './style.css'

// Render modern chatbot UI
document.querySelector('#app').innerHTML = `
  <div class="chat-container">
    <div class="chat-header">
      <div class="status-dot"></div>
      <h2>AI Assistant</h2>
    </div>
    <div class="messages" id="messages">
      <div class="message bot">Hello! How can I help you today?</div>
    </div>
    <div class="chat-footer">
      <form id="chat-form">
        <input type="text" id="user-input" placeholder="Type your message..." required autocomplete="off" />
        <button type="submit" id="submit-btn">
          <span>Send</span>
        </button>
      </form>
      <div id="error-container"></div>
    </div>
  </div>
`;

const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const messagesContainer = document.getElementById('messages');
const submitBtn = document.getElementById('submit-btn');
const errorContainer = document.getElementById('error-container');

function addMessage(text, sender, isTyping = false) {
  const div = document.createElement('div');
  div.className = `message ${sender} ${isTyping ? 'typing' : ''}`;
  div.textContent = text;
  messagesContainer.appendChild(div);
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
  return div;
}

function showError(msg) {
  errorContainer.innerHTML = `<div class="error-msg">${msg}</div>`;
  setTimeout(() => {
    errorContainer.innerHTML = '';
  }, 5000);
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const question = input.value.trim();
  if (!question) return;

  // Clear and disable
  addMessage(question, 'user');
  input.value = '';
  input.disabled = true;
  submitBtn.disabled = true;

  // Typing indicator
  const typingMsg = addMessage('Assistant is thinking...', 'bot', true);

  try {
    const response = await fetch('http://localhost:8081/api/assistant/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question })
    });

    if (!response.ok) {
      throw new Error('Server responded with an error.');
    }

    const data = await response.json();

    // Remove typing indicator and add response
    messagesContainer.removeChild(typingMsg);
    addMessage(data.answer || 'I am not sure how to answer that.', 'bot');

  } catch (err) {
    console.error('Fetch error:', err);
    messagesContainer.removeChild(typingMsg);
    showError('Could not connect to the assistant. Please ensure the backend is running.');
  } finally {
    input.disabled = false;
    submitBtn.disabled = false;
    input.focus();
  }
});
