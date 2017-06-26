var v = " GLOBAL V";

var stuff = "GLOBAL STUFF";

function fun(stuff) {
  console.log(v);
  stuff = "Reassign stuff inside fun";
  console.log(stuff);
}

fun()
alert(stuff);
