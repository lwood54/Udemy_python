// USING FOR/OF

    // for every "i" (variable of my choosing) in an iterable element, like this array1
    // some action will take place. The action does not have to be related to the
    // variable, so I guess you could just use it as a counter
var array1 = ["up", "down", "left", "right", "turn", "spin", "hop", "jump"];
// for (i of array1) {
//   alert(i);
// }

  //Testing for:of as a counter
    // NOTE: in this case, num will not iterate unless it is outside the scope of this
    // for:of loop. So it seems that you can use this as a counter, but it seems
    // to pull the variable from outside the scope every time, so the only way
    // to modify and keep the change is to have the scope outside.
//   var num = 0;
// for (i of array1) {
//   alert(num);
//   console.log("hello");
//   num++;
// }
// console.log(num);




// USING FOR:EACH
// array1.forEach(alert);

function addAwesome(name) {
  alert(name + " is awesome!");
}

addAwesome("django");
var topics = ["python", "django", "science"];
topics.forEach(addAwesome);
    // NOTE: make sure that the function goes in the forEach(), but without the ()
    // to specify for the array, you do the array.forEach(function)



















// BOTTOM //
