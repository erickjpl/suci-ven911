//Desastre1

var modall3{{ archivo.id }} = document.getElementById("myModall3{{ archivo.id }}");
var btnn3{{ archivo.id }} = document.getElementById("myBtnn3{{ archivo.id }}");
var spann3{{ archivo.id }} = document.getElementsByClassName("closee3{{ archivo.id }}")[0];
btnn3{{ archivo.id }}.onclick = function() {
    modall3{{ archivo.id }}.style.visibility = "visible";
    modall3{{ archivo.id }}.style.opacity = 1;
}
spann3{{ archivo.id }}.onclick = function() {
    modall3{{ archivo.id }}.style.visibility = "hidden";
    modall3{{ archivo.id }}.style.opacity = 0;
}
window.onclick = function(event) {
    if (event.target == modall3{{ archivo.id }}) {
        modall3{{ archivo.id }}.style.visibility = "hidden";
        modall3{{ archivo.id }}.style.opacity = 0;
    }
}


// Desastre 2
var modall2{{ archivo.id }} = document.getElementById("myModall2{{ archivo.id }}");
var btnn2{{ archivo.id }} = document.getElementById("myBtnn2{{ archivo.id }}");
var spann2{{ archivo.id }} = document.getElementsByClassName("closee2{{ archivo.id }}")[0];
btnn2{{ archivo.id }}.onclick = function() {
    modall2{{ archivo.id }}.style.visibility = "visible";
    modall2{{ archivo.id }}.style.opacity = 1;

spann2{{ archivo.id }}.onclick = function() {
    modall2{{ archivo.id }}.style.visibility = "hidden";
    modall2{{ archivo.id }}.style.opacity = 0;

window.onclick = function(event) {
    if (event.target == modall{{ archivo.id }}) {
        modall2{{ archivo.id }}.style.visibility = "hidden";
        modall2{{ archivo.id }}.style.opacity = 0;
    }
}