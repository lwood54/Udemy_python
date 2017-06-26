
// THIS IS MY SOLUTION:
var firstName = prompt("What is your first name?");
var lastName = prompt("What is your last name?");
var age = prompt("What is your age?");
var height = prompt("What is your height in cm?");
var pet = prompt("What is your pet's name?")
alert("Thanks for the info.");


if (firstName[0] === lastName[0]) {
  if (age > 20 && age < 30) {
    if (height >= 170) {
      if (pet[pet.length - 1] === "y") {
        console.log("Congratulations spy, welcome aboard!");
      }
    }
  }
} else {
  console.log("Thanks for the info, have a nice day.");
}
