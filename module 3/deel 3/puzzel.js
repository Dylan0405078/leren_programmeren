

//312211



function lookAndSaySequence() {
    let sequence = ["1"]; // start met de eerste regel
    let currentLine = "1";

    while (true) {
        let nextLine = ""; // de volgende regel opbouwen
        let count = 1;
        for (let i = 0; i < currentLine.length; i++) {
            if (currentLine[i] === currentLine[i + 1]) {
                count++; // het aantal keer dat het huidige cijfer voorkomt
            } else {
                nextLine += count + currentLine[i]; // het aantal keer dat het cijfer voorkomt, gevolgd door het cijfer zelf
                count = 1; // reset de teller voor het volgende cijfer
            }
        }
        sequence.push(nextLine); // voeg de volgende regel toe aan de reeks
        currentLine = nextLine; // zet de volgende regel in als de huidige regel

        // controleer of er twee opeenvolgende "3"s in de huidige regel zijn
        if (currentLine.indexOf("33") !== -1) {
            break; // als er twee opeenvolgende "3"s zijn, stop dan de loop
        }
    }

    return sequence;
}

console.log(lookAndSaySequence());
