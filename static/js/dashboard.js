document.getElementById('botForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = document.getElementById('generateBtn');
    btn.innerText = "AI is thinking...";
    btn.disabled = true;

    const data = {
        name: document.getElementById('bizName').value,
        desc: document.getElementById('bizDesc').value,
        type: document.getElementById('bizType').value,
        phone: document.getElementById('bizPhone').value
    };

    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        
        if(result.status === 'success') {
            updatePreview(result.data.config);
            setTimeout(() => {
                window.location.href = '/preview';
            }, 2000);
        }
    } catch (err) {
        alert("Generation failed. Check console.");
    }
});

function updatePreview(config) {
    const chat = document.getElementById('chatWindow');
    document.getElementById('previewName').innerText = config.business_name;
    
    chat.innerHTML += `<div class="bubble user">Hello!</div>`;
    setTimeout(() => {
        chat.innerHTML += `<div class="bubble bot">${config.welcome_message}</div>`;
        chat.scrollTop = chat.scrollHeight;
    }, 800);
}