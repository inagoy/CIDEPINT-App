/**
 * Validates the input for items per page.
 *
 * @returns {boolean} true if the input is valid, false otherwise.
 */
function validateItemsPerPage() {
	const itemsPerPageInput = document.getElementById("inputItemsPage");
	const itemsPerPageError = document.getElementById("pageError");
	const itemsPerPageValue = itemsPerPageInput.value.trim();
	const itemsPerPage = parseInt(itemsPerPageValue);

	if (itemsPerPageValue === "") {
		itemsPerPageError.textContent = "Debe ingresar un número entero válido.";
		return false;
	}

	return true;
}

/**
 * Validates the selected mode.
 *
 * @return {boolean} Returns true if a mode is selected, false otherwise.
 */
function validateMode() {
	var modeSelect = document.getElementById("selectMode");
	var modeError = document.getElementById("modeError");
	var selectedMode = modeSelect.value;

	if (selectedMode === "") {
		modeError.textContent = "Debe seleccionar un modo.";
		return false;
	} else {
		modeError.textContent = "";
		return true;
	}
}

/**
 * Validates the message input field.
 *
 * @return {boolean} Returns true if the message is not empty, false otherwise.
 */
function validateMessage() {
	var messageTextarea = document.getElementById("inputMessage");
	var messageError = document.getElementById("messageError");
	var message = messageTextarea.value.trim();

	if (message === "") {
		messageError.textContent = "Este campo es obligatorio.";
		return false;
	} else {
		messageError.textContent = "";
		return true;
	}
}

/**
 * Validates the contact input field.
 *
 * @return {boolean} Returns true if the contact input is valid, false otherwise.
 */
function validateContact() {
	var contactInput = document.getElementById("inputContact");
	var contactError = document.getElementById("contactError");
	var contact = contactInput.value.trim();

	if (contact === "") {
		contactError.textContent = "Este campo es obligatorio.";
		return false;
	} else if (contact.length > 255) {
		contactError.textContent = "La longitud del mensaje no puede exceder los 255 caracteres.";
		return false;
	} else {
		contactError.textContent = "";
		return true;
	}
}

/**
 * Validates the form by calling individual validation functions for each form field.
 *
 * @return {boolean} Returns true if all form fields are valid, otherwise false.
 */
function validateForm() {
	const isItemsPerPageValid = validateItemsPerPage();
	const isModeValid = validateMode();
	const isMessageValid = validateMessage();
	const isContactValid = validateContact();

	return isItemsPerPageValid && isModeValid && isMessageValid && isContactValid;
}
