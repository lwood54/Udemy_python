// THIS IS THE GOAL
// <div class="row">
//   <div class="gameboard col-md-2"></div>
//   <div class="gameboard col-md-2"></div>
// </div>

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

var colorOfChip = 'blue';

// make a gameboard by copying the div
    // make 6 rows
    for (var i = 0; i < 6; i++) {
      // create <div class="row"> and put inside #gameContainer
      // and create that 6 times.
      $('<div>').addClass('row r' + i).appendTo('#gameContainer');
    }

// I was successfully able to add this: .attr('id', 'r' + i+1) after
// $('<div>').addClass('row').attr('id', 'r' + i+1)
// I'm not going to use this, but I want to remember that this works

// GOOD INFO:
// http://stackoverflow.com/questions/12923970/jquery-addclass-to-element-generated-after-append
    // make 7 columns
    for (var i = 0; i < 7; i++) {
      // create <div class="gameboard"> and put inside each row
      // and create 7 columns
      $('<div>').addClass('gameboard c' + i).appendTo('.row');
    }

// GOAL:
    // I will have to create an algorithm that will test for 4 equal
    // colors in a row. The diagnoal will be hardest I think.
    // It will be something like "if r6,c1 === r5,c2 && r5,c2 === r4,c3 &&
    // r4,c3 === r3,c4", then winner. But I'll have to run that for the
    // whole board. Also testing for any 4 circles in a column or in a row
    // that are the same.
var columns = [];

//make array for each column
for (var i = 0; i < 7; i++) {
  columns[i] = $('.c' + i)
};

// if you click on a column, check the column circles starting at
// the bottom, if the bottom is blue or red, then move up
// keep checking until the class is not blue or red, then apply
// colored chip

$('.r5 .c0').addClass('blueChip');
$('.r4 .c0').addClass('redChip');


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
       alert("You are in column 0");
       for (var i = columns[0].length; i >= 0; i--) {
         if (!$(columns[0][i]).hasClass('blueChip') || !$(columns[0][i]).hasClass('redChip')) {
           // turn the color to current chip
           console.log("Location 1:" + colorOfChip);
           $(columns[0][i]).addClass(colorOfChip + "Chip");
           colorOfChipSwitch();
           return 0;
          //  break;
         };
       }
      //  colorOfChipSwitch();
      //  return 0;
      break;
    case isColumn1:
      alert("You are in column 1");
      return 1;
      break;
    case isColumn2:
      alert("You are in column 2");
      return 2;
      break;
    case isColumn3:
      alert("You are in column 3");
      return 3;
      break;
    case isColumn4:
      alert("You are in column 4");
      return 4;
      break;
    case isColumn5:
      alert("You are in column 5");
      return 5;
      break;
    case isColumn6:
      alert("You are in column 6");
      return 6;
      break;
    default:
      alert("Something went wrong.");
  }
}

// check for color starting at bottom, fill when empty
function fillChipSpace(element) {
  if ($(element).hasClass('.blueChip' || '.redChip')) {
    alert(0);
    return 0;
  } else {
    alert(0);
    return 1;
  }
}



// CREATING "click" event to drop chip
$(columns).each(function(i) {
  $(columns[i]).click(function() {
    var currentColor = checkColor(this);
    getColumnNum(this);



  })
})


// make a listening event for the circles of each row
    // once clicked, it should drop the correct color chip
    // to the next lowest position available on that column


// check if there are 4 dots of any one color in a row:
    // including up & down, left & right, or diagonal
