// create player objects:
var p1 = {
  name: prompt("Player One, what is your name?"),
  turn: true,
  chipColor: 'blue'
}
var p2 = {
  name: prompt("Player Two, what is your name?"),
  turn: false,
  chipColor: 'red'
}

$('#turn').text(p1.name + " : it's your turn!");

var colorOfChip;
$('button').on('click', function() {
  startGame();
});

function startGame() {
  playerTurn()
  clearBoard();
  colorOfChip = 'blue';
}
function clearBoard(){
  console.log("CLEARBOARD");
  $('.gameboard').removeClass('redChip blueChip');
}


function playerTurn() {
  if (p1.turn) {
    $('#turn').text(p1.name + " : it's your turn!");
    return p1.name;
  } else {
    $('#turn').text(p2.name + " : it's your turn!")
    return p2.name;
  }
}

// make a gameboard by copying the div
    // make 6 rows
    for (var i = 0; i < 6; i++) {
      // create <div class="row"> and put inside #gameContainer
      // and create that 6 times.
      $('<div>').addClass('row r' + i).appendTo('#gameContainer');
    }

    // make 7 columns
    for (var i = 0; i < 7; i++) {
      // create <div class="gameboard"> and put inside each row
      // and create 7 columns
      $('<div>').addClass('gameboard c' + i).appendTo('.row');
    }

//make array for each column
var columns = [];
for (var i = 0; i < 7; i++) {
  columns[i] = $('.c' + i)
};

// for reference: this is how to call a child within a specific
// parent class .r5 is in parent row class, .c0 is in child column class
// $('.r5 .c0').addClass('blueChip');
// $('.r4 .c0').addClass('redChip');

function colorOfChipSwitch() {
  if (colorOfChip === 'blue') {
    colorOfChip = 'red';
    p1.turn = false;
    p2.turn = true;
  } else {
    colorOfChip = 'blue';
    p2.turn = false;
    p1.turn = true;
  }
}

// WHAT I WANT:
  // find out column #, check if row at bottomw has a color
  // if no color, then apply current color chip

// Find out which column is being clicked.
function getColumnNum(element) {
  var isColumn0 = $(element).hasClass('c0');
  var isColumn1 = $(element).hasClass('c1');
  var isColumn2 = $(element).hasClass('c2');
  var isColumn3 = $(element).hasClass('c3');
  var isColumn4 = $(element).hasClass('c4');
  var isColumn5 = $(element).hasClass('c5');
  var isColumn6 = $(element).hasClass('c6');
  switch (true) {
    case isColumn0:
      return 0;
      break;
    case isColumn1:
      return 1;
      break;
    case isColumn2:
      return 2;
      break;
    case isColumn3:
      return 3;
      break;
    case isColumn4:
      return 4;
      break;
    case isColumn5:
      return 5;
      break;
    case isColumn6:
      return 6;
      break;
    default:
      return -1;
  }
}

// check for color starting at bottom, fill when empty
function fillEmptySlot(element) {
  var column = '.c' + getColumnNum(element);
    for (var i = 5; i >= 0 ; i--) {
      if(!slotFull('.r' + i + " " + column)) {
        $('.r' + i + " " + column).addClass(colorOfChip + 'Chip');
        break;
      }
    // BELOW: WAS THE CODE FOR ONE COLUMN...now all columns
    // represented in above code.

    // if(!slotFull('.r5 .c0')) {
    //   $('.r5 .c0').addClass(colorOfChip + 'Chip');
    // } else if(!slotFull('.r4 .c0')) {
    //   $('.r4 .c0').addClass(colorOfChip + 'Chip');
    // } else if(!slotFull('.r3 .c0')) {
    //   $('.r3 .c0').addClass(colorOfChip + 'Chip');
    // } else if(!slotFull('.r2 .c0')) {
    //   $('.r2 .c0').addClass(colorOfChip + 'Chip');
    // } else if(!slotFull('.r1 .c0')) {
    //   $('.r1 .c0').addClass(colorOfChip + 'Chip');
    // } else if(!slotFull('.r0 .c0')) {
    //   $('.r0 .c0').addClass(colorOfChip + 'Chip');
    // } else {
    //   alert("Slots are full.");
    // }

  }
  // return the next available element to fill
}

