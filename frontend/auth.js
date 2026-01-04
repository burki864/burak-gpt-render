const API = "https://burakgpt.onrender.com";

document.getElementById("loginBtn").onclick = () => {
  document.getElementById("loginModal").style.display = "block";
};

document.getElementById("signupBtn").onclick = () => {
  document.getElementById("signupModal").style.display = "block";
};

function closeModals() {
  document.querySelectorAll(".modal").forEach(m => m.style.display = "none");
}

function openSignup() {
  closeModals();
  document.getElementById("signupModal").style.display = "block";
}

function openLogin() {
  closeModals();
  document.getElementById("loginModal").style.display = "block";
}

async function login() {
  const email = loginEmail.value;
  const password = loginPassword.value;
  if (!email || !password) return alert("Email ve şifre zorunlu");

  const res = await fetch(API + "/auth/login", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({email, password})
  });

  const data = await res.json();
  if (!res.ok) return alert(data.detail);

  localStorage.setItem("token", data.token);
  location.reload();
}

async function signup() {
  const e = signupEmail.value;
  const p1 = signupPassword.value;
  const p2 = signupPassword2.value;

  if (!e || !p1 || !p2) return alert("Tüm alanlar zorunlu");
  if (p1 !== p2) return alert("Şifreler uyuşmuyor");

  const res = await fetch(API + "/auth/signup", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({email: e, password: p1})
  });

  const data = await res.json();
  if (!res.ok) return alert(data.detail);

  alert("Mailine doğrulama kodu gönderildi");
}

function googleLogin() {
  window.location.href = API + "/auth/google";
}
