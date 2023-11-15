window.onload = () => {
  const voteForm = document.getElementById("voteForm");
  const resultDiv = document.getElementById("result");

  voteForm.addEventListener("submit", (event) => {
    event.preventDefault();

    // Get the values of the input fields
    const support = parseInt(document.getElementById("support").value, 10);
    const neutralLeaningSupport = parseInt(document.getElementById("neutralLeaningSupport").value, 10);
    const neutral = parseInt(document.getElementById("neutral").value, 10);
    const neutralLeaningOppose = parseInt(document.getElementById("neutralLeaningOppose").value, 10);
    const oppose = parseInt(document.getElementById("oppose").value, 10);

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
    const formattedSupermajority = supermajority.toFixed(2);

    // Update the result div with the result
    if (supermajority >= 60) {
      resultDiv.innerHTML = `The supermajority is ${formattedSupermajority}%. The vote passes!`;
    } else {
      resultDiv.innerHTML = `The supermajority is ${formattedSupermajority}%. The vote fails.`;
    }
  });
};