function slotFull(element) {
  if ($(element).hasClass('redChip') || $(element).hasClass('blueChip')) {
    return true;
  } else {
    return false;
  }
  // return true if called slot is full or false if empty
}


function dropChip(element, color) {
  fillEmptySlot(element);
  colorOfChipSwitch();
}


// CREATING "click" event to drop chip
$(columns).each(function(i) {
  var winner;
  $(columns[i]).click(function() {
    dropChip(this, colorOfChip);
    playerTurn();
    if (checkForWin()) {
      loser = playerTurn();
      if (loser === p1.name) {
        winner = p2.name;
      } else {
        winner = p1.name;
      }
      alert("Game Over! " + winner + " WON!!!");

    }
  })
});

// check if there are 4 dots of any one color in a row:
    // including up & down, left & right, or diagonal

// check for 4 of the same color
function colorMatchCheck(one,two,three,four){
  if (one === two && two === three && three === four && one !== 'gray') {
    return true;
  } else {
    return false;
  }
}

// get color of div
function checkColor(element) {
  var isRed = $(element).hasClass('redChip');
  var isBlue = $(element).hasClass('blueChip');
  if (isRed) {
    return 'red';
  } else if (isBlue) {
    return 'blue';
  } else {
    return 'gray';
  }
};


//check all win options:
function checkForWin() {
  if (checkDiagonalWin() || checkHorizontalWin() || checkVerticalWin()) {
    return true;
  } else {
    return false;
  }
}

// check for diagonal win
function checkDiagonalWin() {
  var one;
  var two_A;
  var three_A;
  var four_A;
  var two_B;
  var three_B;
  var four_B;
    for(var c = 0; c < 7; c++) {
      for (var r = 0; r < 6; r++) {
        one = checkColor('.r' +r + " .c" +c);
        two_A = checkColor('.r' +(r+1) + " .c" +(c+1));
        three_A = checkColor('.r' +(r+2) + " .c" +(c+2));
        four_A = checkColor('.r' +(r+3) + " .c" +(c+3));
        two_B = checkColor('.r' +(r-1) + " .c" +(c+1));
        three_B = checkColor('.r' +(r-2) + " .c" +(c+2));
        four_B = checkColor('.r' +(r-3) + " .c" +(c+3));
        if (colorMatchCheck(one, two_A, three_A, four_A)) {
          return true;
        } else if (colorMatchCheck(one, two_B, three_B, four_B)) {
          return true;
        }
      }
    }
    return false;
  // return true if 4 in a row
}
/// r5,c0 vs r4,c1 vs r3,c2 vs r2,c3


// check columns for win
function checkVerticalWin() {
  var one;
  var two;
  var three;
  var four;
    for(var c = 0; c < 7; c++) {
      for (var r = 0; r < 3; r++) {
        one = checkColor('.r' +r + " .c" +c);
        two = checkColor('.r' +(r+1) + " .c" +c);
        three = checkColor('.r' +(r+2) + " .c" +c);
        four = checkColor('.r' +(r+3) + " .c" +c);
        if (colorMatchCheck(one, two, three, four)) {
          return true;
        } else {
          continue;
        }
      }
    }
    return false;
  // return true if 4 in a row
}

//check rows for win
function checkHorizontalWin() {
  var one;
  var two;
  var three;
  var four;
  for (var r = 0; r < 6; r++) {
    for (var c = 0; c < 4; c++) {
      one = checkColor('.r' +r + " .c" +c);
      two = checkColor('.r' +r + " .c" +(c+1));
      three = checkColor('.r' +r + " .c" +(c+2));
      four = checkColor('.r' +r + " .c" +(c+3));
        if (colorMatchCheck(one, two, three, four)) {
          return true;
        } else {
          continue;
        }
      }
    }
    return false;
  // return true if 4 in a row
}




/////// ALTERNATE APPROACHE: Make each circle an object
/////// that has properties like color: ____, full: true/false
/////// column: ____, row: _____
///////   Then I should be able to get rid of the arrays and just
///////   check to see if a circle has certain properties in its object
