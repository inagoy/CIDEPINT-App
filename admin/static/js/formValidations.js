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

/**
 * Validates if the input value contains only letters and spaces.
 *
 * @param {string} inputId - The ID of the input element.
 * @param {string} errorId - The ID of the error element.
 * @return {void} This function does not return anything.
 */
function validateJustText(inputId, errorId) {
	
	const input = document.getElementById(inputId);
	const error = document.getElementById(errorId);
	const pattern = /^[A-Za-z\s]+$/;

	if (!pattern.test(input.value)) {
		error.textContent = "Solo se permiten letras y espacios";
		return false;
	} else {
		error.textContent = "";
		return true;
	}
}

/**
 * Validates if the input value contains only numbers.
 *
 * @param {string} inputId - The id of the input element.
 * @param {string} errorId - The id of the error element.
 * @returns {boolean} Returns true if the input value contains only numbers, otherwise false.
 */
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


/**
 * Validates the username input and displays an error message if the input is
 * invalid. Returns true if the input is valid and false otherwise.
 *
 * @param {string} inputId - The id of the username input element.
 * @param {string} errorId - The id of the element where the error message will be displayed.
 * @return {boolean} - True if the username is valid, false otherwise.
 */
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

/**
 * Validates a password input and displays an error message if the password does not meet the criteria.
 *
 * @param {string} inputId - The ID of the password input element.
 * @param {string} errorId - The ID of the error message element.
 */
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

/**
 * Validates the direccion input field by checking if it contains at least one number
 *
 * @param {string} inputId - the id of the direccion input field
 * @param {string} errorId - the id of the error element to display the error message
 * @return {boolean} true if the direccion is valid, false otherwise
 */
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

/**
 * Validates a phone number input and displays an error message if the phone number is not valid.
 *
 * @param {string} inputId - The ID of the phone number input element.
 * @param {string} errorId - The ID of the error message element.
 * @return {boolean} Returns true if the phone number is valid and allows form submission. Returns false if the phone number is not valid and prevents form submission.
 */
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