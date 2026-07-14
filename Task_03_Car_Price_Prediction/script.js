// ==============================
// Car Price Prediction Dashboard
// ==============================

document.addEventListener("DOMContentLoaded", function () {

    // ==============================
    // Prediction Form
    // ==============================

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function (event) {

            const inputs = form.querySelectorAll("input, select");

            let valid = true;

            inputs.forEach(function (input) {

                if (input.value.trim() === "") {

                    valid = false;

                    input.style.border = "2px solid red";

                } else {

                    input.style.border = "1px solid #ccc";

                }

            });

            if (!valid) {

                event.preventDefault();

                alert("Please fill all fields.");

                return;

            }

            const button = form.querySelector("button");

            button.innerHTML = "Predicting...";

            button.disabled = true;

        });

    }

    // ==============================
    // Smooth Scroll
    // ==============================

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {

        anchor.addEventListener("click", function (e) {

            e.preventDefault();

            document.querySelector(this.getAttribute("href"))
                .scrollIntoView({

                    behavior: "smooth"

                });

        });

    });

    // ==============================
    // Prediction Result Animation
    // ==============================

    const result = document.querySelector(".result");

    if (result) {

        result.style.opacity = "0";

        result.style.transform = "translateY(30px)";

        result.style.transition = "all 0.6s ease";

        setTimeout(function () {

            result.style.opacity = "1";

            result.style.transform = "translateY(0px)";

        }, 300);

    }

});