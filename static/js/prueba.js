// Obtenemos los elementos del menú y la información
const item1 = document.getElementById("item1");
const item2 = document.getElementById("item2");
const item3 = document.getElementById("item3");
const info1 = document.getElementById("info1");
const info2 = document.getElementById("info2");
const info3 = document.getElementById("info3");

// Asignamos eventos click a los elementos del menú
item1.addEventListener("click", () => {
    info1.style.display = "block";
    info2.style.display = "none";
    info3.style.display = "none";
});

item2.addEventListener("click", () => {
    info1.style.display = "none";
    info2.style.display = "block";
    info3.style.display = "none";
});

item3.addEventListener("click", () => {
    info1.style.display = "none";
    info2.style.display = "none";
    info3.style.display = "block";
});