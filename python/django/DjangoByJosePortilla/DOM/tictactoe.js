var boardSquare = document.querySelectorAll("td");
var playerOne = true;
var playerTwo = false;
var turnContent = document.querySelector("#turn");

var nextPlayer;
var winner;


var resetButton = document.querySelector("button");
resetButton.addEventListener("click", function() {
  boardSquare.forEach(function(i) {
    i.innerHTML = '';
    i.style.backgroundColor = "teal";
    i.style.color = "gray";
  });
  if (winner === "A") {
    nextPlayer = "E";
    playerOne = false;
    playerTwo = true;
    turnContent.innerHTML = "Now E get's to start!";
  } else if (winner === "E") {
    nextPlayer = "A";
    playerTwo = false;
    playerOne = true;
    turnContent.innerHTML = "Now A get's to start!";
  }

});


function checkForWin() {
  var box1 = document.getElementById("box1").innerHTML;
  var box2 = document.getElementById("box2").innerHTML;
  var box3 = document.getElementById("box3").innerHTML;
  var box4 = document.getElementById("box4").innerHTML;
  var box5 = document.getElementById("box5").innerHTML;
  var box6 = document.getElementById("box6").innerHTML;
  var box7 = document.getElementById("box7").innerHTML;
  var box8 = document.getElementById("box8").innerHTML;
  var box9 = document.getElementById("box9").innerHTML;

  if (box1 === box2 && box2 === box3) {
    if (box1 != '' && box2 != '' && box3 != '') {
      return true;
    }
  } else if (box4 === box5 && box5 === box6) {
      if (box4 != '' && box4 != '' && box6 != '') {
        return true;
      }
  } else if (box7 === box8 && box8 === box9) {
      if (box7 != '' && box8 != '' && box9 != '') {
        return true;
      }
  } else if (box1 === box4 && box4 === box7) {
      if (box1 != '' && box4 != '' && box7 != '') {
        return true;
      }
  } else if (box2 === box5 && box5 === box8) {
      if (box2 != '' && box5 != '' && box8 != '') {
        return true;
      }
  } else if (box3 === box6 && box6 === box9) {
      if (box3 != '' && box6 != '' && box9 != '') {
        return true;
      }
  } else if (box1 === box5 && box5 === box9) {
      if (box1 != '' && box5 != '' && box9 != '') {
        return true;
      }
  } else if (box3 === box5 && box5 === box7) {
      if (box3 != '' && box5 != '' && box7 != '') {
        return true;
      }
  } else {
      return false;
    }
};

function playerTurn() {
  if (playerOne) {
    playerOne = false;
    playerTwo = true;
    return "A";
  } else if (playerTwo){
    playerTwo = false;
    playerOne = true;
    return "E";
  }
}

boardSquare.forEach(function(i) {
  i.addEventListener("click", function() {
    var box = i.innerHTML;
    if (playerTurn() === "A") {
      i.innerHTML = "A";
      i.style.backgroundColor = "rgb(201, 88, 184)";
      i.style.color = "black";
      turnContent.innerHTML = "It's E's turn!";
      turnContent.style.color = "white";
      turnContent.style.backgroundColor = "rgb(107, 26, 165)";
    } else {
      i.innerHTML = "E";
      i.style.backgroundColor = "rgb(107, 26, 165)";
      i.style.color = "white";
      turnContent.innerHTML = "It's A's turn!";
      turnContent.style.color = "black";
      turnContent.style.backgroundColor = "rgb(201, 88, 184)";
    }
    if (checkForWin()) {
      nextPlayer = playerTurn();
      if (nextPlayer === "A") {
        winner = "E";
      } else if (nextPlayer === "E") {
        winner = "A";
      }
      alert(winner + " is the winner!!!");
    }
  });

})
