// // PART 5 LESSON ON JS Objects
// var carInfo = {make: "Toyota", year: 1990, model: "Camry"}
// // he introduced calling parts of the object like carInfo['make'];
// console.log(carInfo.make);
//
// alert(carInfo.year);
// // to change a value in the object
// carInfo.year = 2006;
// alert(carInfo.year);
//
// var myNewO = {a: "hello", b:[1,2,3], c: {inside: ['a','b','c']}}
// console.log(myNewO);
//
// console.log(myNewO.b[1]);
//
// // to show the entire object
//
// console.dir(carInfo);
//
//
// // Using a for:in loop
// for (key in carInfo) {
//   console.log(key + ": " + carInfo[key]);
// }


// USING "this"
// var simple = {
//   prop : "Hello",
//   myMethod : function() {
//     console.log("The myMethod was called");
//   }
// }
// console.log(simple.prop);
// simple.myMethod();



var myObj = {
  name : "Logan",
  greet : function(){
    console.log("Hello " + this.name);
  }
}
myObj.greet();
