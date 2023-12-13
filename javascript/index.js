const coffeeLimit = 100;
let coffeeCount = "99";

if (coffeeCount < coffeeLimit) {
    console.log("Võta võta");

} else if (coffeeLimit == Number(coffeeCount)) {
    console.log("Hoiatan, see oli viimane tass.");

} else {
    console.log("Pese mind.");
}