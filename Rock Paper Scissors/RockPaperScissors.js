
const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
  if (userInput === 'rock' || userInput === 'scissors' || userInput === 'paper' || userInput === 'bomb') {
      return userInput;
  } else {
      console.log('Error, please type: rock, paper or scissors.')
  }
}

const getComputerChoice = () => {
  const randomNumber = Math.floor(Math.random() * 3)
  switch (randomNumber) {
    case 0:
      return 'rock';
    case 1:
      return 'scissors';
    case 2:
      return 'paper';
  }
};

const determineWinner = (userChoice, computerChoice) => {
  if (userChoice === computerChoice) {
    return 'This game is a tie!';
  }
  if (userChoice === 'rock') {
    if (computerChoice === 'paper') {
      return "Sorry the computer won!"
    } else {
      return "Congratulations, you won!"
    }
  }

  if (userChoice === 'paper') {
    if (computerChoice === 'scissors') {
      return "Sorry, computer won!";
    } else {
      return "Congratulations, you won!";
      }
    }

  if (userChoice === 'scissors') {
    if (computerChoice === 'rock') {
      return "Sorry, computer won!";
    }
    else {
      return "Congratulations, you won!"
    }
  }

  if (userChoice === 'bomb') {
    return "Congratulations, you did 911."
  }
};

const playGame = () => {
  const userChoice = getUserChoice('rock');
  const computerChoice = getComputerChoice();
  console.log('You threw: ' + userChoice);
  console.log('The computer threw: ' + computerChoice);

  console.log(determineWinner(userChoice, computerChoice))
};

playGame()
