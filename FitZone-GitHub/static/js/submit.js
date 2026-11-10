document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("submit");

    button.addEventListener("click", async () => {
        const name = document.getElementById("product").value;

        const response = await fetch(
            "http://127.0.0.1:5000/search?name=" + encodeURIComponent(name)
        );

        const result = await response.text();
        document.getElementById("results").innerHTML = result;
    });
});

