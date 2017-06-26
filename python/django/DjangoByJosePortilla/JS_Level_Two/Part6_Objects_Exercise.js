// Part 6 - Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function(){
    console.log(this.name.length - 1);
  }
}

employee.nameLength();

// Add a method called nameLength that prints out the
// length of the employees name to the console.


///////////////////
// PROBLEM 2 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}

// My initial idea:
for (var i in employee) {
  alert(i + " is " + employee[i])
}

// option 2 after research:
// Object.keys(employee).forEach(function (i) {
//   alert(i + " is " + employee[i]);
// });

// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert:
// Name is John Smith, Job is Programmer, Age is 31.



///////////////////
// PROBLEM 3 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName: function () {
    var nameArray = this.name.split(' ');
    console.log(nameArray[nameArray.length-1]);
  }
}
employee.lastName();
// Add a method called lastName that prints
// out the employee's last name to the console.

// You will need to figure out how to split a string to an array.
// Hint: http://www.w3schools.com/jsref/jsref_split.asp
