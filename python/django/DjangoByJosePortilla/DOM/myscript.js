var headOne = document.querySelector('#one');
var headTwo = document.querySelector('#two');
var headThree = document.querySelector('#three');

function changeTextContent(element, content) {
  element.textContent = content;
}

function changeTextColor(element, color) {
  element.style.color = color;
}

console.log("Connected");


headOne.addEventListener("mouseover", function(){
  // TRYING TO USE FUNCTIONS: (it works!)
  changeTextContent(headOne, "(with functions: mouse over text)");
  changeTextColor(headOne, "green");
  // COURSE INSTRUCTION:
  // headOne.textContent = "Mouse Currently Over Text!";
  // headOne.style.color = "green";
  // Just for fun:
  // headOne.textContent = prompt("What would you like this to say now?");
  // headOne.style.color = prompt("What color do you want the text?");
});

headOne.addEventListener("mouseout", function(){
  headOne.textContent = "HOVER OVER ME!";
  headOne.style.color = 'black';
});

headTwo.addEventListener("click", function(){
  if (headTwo.style.color === 'black') {
    headTwo.textContent = "I've been clicked, now what?! (Should I click again?)";
    headTwo.style.color = "orange";
  } else {
    headTwo.textContent = "CLICK ME!";
    headTwo.style.color = "black";
  };

});

headThree.addEventListener("dblclick", function(){
  if (headThree.style.color === 'black') {
    headThree.textContent = "I've been double clicked, now what?! (Should I double click again?)";
    headThree.style.color = "teal";
  } else {
    headThree.textContent = "DOUBLE CLICK ME!";
    headThree.style.color = "black";
  }

});
