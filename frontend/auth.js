let mode = "login";

function openLogin() {
    mode = "login";
    document.getElementById("modal-title").innerText = "Giriş Yap";
    document.getElementById("switch").innerHTML =
        "Hesabın yok mu? <a onclick='openSignup()'>Kayıt Ol</a>";
    document.getElementById("modal").classList.remove("hidden");
}

function openSignup() {
    mode = "signup";
    document.getElementById("modal-title").innerText = "Kayıt Ol";
    document.getElementById("switch").innerHTML =
        "Zaten hesabın var mı? <a onclick='openLogin()'>Giriş Yap</a>";
    document.getElementById("modal").classList.remove("hidden");
}

function closeModal() {
    document.getElementById("modal").classList.add("hidden");
}

async function submitAuth() {
    const email = email.value;
    const password = password.value;

    const endpoint = mode === "login" ? "/auth/login" : "/auth/signup";

    const res = await fetch(endpoint + `?email=${email}&password=${password}`, {
        method: "POST"
    });

    const data = await res.json();
    alert(JSON.stringify(data));
}

