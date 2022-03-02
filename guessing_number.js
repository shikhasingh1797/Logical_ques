console.log("🎄🎄You're welcome in guessing number game🎄🎄")
console.log("🎄🎄For guessing number you have only 5 cahnce")
var n = require("readline-sync");
var guess=n.question("Enter a num:")
var number_of_guesses = 0
var chance=5
while (number_of_guesses < 5){
  var guess1 = n.question("Guess number:")
    number_of_guesses++
    if (!(guess1==guess)){
      console.log("Your guess is wrong 😒😒")
      chance--
      console.log("You have only",chance," chance now 👉🏻")
    }
    if (guess1 == guess){
        break
}
}
    
if (guess1 === guess){
  console.log("🌸🌸🌸🌸 Congratulations , You won this game 🌸🌸🌸🌸")
}
    
else{
    console.log("Sorry , you lost the game" )
}