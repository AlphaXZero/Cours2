const taskDuration = [25, 40, 15, 60, 5, 45]
const task = ["Send email", "harrass supplier", "prepare months report", "call the client to sell some useless things"]
const users = [
    { prenom: "Nour", nom: "El Amrani" },
    { prenom: "Marc", nom: "Renard" },
    { prenom: "Sophie", nom: "Lambert" }
];
const products = [
    { nom: "Clavier", prixHT: 40 },
    { nom: "Souris", prixHT: 25 },
    { nom: "Écran 24 pouces", prixHT: 199 }
];
const taxRate = 0.21;
const reviews = [
    { auteur: "Alice", note: 5 },
    { auteur: "Marc", note: 1 },
    { auteur: "Luc", note: 3 },
    { auteur: "Nour", note: 4 },
    { auteur: "Sophie", note: 2 }
];
function playMysteryNumber() {
    let counter = 1;
    const minValue = Number(document.getElementById("minValue").value);
    const maxValue = Number(document.getElementById("maxValue").value);
    const mysteryNumber = Math.floor(Math.random() * (maxValue - minValue + 1)) + minValue;
    while (true) {
        const userInput = Number(prompt(`Guess the mystery number between ${minValue} and ${maxValue}:`));
        if (userInput === mysteryNumber) {
            alert(`Congratulations! You've guessed the number ${mysteryNumber} in ${counter} attempts.`);
            break;
        } else if (userInput < mysteryNumber) {
            alert("Too low! Try again.");
        } else if (userInput > mysteryNumber) {
            alert("Too high! Try again.");
        }
        counter++;
    }

}
const user2 = [
    { email: "alice@example.com", accepteNewsletter: true, actif: true },
    { email: "marc@example.com", accepteNewsletter: false, actif: true },
    { email: "nour@example.com", accepteNewsletter: true, actif: false },
    { email: "sophie@example.com", accepteNewsletter: true, actif: true }
];

const products2 = [
    { nom: "Souris sans fil", categorie: "accessoires", stock: 12 },
    { nom: "Clavier mécanique", categorie: "accessoires", stock: 0 },
    { nom: "Écran 27 pouces", categorie: "ecrans", stock: 5 },
    { nom: "Tapis de souris XL", categorie: "accessoires", stock: 7 }
];

const orders = [120, 90, 45, 230];

const sessions = [
    { pseudo: "Alice", dureeMinutes: 30 },
    { pseudo: "Marc", dureeMinutes: 45 },
    { pseudo: "Nour", dureeMinutes: 25 },
    { pseudo: "Sophie", dureeMinutes: 50 }
];

const taches = [
    { intitule: "Envoyer le contrat", terminee: true },
    { intitule: "Relancer le client", terminee: false },
    { intitule: "Mettre à jour le dossier", terminee: true },
    { intitule: "Archiver les anciens mails", terminee: false }
];



function showLottoResults() {
    const numberAmmount = Number(document.getElementById("numberAmount").value);
    const minValue = Number(document.getElementById("minValueLotto").value);
    const maxValue = Number(document.getElementById("maxValueLotto").value);
    const userNumbers = [];
    let flag = true;
    for (let i = 0; i < numberAmmount; i++) {
        let randomNumber = Math.floor(Math.random() * (maxValue - minValue + 1)) + minValue;
        if (maxValue - minValue < numberAmmount) {
            flag = false;
            break;
        }
        else if (userNumbers.includes(randomNumber)) {
            i--;
            continue;
        } else {
            userNumbers.push(randomNumber);
        }
    }
    if (flag) {
        document.getElementById("lottoResults").innerHTML = `Your lotto numbers are: ${userNumbers.join(", ")} `;
    }
    else {
        document.getElementById("lottoResults").innerHTML = "Range too small for the amount of unique numbers requested.";
    }
}

const generateServerStatusMessage = () => {
    const isMaintenance = true;

    if (isMaintenance) {
        return "server is under maintenance, please try again later.";
    } else {
        return "server is working normally.";
    }
};

function displayServerStatus() {
    const statusMessage = generateServerStatusMessage();
    document.getElementById("serverStatus").innerHTML = `The ${statusMessage}`;
}

const formatTaskMessage = (taskAmmount) => {
    if (taskAmmount <= 0) { return "You have no tasks to complete."; }
    else if (taskAmmount === 1) { return "You only have 1 task to complete."; }
    else { return `You have ${taskAmmount} tasks to complete.`; }
}

function showTaskMessage() {
    const taskAmmount = Number(document.getElementById("taskAmmount").value);
    const message = formatTaskMessage(taskAmmount);
    document.getElementById("taskMessage").innerHTML = message;
}

const calculatePriceWithTax = (price, taxRate) => {
    return price + (price * taxRate / 100);
}

const calculateTotalPrice = (unitPrice, quantity, taxRate) => {
    const priceWithTax = calculatePriceWithTax(unitPrice, taxRate);
    return priceWithTax * quantity;
}

function displayTotalPrice() {
    const unitPrice = Number(document.getElementById("unitPrice").value);
    const quantity = Number(document.getElementById("quantity").value);
    const taxRate = Number(document.getElementById("taxRate").value);
    const totalPrice = calculateTotalPrice(unitPrice, quantity, taxRate);
    document.getElementById("totalPrice").innerHTML = `The total price is: $${totalPrice.toFixed(2)}`;
}

const isLongTask = (duration) => {
    return duration >= 30;
}

