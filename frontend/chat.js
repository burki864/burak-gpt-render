const token = localStorage.getItem("token");

if (token) {
  document.getElementById("chatContainer").classList.remove("hidden");
}

async function sendMessage() {
  const msg = messageInput.value;
  if (!msg) return;

  const res = await fetch(API + "/chat", {
    method: "POST",
    headers: {
      "Authorization": "Bearer " + token,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({message: msg})
  });

  const data = await res.json();
  chatBox.innerHTML += `<p><b>Sen:</b> ${msg}</p>`;
  chatBox.innerHTML += `<p><b>BurakGPT:</b> ${data.reply}</p>`;
}
