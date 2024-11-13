// tutorial file to test js on this machine
//
//Import the readline module to read user input

const readline = require('readline');

//create an interface for reading input from the console
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

// Ask the user for the first number
rl.question('Enter the first number: ', (first) => {

  // Ask the user for the second number
  rl.question('Enter the second number: ', (second) => {

	    // Convert the inputs to numbers and calculate the sum
	    const sum = parseFloat(first) + parseFloat(second);

	    // Print the result
	    console.log(`The sum of ${first} and ${second} is ${sum}`);

	    // Close the readline interface
	    rl.close();
  });
});
