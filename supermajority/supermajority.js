window.onload = () => {
  voteForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const resultDiv = document.getElementById("result");

    // Get the values of the input fields
    const support = Number(document.getElementById("support").value);
    const neutralLeaningSupport = Number(document.getElementById("neutralLeaningSupport").value);
    const neutral = Number(document.getElementById("neutral").value);
    const neutralLeaningOppose = Number(document.getElementById("neutralLeaningOppose").value);
    const oppose = Number(document.getElementById("oppose").value);

    // Stores all category values in an array
    const inputValues = [support, neutralLeaningSupport, neutral, neutralLeaningOppose, oppose];

    // Check if any of the input fields are blank
    if (inputValues.some(isNaN)) {
      resultDiv.innerHTML = "Invalid input. Please enter a number for each category.";
      return;
    }

    // Check if all inputted values are zero
    if (inputValues.every((input) => input === 0)) {
      resultDiv.innerHTML = "All inputted values are zero. The supermajority is 0%.";
      return;
    }

    // Calculate the total number of voters and the total sum of votes
    const totalVoters = support + neutralLeaningSupport + neutral + neutralLeaningOppose + oppose;
    const totalSum = support * 100 + neutralLeaningSupport * 75 + neutral * 50 + neutralLeaningOppose * 25;

    // Calculate the supermajority
    const supermajority = totalSum / totalVoters;

    // Format the supermajority as a percentage with two decimal places
    const formattedSupermajority = Number(supermajority).toFixed(2);

    // Update the result div with the result
    if (supermajority >= 60) {
      resultDiv.innerHTML = `The supermajority is ${formattedSupermajority}%. The vote passes!`;
    } else {
      resultDiv.innerHTML = `The supermajority is ${formattedSupermajority}%. The vote fails.`;
    }
  });
};