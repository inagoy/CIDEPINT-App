/**
 * Validates an email address entered in an input field and displays an error message if the email format is invalid.
 *
 * @param {string} inputId - The id of the input field containing the email address.
 * @param {string} errorId - The id of the element where the error message should be displayed.
 * @return {void} This function does not return anything.
 */
function validateEmail(inputId, errorId) {
	const emailInput = document.getElementById(inputId);
	const emailError = document.getElementById(errorId);
	const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

	if (!emailPattern.test(emailInput.value)) {
		emailError.textContent = "Formato de mail inválido. Intente nuevamente";
		return false;
	} else {
		emailError.textContent = "";
		return true;
	}
}

function validateJustText(inputId, errorId) {
	const input = document.getElementById(inputId);
	const error = document.getElementById(errorId);
	const pattern = /^[\p{L}\s´]+$/u;

	if (!pattern.test(input.value)) {
		error.textContent = "Solo se permiten letras y espacios";
		return false;
	} else {
		error.textContent = "";
		return true;
	}
}

function validateJustNumber(inputId, errorId) {
    const input = document.getElementById(inputId);
    const error = document.getElementById(errorId);
    const pattern = /^\d+$/; // Pattern for numbers only

    if (!pattern.test(input.value)) {
        error.textContent = "Solo se permiten números";
		return false;
    } else {
        error.textContent = "";
		return true;
	}
}


function validateUsername(inputId, errorId) {
	const usernameInput = document.getElementById(inputId);
	const usernameError = document.getElementById(errorId);
	const pattern = /^[A-Za-z0-9_]+$/;

	if (usernameInput.value.length < 4) {
		usernameError.textContent = "El nombre de usuario debe tener por lo menos 4 caracteres.";
	}

	if (!pattern.test(usernameInput.value)) {
		// Display an error message
		usernameError.textContent = "Nombre de usuario inválido. Solo letras, números y '_'";
		return false; // Return false to prevent form submission
	} else {
		// Clear the error message
		usernameError.textContent = "";
		return true; // Return true to allow form submission
	}
}

function validatePassword(inputId, errorId) {
	const passwordInput = document.getElementById(inputId);
	const passwordError = document.getElementById(errorId);
	const password = passwordInput.value;

	if (password.length < 6) {
		passwordError.textContent = "La contraseña debe tener por lo menos 6 caracteres.";
		return false;
	}

	if (!/\d/.test(password)) {
		passwordError.textContent = "La contraseña debe contener por lo menos un número";
		return false;
	}

	if (!/[A-Z]/.test(password)) {
		passwordError.textContent = "La contraseña debe contener por lo menos una mayúscula";
		return false;
	}
	else{
		passwordError.textContent = "";
		return true
	}

	
}

function validateDireccion(inputId, errorId) {
    const input = document.getElementById(inputId);
    const error = document.getElementById(errorId);
    const pattern = /^[a-zA-Z\s.,-]*\d+[a-zA-Z0-9\s.,-]*$/; // Pattern to require at least one number

    if (!pattern.test(input.value)) {
        error.textContent = "La dirección debe contener al menos un número y puede incluir letras, números y signos de puntuación comunes";
		return false
	} else {
        error.textContent = "";
		return true
    }
}

function validatePhoneNumber(inputId, errorId) {
	const phoneNumberInput = document.getElementById(inputId);
	const phoneNumberError = document.getElementById(errorId);
	const phoneNumberValue = phoneNumberInput.value.trim();

	// Check if the phone number consists of digits and is a certain length
	const phoneNumberPattern = /^\d{9,15}$/; // Change the length requirement as needed

	if (!phoneNumberPattern.test(phoneNumberValue)) {
		phoneNumberError.textContent = "Por favor ingrese un número de teléfono válido";
		return false; // Prevent form submission
	} else {
		phoneNumberError.textContent = "";
		return true; // Allow form submission
	}
}