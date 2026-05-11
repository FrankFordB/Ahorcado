const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const intentosRestantes = parseInt(canvas.dataset.intentos);
const errores = 7 - intentosRestantes;

function drawBase() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.lineWidth = 4;
    ctx.strokeStyle = "#ffffff";
    ctx.fillStyle = "#ffffff";

    // base
    ctx.beginPath();
    ctx.moveTo(50, 350);
    ctx.lineTo(200, 350);
    ctx.stroke();

    // poste vertical
    ctx.beginPath();
    ctx.moveTo(100, 350);
    ctx.lineTo(100, 50);
    ctx.lineTo(250, 50);
    ctx.lineTo(250, 80);
    ctx.stroke();
}

function drawHangman(errores) {
    drawBase();

    if (errores >= 1) {
        ctx.beginPath();
        ctx.arc(250, 100, 20, 0, Math.PI * 2);
        ctx.stroke();
    }

    if (errores >= 2) {
        ctx.beginPath();
        ctx.moveTo(250, 120);
        ctx.lineTo(250, 200);
        ctx.stroke();
    }

    if (errores >= 3) {
        ctx.beginPath();
        ctx.moveTo(250, 140);
        ctx.lineTo(220, 170);
        ctx.stroke();
    }

    if (errores >= 4) {
        ctx.beginPath();
        ctx.moveTo(250, 140);
        ctx.lineTo(280, 170);
        ctx.stroke();
    }

    if (errores >= 5) {
        ctx.beginPath();
        ctx.moveTo(250, 200);
        ctx.lineTo(220, 240);
        ctx.stroke();
    }

    if (errores >= 6) {
        ctx.beginPath();
        ctx.moveTo(250, 200);
        ctx.lineTo(280, 240);
        ctx.stroke();
    }

    if (errores >= 7) {
        ctx.beginPath();
        ctx.arc(243, 95, 2, 0, Math.PI * 2);
        ctx.arc(257, 95, 2, 0, Math.PI * 2);
        ctx.fill();
    }
}

drawHangman(errores);
