class Calculator {
    constructor(prv, currentOperandTextElement) {
        this.previousOperand = prv;
        this.currentOperandTextElement = currentOperandTextElement;
        this.lastnumber = 0;
        this.update = false;
        this.y = ["÷", "*", "+", "-"];
        this.clear();
    }
    multColorButton(button) {
        this.y.forEach((op) => {
            document.getElementById(op).style.background =
                "rgba(114, 114, 114, 0.75)";
        });
        var x = document.getElementById(button);
        x.style.background = "green";
    }

    clear() {
        this.y.forEach((op) => {
            document.getElementById(op).style.background =
                "rgba(114, 114, 114, 0.75)";
        });
        this.currentOperand = "";
        this.previousOperand = "";
        this.lastnumber = 0;
        this.update = false;
        this.operation = undefined;
    }

    delete() {
        this.currentOperand = this.currentOperand.toString().slice(0, -1);
    }

    appendNumber(number) {
        this.y.forEach((op) => {
            if (document.getElementById(op).style.background === "green") {
                document.getElementById(op).style.background =
                    "rgba(114, 114, 114, 0.75)";
            }
        });
        if (number === "." && this.currentOperand.includes(".")) return;
        this.currentOperand = this.currentOperand.toString() + number.toString();
    }

    chooseOperation(operation) {
        if (this.currentOperand === "") return;
        if (this.previousOperand !== "") {
            this.compute();
            this.updateDisplay();
        }
        this.update = true;
        this.operation = operation;
        this.previousOperand = this.currentOperand;
        this.currentOperand = "";
    }

    compute(equals = "") {
        if (this.update === true) {
            this.lastnumber = parseFloat(this.currentOperand);
            this.update = false;
        }
        if (equals === "=") {
            this.y.forEach((op) => {
                document.getElementById(op).style.background =
                    "rgba(114, 114, 114, 0.75)";
            });
        }
        let computation;
        let prev = parseFloat(this.previousOperand);
        const current = parseFloat(this.currentOperand);
        if (isNaN(current)) {
            return;
        }
        if (isNaN(prev)) {
            prev = this.lastnumber;
        }
        switch (this.operation) {
            case "+":
                computation = prev + current;
                break;
            case "-":
                computation = prev - current;
                break;
            case "*":
                computation = prev * current;
                break;
            case "÷":
                computation = prev / current;
                break;
            default:
                return;
        }

        this.currentOperand = computation;
        // this.operation = undefined;
        this.previousOperand = "";
    }

    getDisplayNumber(number) {
        const stringNumber = number.toString();
        const integerDigits = parseFloat(stringNumber.split(".")[0]);
        const decimalDigits = stringNumber.split(".")[1];
        let integerDisplay;
        if (isNaN(integerDigits)) {
            integerDisplay = "";
        } else {
            integerDisplay = integerDigits.toLocaleString("en", {
                maximumFractionDigits: 0,
            });
        }
        if (decimalDigits != null) {
            integerDisplay = `${integerDisplay}.${decimalDigits}`;
        }

        return integerDisplay;
    }

    updateDisplay() {
        this.currentOperandTextElement.innerText = this.getDisplayNumber(
            this.currentOperand
        );
    }
}

const numberButtons = document.querySelectorAll("[data-number]");
const operationButtons = document.querySelectorAll("[data-operation]");
const deleteButton = document.querySelector("[data-delete]");
const allClearButton = document.querySelector("[data-all-clear]");

const currentOperandTextElement = document.querySelector(
    "[data-current-operand]"
);

const calculator = new Calculator("", currentOperandTextElement);

numberButtons.forEach((button) => {
    button.addEventListener("click", () => {
        calculator.appendNumber(button.innerText);
        calculator.updateDisplay();
    });
});

operationButtons.forEach((button) => {
    button.addEventListener("click", () => {
        calculator.multColorButton(button.innerText);
        calculator.chooseOperation(button.innerText);
        // calculator.updateDisplay();
    });
});

function equalsButton() {
    calculator.compute("=");
    calculator.updateDisplay();
}

allClearButton.addEventListener("click", (button) => {
    calculator.clear();
    calculator.updateDisplay();
});

deleteButton.addEventListener("click", (button) => {
    calculator.delete();
    calculator.updateDisplay();
});