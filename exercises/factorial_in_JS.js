let x = parseInt(prompt("Wpisz liczbę, dla której chcesz obliczyć silnię"))
i = 1
s = 1
while (i <= x) {
    s = s * i
    i++
}
console.log(x + '!: ' + s)