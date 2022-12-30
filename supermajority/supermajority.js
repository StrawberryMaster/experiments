window.onload = () => {
  voteForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const resultDiv = document.getElementById("result");

    // Get the values of the input fields
    const support = parseInt(document.getElementById("support").value, 10);
    const neutralLeaningSupport = parseInt(document.getElementById("neutralLeaningSupport").value, 10);
    const neutral = parseInt(document.getElementById("neutral").value, 10);
    const neutralLeaningOppose = parseInt(document.getElementById("neutralLeaningOppose").value, 10);
    const oppose = parseInt(document.getElementById("oppose").value, 10);

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