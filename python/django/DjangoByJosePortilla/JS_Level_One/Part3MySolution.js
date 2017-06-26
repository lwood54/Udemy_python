// Link this HTML file (JS_First_Exercise.html) to you own .js file
// Use Javascript to accept a number input in pounds (lbs)
// Then in your js file convert this number to kilograms (* 0.454)
// Afterwards report back in an alert what the weight is in kg
// Then log/write "Conversion Completed" to the console

var num = prompt("Number in pounds: ");
var inKilograms = num * .454;
alert("Your number in pounds: " + num + " in kilograms is: " + inKilograms + "kg");
console.log("Conversion completed");
