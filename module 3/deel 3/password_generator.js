function generatePassword() {
    // Functie om een willekeurig element uit een array te kiezen
    function getRandomElement(array) {
        return array[Math.floor(Math.random() * array.length)];
    }

    
    function getRandomUppercase() {
        const uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        let uppercase = getRandomElement(uppercaseLetters.split(''));
        // Controleren of hoofdletter op 2 middelste posities staan.
        while (uppercase === password[11] || uppercase === password[12]) {
            uppercase = getRandomElement(uppercaseLetters.split(''));
        }
        return uppercase;
    }


    function getRandomLowercase() {
        const lowercaseLetters = "abcdefghijklmnopqrstuvwxyz";
        return getRandomElement(lowercaseLetters.split(''));
    }

    
    function getRandomSpecialChar() {
        const specialChars = "@#$%&_?";
        let specialChar = getRandomElement(specialChars.split(''));
        // Controleren of teken niet op eerste of laatste plek staat.
       while (specialChar === password[0] || specialChar === password[23]) {
            specialChar = getRandomElement(specialChars.split(''));
        }
        return specialChar;
    }

    
    function getRandomDigit() {
        return Math.floor(Math.random() * 10);
    }

    let password = "";

    // Genereer 2 tot 6 hoofdletters
    const numUppercase = Math.floor(Math.random() * 5) + 2;
    for (let i = 0; i < numUppercase; i++) {
        password += getRandomUppercase();
    }

    // Genereer minimaal 8 kleine letters
    for (let i = 0; i < 8; i++) {
        password += getRandomLowercase();
    }

    // Genereer 3 speciale tekens
    for (let i = 0; i < 3; i++) {
        password += getRandomSpecialChar();
    }

    // Genereer 4 tot 7 cijfers
    const numDigits = Math.floor(Math.random() * 4) + 4;
    for (let i = 0; i < numDigits; i++) {
        password += getRandomDigit();
    }

    // Controleer of het wachtwoord eindigt met een hoofdletter
    if (password.endsWith(getRandomUppercase())) {
        password = password.slice(0, -1) + getRandomLowercase();
    }

    return password;
}


console.log("Dit is je wachtwoord: " + generatePassword());
