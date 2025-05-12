const getSleepHours = (day) => {
  switch(day) {
    case 'monday':
    return 8
    break;
    case 'tuesday':
    return 7
    break;
    case 'wednesday':
    return 6
    break;
    case 'thursday':
    return 8
    break;
    case 'friday':
    return 10
    break;
    case 'saturday':
    return 4
    break;
    case 'sunday':
    return 8
    break;
    defualt:
    return 'Error!'
  }
};

const getActualSleepHours = () => 
  getSleepHours('monday') +
  getSleepHours('tuesday') +
  getSleepHours('wednesday') +
  getSleepHours('thursday') +
  getSleepHours('friday') +
  getSleepHours('saturday') +
  getSleepHours('sunday');


console.log(getSleepHours('monday'));
console.log(getActualSleepHours());

const getIdealSleepHours = () => {
  let idealHours = 8;
  return idealHours * 7;
};

const calculateSleepDebt = () => {
  const actualSleepHours = getActualSleepHours();
  const idealSleepHours = getIdealSleepHours();

  if(actualSleepHours === idealSleepHours) {
    console.log("You've got the perfect amount of sleep.");
  }
  else if(actualSleepHours > idealSleepHours) {
    console.log("You've got " + (idealSleepHours - actualSleepHours) + " hours more sleep than needed.");
  }
  else if(actualSleepHours < idealSleepHours) {
    console.log('You should get ' + (idealSleepHours - actualSleepHours) +' hours more sleep');
  }
  else {
    console.log('Error! Something went wrong. Check your code.');
  }
};

calculateSleepDebt();
