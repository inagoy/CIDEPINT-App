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
	} else {
		emailError.textContent = "";
	}
}

function validateJustText(inputId, errorId) {
	const input = document.getElementById(inputId);
	const error = document.getElementById(errorId);
	const pattern = /^[\p{L}\s´]+$/u;

	if (!pattern.test(input.value)) {
		error.textContent = "Solo se permiten letras y espacios";
	} else {
		error.textContent = "";
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
		usernameError.textContent = "Nombre de usuario inválido. Solo letras, números y _";
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
		return;
	}

	if (!/\d/.test(password)) {
		passwordError.textContent = "La contraseña debe contener por lo menos un número";
		return;
	}

	if (!/[A-Z]/.test(password)) {
		passwordError.textContent = "La contraseña debe contener por lo menos una mayúscula";
		return;
	}

	passwordError.textContent = "";
}
