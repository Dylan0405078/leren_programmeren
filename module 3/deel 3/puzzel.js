
// vraag 1)
        //312211



function puzzle() {
    let sequence = ["1"]; 
    let currentLine = "1";

    while (true) {
        let nextLine = ""; 
        let count = 1;


        // i is positie teller om te cijfers te tellen en waarde word verhoogd tot aan dat hij het einde bereikt.
        for (let i = 0; i < currentLine.length; i++) {
            if (currentLine[i] === currentLine[i + 1]) {
                count++; // zorgt dat de line met 1 verlengt word
            } else {
                nextLine += count + currentLine[i]; 
                count = 1; // reset de teller voor het volgende cijfer
            }
        }
        sequence.push(nextLine); // pusht oude regel door voor een nieuwe regel en start opnieuw.
        currentLine = nextLine; // nieuwe regel gebruikt als huidige regel

        // controleren of er 2 "3" acher elkaar staan zo ja? break de loop
        if (currentLine.indexOf("33") !== -1) {
            break; 
        }
    }

    return sequence;
}

console.log(puzzle());
