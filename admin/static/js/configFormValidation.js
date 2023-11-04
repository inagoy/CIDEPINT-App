/**
 * Validates the input for items per page.
 *
 * @param {string} inputId - The ID of the inuput element.
 * @param {string} errorId - The ID of the error element.
 * @returns {boolean} true if the input is valid, false otherwise.
 */
function validateItemsPerPage(inputId, errorId) {
	const itemsPerPageInput = document.getElementById(inputId);
	const itemsPerPageError = document.getElementById(errorId);
	const itemsPerPageValue = itemsPerPageInput.value.trim();
	const itemsPerPage = parseInt(itemsPerPageValue);
	let pattern = /^\d+$/;
	if (itemsPerPageValue === "" || isNaN(itemsPerPage) || !pattern.test(itemsPerPageValue)) {
		itemsPerPageError.textContent = "Debe ingresar un número entero válido.";
		return false;
	} else {
        itemsPerPageError.textContent = ""; // Clear the error message when the input is valid
        return true;
    }

}

/**
 * Validates the selected mode.
 *
 * @param {string} selectId - The ID of the select element.
 * @param {string} errorId - The ID of the error element.
 * @return {boolean} Returns true if a mode is selected, false otherwise.
 */
function validateMode(selectId, errorId) {
	var modeSelect = document.getElementById(selectId);
	var modeError = document.getElementById(errorId);
	var selectedMode = modeSelect.value;

	if (selectedMode === "" || (selectedMode != "True" && selectedMode != "False")) {
		modeError.textContent = "Debe seleccionar un modo válido";
		return false;
	} else {
		modeError.textContent = "";
		return true;
	}
}

/**
 * Validates the message input field.
 *
 * @param {string} inputId - The ID of the inuput element.
 * @param {string} errorId - The ID of the error element.
 * @return {boolean} Returns true if the message is not empty, false otherwise.
 */
function validateMessage(inputId, errorId) {
	var messageTextarea = document.getElementById(inputId);
	var messageError = document.getElementById(errorId);
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
 * @param {string} inputId - The ID of the inuput element.
 * @param {string} errorId - The ID of the error element.
 * @return {boolean} Returns true if the contact input is valid, false otherwise.
 */
function validateContact(inputId, errorId) {
	var contactInput = document.getElementById(inputId);
	var contactError = document.getElementById(errorId);
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
    const isItemsPerPageValid = validateItemsPerPage('inputItemsPage', 'pageError');
    const isModeValid = validateMode('selectMode', 'modeError');
    const isMessageValid = validateMessage('inputMessage', 'messageError');
    const isContactValid = validateContact('inputContact', 'contactError');

    return isItemsPerPageValid && isModeValid && isMessageValid && isContactValid;
}


/**
 * Confirmation message when the edit button is clicked.
 *
 * @return {void} This function does not return a value.
 */
function confirmEdit() {
    if (validateForm()) {
        let modal = document.getElementById("configuration_confirm");
        openModal(modal);
    }
}


/**
 * Edition form submission.
 * @return {void} This function does not return a value.
 */
function confirmAndSubmit() {
   	document.querySelector('form').submit();
}
