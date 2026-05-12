const miForm = document.getElementById("miForm");
if (miForm) miForm.addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const res = await fetch("/", { method: "POST", body: formData });
    const html = await res.text();

    const doc = new DOMParser().parseFromString(html, "text/html");

    document.querySelector(".box_palabras").innerHTML = doc.querySelector(".box_palabras").innerHTML;
    document.querySelector(".dibujo p").innerHTML = doc.querySelector(".dibujo p").innerHTML;
    document.querySelector(".modal").style.display = doc.querySelector(".modal").style.display;
    document.getElementById("input_clean").value = "";
    document.getElementById("input_clean").focus();

    const intentosActuales = parseInt(doc.querySelector(".box_palabras").dataset.intentos);
    drawHangman(7 - intentosActuales);
});

const switchVolver = document.getElementById("switchVolver");


if (window.location.pathname === "/wikipedia") {
    switchVolver.checked = true;
}

switchVolver.addEventListener("change", function () {
    if (this.checked) {
        window.location.href = "/wikipedia";
    } else {
        window.location.href = "/";
    }
});
