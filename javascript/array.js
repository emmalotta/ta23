const cats = ["Leopard", "Serval", "Jaguar", "Tiger", "Carcal", "Lion"]

// for loop

for (let index = 0; index < cats.length; index++){
    console.log(cats[index].toUpperCase())
}

// forEach loop

cats.forEach((cat) => {
    console.log(cat.toUpperCase())
});