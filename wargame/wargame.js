window.onload = () => {
    document.getElementById("battleForm").addEventListener("submit", (event) => {
        event.preventDefault();

        const nations = {
            Japan: { power: 7 },
            Turkey: { power: 5 },
            Australia: { power: 6 },
            Mexico: { power: 5 },
            Paraguay: { power: 3 },
            Chad: { power: 3 },
            Mongolia: { power: 4 },
            Madagascar: { power: 3 },
            TrinidadAndTobago: { power: 2 }
        };

        const nationNames = {
            Japan: "Japan",
            Turkey: "Turkey",
            Australia: "Australia",
            Mexico: "Mexico",
            Paraguay: "Paraguay",
            Chad: "Chad",
            Mongolia: "Mongolia",
            Madagascar: "Madagascar",
            TrinidadAndTobago: "Trinidad and Tobago"
        }

        function rollDice() {
            return Math.floor(Math.random() * 6) + 1;
        }

        const resultDiv = document.getElementById("result");

        // Get the values of the input fields
        const attacker = document.getElementById("attacker").value;
        const defender = document.getElementById("defender").value;

        // Check if attacker and defender are the same
        if (attacker === defender) {
            resultDiv.innerHTML = "Invalid input. Attacker and defender cannot be the same.";
            return;
        }

        // Check if any of the input fields are blank
        if (!attacker || !defender) {
            resultDiv.innerHTML = "Invalid input. Please select an attacker and defender.";
            return;
        }

        // Check if attacker or defender are not in the nations list
        if (!nations[attacker] || !nations[defender]) {
            resultDiv.innerHTML = "Invalid input. Please select a valid attacker and defender.";
            return;
        }

        const attackerRoll = rollDice();
        const defenderRoll = rollDice();
        const attackerNeeded = 10 - nations[attacker].power;
        const defenderNeeded = 10 - nations[defender].power;

        let result;
        if (attackerRoll >= attackerNeeded && defenderRoll < defenderNeeded) {
            result = `${nationNames[attacker]} has the advantage!`;
        } else if (defenderRoll >= defenderNeeded && attackerRoll < attackerNeeded) {
            result = `${nationNames[defender]} has the advantage!`;
        } else {
            result = `Neither side has the advantage! A tie occured.`;
        }
        document.getElementById("result").innerHTML = `Attacker: ${nationNames[attacker]} rolled ${attackerRoll}, needed ${attackerNeeded} <br> Defender: ${nationNames[defender]} rolled ${defenderRoll}, needed ${defenderNeeded} <br> ${result}`;
    });
};