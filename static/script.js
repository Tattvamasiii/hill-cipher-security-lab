const canvas =
    document.getElementById(
        "matrixCanvas"
    );

const ctx =
    canvas.getContext("2d");

canvas.width =
    window.innerWidth;

canvas.height =
    window.innerHeight;

const letters =
    "01ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const fontSize = 16;

const columns =
    canvas.width / fontSize;

const drops = [];

for (let i = 0; i < columns; i++) {

    drops[i] = 1;
}

function drawMatrixRain() {

    ctx.fillStyle =
        "rgba(0, 0, 0, 0.08)";

    ctx.fillRect(
        0,
        0,
        canvas.width,
        canvas.height
    );

    ctx.fillStyle = "#00ff99";

    ctx.font =
        fontSize + "px monospace";

    for (let i = 0; i < drops.length; i++) {

        const text =
            letters.charAt(
                Math.floor(
                    Math.random()
                    * letters.length
                )
            );

        ctx.fillText(
            text,
            i * fontSize,
            drops[i] * fontSize
        );

        if (
            drops[i] * fontSize
            > canvas.height
            &&
            Math.random() > 0.975
        ) {
            drops[i] = 0;
        }

        drops[i]++;
    }
}

setInterval(
    drawMatrixRain,
    40
);

window.addEventListener(
    "resize",
    () => {

        canvas.width =
            window.innerWidth;

        canvas.height =
            window.innerHeight;
    }
);

const matrixSize =
    document.getElementById(
        "matrixSize"
    );

const matrixInput =
    document.getElementById(
        "matrixInput"
    );

matrixSize.addEventListener(
    "change",
    () => {

        if (
            matrixSize.value === "2"
        ) {

            matrixInput.placeholder =
                "Example: 3 3 2 5";
        }

        else {

            matrixInput.placeholder =
                "Example: 6 24 1 13 16 10 20 17 15";
        }
    }
);

const cards =
    document.querySelectorAll(
        ".feature-card, .nav-card"
    );

cards.forEach(card => {

    card.addEventListener(
        "mouseenter",
        () => {

            card.style.transform =
                "scale(1.05)";
        }
    );

    card.addEventListener(
        "mouseleave",
        () => {

            card.style.transform =
                "scale(1)";
        }
    );
});