const filterLongTasks = (tasks) => {
    const longTasks = [];
    for (let i = 0; i < tasks.length; i++) {
        if (isLongTask(tasks[i])) {
            longTasks.push(tasks[i]);
        }
    }
    return longTasks;
}

function displayLongTasks() {
    const longTasks = filterLongTasks(taskDuration);
    document.getElementById("longTasks").innerHTML = `All tasks: ${taskDuration.join(", ")}<br>Long tasks (30 mins or more): ${longTasks.join(", ")}`;
}

const applyOperation = (a, b, operation) => {
    const result = operation(a, b);
    document.getElementById("operationResult").innerHTML += `The result of the operation ${a} ${operation.name} ${b} is: ${result}<br>`;
}

const add = (x, y) => x + y;
const subtract = (x, y) => x - y;
const average = (x, y) => (x + y) / 2;

function showOperations() {
    const num1 = Math.floor(Math.random() * 100);
    const num2 = Math.floor(Math.random() * 100);


    applyOperation(num1, num2, add);
    applyOperation(num1, num2, subtract);
    applyOperation(num1, num2, average);
}

const forEachTask = (tasks, action) => {
    for (let i = 0; i < tasks.length; i++) {
        action(tasks[i], i);
    }
}

const showTaskWithIndex = (task, index) => {
    document.getElementById("tasksWithIndex").innerHTML += `Task ${index}: ${task}<br>`;
}

const showTaskIfLong = (task, index) => {
    if (task.length > 25) {
        document.getElementById("tasksWithIndex").innerHTML += `Task ${index}: ${task}<br>`;
    }
}



function showTasks() {
    document.getElementById("tasksWithIndex").innerHTML += `Tasks:<br>`;
    forEachTask(task, showTaskWithIndex);
    document.getElementById("tasksWithIndex").innerHTML += `Long Tasks:<br>`;
    forEachTask(task, showTaskIfLong);
}

const executeIfConnected = (isConnected, action) => {
    if (isConnected) {
        action();
    } else {
        document.getElementById("connectionStatus").innerHTML = "User is not connected. Please log in.";
    }
}

function showConnectionStatusTrue(bool) {
    executeIfConnected(bool, () => {
        document.getElementById("connectionStatus").innerHTML = "User is connected. Welcome back!";
    });
}

const formatTask = (taskName) => {
    return `→ ${taskName}`;
}

function displayFormattedTasks() {
    const formattedTasks = task.map(formatTask).join("<br>");
    document.getElementById("formattedTasks").innerHTML = formattedTasks;
}

const formatName = (user) => {
    return `${user.prenom} ${user.nom}`;
}

function displayUserNames() {
    const formattedNames = users.map(formatName).join("<br>");
    document.getElementById("userNames").innerHTML = formattedNames;
}

const formatProductPrice = (product) => {
    const formattedProduct = { nom: product.nom, prixHT: product.prixHT.toFixed(2), prixTTC: calculatePriceWithTax(product.prixHT, taxRate * 100).toFixed(2), libelle: `${product.nom} : ${calculatePriceWithTax(product.prixHT, taxRate * 100).toFixed(2)} € TTC` };
    return formattedProduct;
}
function displayProductPrices() {
    const formattedProducts = products.map(formatProductPrice);
    document.getElementById("productPrices").innerHTML = formattedProducts.map(p => `${p.nom}, ${p.prixHT}, ${p.prixTTC}, ${p.libelle}`).join("<br>");
}

function displayPositiveReviews() {
    const positiveReviews = reviews.filter(review => review.note >= 3);
    document.getElementById("length").innerHTML = "number of reviews: " + positiveReviews.length;
    document.getElementById("positiveReviews").innerHTML = "positive reviews: <br>" + positiveReviews.map(r => `${r.auteur}: ${r.note}`).join("<br>");
}

function displayActiveUsers() {
    const activeUsers = user2.filter(user => user.actif && user.accepteNewsletter);
    document.getElementById("activeUsers").innerHTML = "Active users subscribed to newsletter: <br>" + activeUsers.map(u => `email: ${u.email}, accepteNewsletter: ${u.accepteNewsletter}, actif: ${u.actif}`).join("<br>");
}

function displayAvailableProducts() {
    const availableProducts = products2.filter(product => product.categorie === "accessoires" && product.stock > 0);
    document.getElementById("availableProducts").innerHTML = "Available accessories in stock: <br>" + availableProducts.map(p => `nom: ${p.nom}, categorie: ${p.categorie}, stock: ${p.stock}`).join("<br>");
}

function displaySales() {
    const highValueOrders = orders.reduce((acc, current) => acc + current, 0);
    document.getElementById("sales").innerHTML = "Total sales: " + highValueOrders;
}

function displayAverageSessionTime() {
    const totalDuration = sessions.reduce((acc, session) => acc + session.dureeMinutes, 0);
    const averageDuration = totalDuration / sessions.length;
    document.getElementById("totalSessionTime").innerHTML = "Total session duration: " + totalDuration + " minutes";
    document.getElementById("averageSessionTime").innerHTML = "Average session duration: " + averageDuration.toFixed(2) + " minutes";
}

function displayFinishedTasksStats() {
    const finishedTasks = taches.reduce((acc, tache) => tache.terminee ? acc + 1 : acc, 0);
    document.getElementById("finishedTasks").innerHTML = `${finishedTasks} tasks completed out of ${taches.length}.`;

}