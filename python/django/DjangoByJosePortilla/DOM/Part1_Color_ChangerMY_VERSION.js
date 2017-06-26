var colorInput = [];
var colorArray = [];
var colorLoopFlag = true;
var colorLoop;

// Grab the Header with h1
var header = document.querySelector("h1")

// Then you can interface with the object.
// Interface with the style.
//You will see a ton of options show up!
header.style.color = 'blue'

// PERSONAL MADE UP CHALLENGE: transition the colors through a color gradient
// If done right, then it will just look like a continuous changing color scheme

// get previous rgb #s and pass them through
// set conditions as to which ones will increase and assign
// new rgb values to previous values plus incriment
// add the new values to a global color array to be
// passed through changeHeaderColor() again.
function changeHeaderColor(prevR, prevG, prevB){
  var newR;
  var newG;
  var newB;
  colorInput = "rgb(" + prevR + "," + prevG + "," + prevB + ")"
  header.style.color = colorInput;
  if (prevR === 255 && prevG < 255 && prevB < 255) {
    newR = prevR;
    newG = prevG + 5;
    newB = prevB + 5;
  } else if (prevG === 255 && prevR > 0 && prevB > 0) {
    newR = prevR - 5;
    newG = prevG;
    newB = prevB - 5;
  } else if (prevB === 0 && prevR < 255 && prevG > 0) {
    newR = prevR + 5;
    newG = prevG - 5;
    newB = prevB;
  } else {
    newR = 255;
    newG = 0;
    newB = 0;
  }
  colorArray[0] = newR;
  colorArray[1] = newG;
  colorArray[2] = newB;
  console.log(colorArray);
}

// Now perform the action over intervals (milliseocnds):
function startLoop() {
  colorLoop = setInterval(function() {changeHeaderColor(colorArray[0],colorArray[1],colorArray[2]);},20);
  
}

function colorLoopOpposite() {
  if (colorLoopFlag) {
    clearInterval(colorLoop);
    colorLoopFlag = false;
  } else if (!colorLoopFlag) {
      startLoop();
      colorLoopFlag = true;
  }

}

header.addEventListener('mouseover', colorLoopOpposite, false);
