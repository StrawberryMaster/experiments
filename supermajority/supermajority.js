window.onload = () => {
  const voteForm = document.getElementById("voteForm");
  const resultDiv = document.getElementById("result");
  const fields = ["support", "neutralLeaningSupport", "neutral", "neutralLeaningOppose", "oppose"];

  voteForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const values = fields.map(id => parseInt(document.getElementById(id).value, 10));

    // Validate input
    if (values.some(Number.isNaN)) {
      resultDiv.textContent = "Invalid input. Please enter a number for each category.";
      return;
    }
    if (values.every(v => v === 0)) {
      resultDiv.textContent = "All values are zero. The supermajority is 0%.";
      return;
    }

    // Supermajority calculation
    const totalVoters = values.reduce((a, b) => a + b);
    const weights = [100, 75, 50, 25, 0];
    const totalSum = values.reduce((sum, val, idx) => sum + val * weights[idx], 0);
    const supermajority = (totalSum / totalVoters).toFixed(2);

    // Display result
    resultDiv.textContent = supermajority >= 60
      ? `The supermajority is ${supermajority}%. The vote passes!`
      : `The supermajority is ${supermajority}%. The vote fails.`;
  });
};
