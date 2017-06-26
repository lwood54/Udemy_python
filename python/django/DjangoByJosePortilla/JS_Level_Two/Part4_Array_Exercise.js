var roster = [];

function askChoice() {
  var choice = prompt("Please choose one of the following: 'add', 'remove', 'display', or 'quit'.")
  return choice;
}

function getFullName() {
  var firstName = prompt("What is the first name?");
  var lastName = prompt("What is the last name?");
  var fullName = firstName + " " + lastName;
  return fullName;
}

function addStudent() {
  var fullName = getFullName();
  var indexPos = roster.indexOf(fullName);
  if (indexPos > -1) {
    return alert("Sorry, that name already exists.")
  }
  roster.push(fullName);
  alert(fullName + " has been added.");
}

function removeStudent() {
  var fullName = getFullName();
  var indexPos = roster.indexOf(fullName);
  if (indexPos > -1) {
    roster.splice(indexPos, 1);
    alert(fullName + " hass been removed.");
  } else {
    return alert("Sorry, not on the list.");
  }
}

function displayRoster() {
  if (roster.length < 1) {
    return alert("Sorry, there are no names on this list.")
  }
  for (i of roster) {
    console.log(i);
  }
}

var choice = askChoice();

while (choice !== "quit") {
  if (choice === "add") {
    addStudent();
    choice = askChoice();
  } else if (choice === "remove") {
    removeStudent();
    choice = askChoice();
  } else if (choice === "display") {
    displayRoster();
    choice = askChoice();
  } else {
    alert("ERROR: Command not recognized. Please refresh to restart app.")
    choice = "quit";
  }
}
alert("Thanks for stopping by!");
