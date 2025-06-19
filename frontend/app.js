document.getElementById('send').addEventListener('click', async () => {
    const input = document.getElementById('input');
    const token = document.getElementById('token').value;
    const text = input.value;
    if (!text) return;
    appendMessage('You', text);
    input.value = '';
    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': token },
        body: JSON.stringify({ message: text })
    });
    const data = await response.json();
    appendMessage('Bot', data.reply);
});

function appendMessage(sender, text) {
    const div = document.getElementById('messages');
    const p = document.createElement('p');
    p.textContent = sender + ': ' + text;
    div.appendChild(p);
    div.scrollTop = div.scrollHeight;
}
