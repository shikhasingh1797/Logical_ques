console.log("ππYou're welcome in guessing number gameππ")
console.log("ππFor guessing number you have only 5 cahnce")
var n = require("readline-sync");
var guess=n.question("Enter a num:")
var number_of_guesses = 0
var chance=5
while (number_of_guesses < 5){
  var guess1 = n.question("Guess number:")
    number_of_guesses++
    if (!(guess1==guess)){
      console.log("Your guess is wrong ππ")
      chance--
      console.log("You have only",chance," chance now ππ»")
    }
    if (guess1 == guess){
        break
}
}
    
if (guess1 === guess){
  console.log("πΈπΈπΈπΈ Congratulations , You won this game πΈπΈπΈπΈ")
}
    
else{
    console.log("Sorry , you lost the game" )
}