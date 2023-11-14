/**
 * Retrieves user information and displays it in a modal.
 *
 * @param {HTMLElement} button - The button element that triggers the function.
 * @return {void} This function does not return a value.
 */
function viewUser(button) {
	let modal = document.getElementById("user_view");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data

	modal.querySelector("#user-first-name").innerHTML = data.first_name;
	modal.querySelector("#user-last-name").innerHTML = data.last_name;
	modal.querySelector("#user-email").innerHTML = data.email;
	if (data.active === "True"){
		modal.querySelector("#user-active").innerHTML = "Activo";
	} else {
		modal.querySelector("#user-active").innerHTML = "Inactivo";
	}

	function setInnerHTML(elementId, value) {
        const element = modal.querySelector(elementId);
        element.innerHTML = value === undefined || value === null || value === "" ? "No hay datos ingresados" : value;
    }

	setInnerHTML("#user-username", data.username);
	setInnerHTML("#user-phone", data.phone);
	setInnerHTML("#user-address", data.address);
	setInnerHTML("#user-gender", data.gender);
	setInnerHTML("#user-dni", data.document);

	
    const editButton = modal.querySelector("#edit-button");
    editButton.setAttribute('data-element', JSON.stringify(data));
    editButton.setAttribute('data-url', button.getAttribute("data-url")); 
	openModal(modal);
}

/**
 * Edits the user information based on the data provided by the button element.
 *
 * @param {Element} button - The button element that triggered the edit action.
 * @return {void} This function does not return anything.
 */
function editUser(button) {
	document.getElementById("user_view").style.display = "none";
	let modal = document.getElementById("user_edit");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data

	modal.querySelector("#inputEmail").value = data.email;
	modal.querySelector("#inputName").value = data.first_name;
	modal.querySelector("#inputSurname").value = data.last_name;
	modal.querySelector("#inputUsername").value = data.username;
	modal.querySelector("#inputAddress").value = data.address;
	modal.querySelector("#inputPhoneNumber").value = data.phone;
	modal.querySelector("#inputDocument").value = data.document;

	const selectDocument = document.querySelector("#inputDocumentType");

	// Loop through the options to find the one that matches data.documentType
	for (let i = 0; i < selectDocument.options.length; i++) {
		const option = selectDocument.options[i];
		if (option.value == data.document_type) {
			option.selected = true; // Select the matching option
			break; // Exit the loop once found
		}
	}

	const selectGender = document.querySelector("#inputGender");

	// Loop through the options to find the one that matches data.documentType
	for (let i = 0; i < selectGender.options.length; i++) {
		const option = selectGender.options[i];
		if (option.value == data.gender) {
			option.selected = true; // Select the matching option
			break; // Exit the loop once found
		}
	}

	const checkboxActive = document.querySelector("#inputActive");

	checkboxActive.checked = data.active == "True" ? true : false;

	const form = modal.querySelector("#edit-form");
	form.action = button.getAttribute("data-url")


	openModal(modal);
}

/**
 * Deletes a user.
 *
 * @param {Element} button - The button element that triggered the delete action.
 * @return {undefined} This function does not return a value.
 */
function deleteUser(button) {
	let modal = document.getElementById("user_delete");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data

	modal.querySelector("#user-id").value = data.id;
	openModal(modal);
}

/**
 * Adds a user by opening a modal.
 *
 * @param {type} paramName - description of parameter
 * @return {type} description of return value
 */
function addUser() {
	let modal = document.getElementById("user_add");
	openModal(modal);
}

/**
 * Opens the user roles modal when a button is clicked.
 *
 * @param {Element} button - The button element that triggers the modal.
 * @return {undefined} This function does not return a value.
 */
function userRoles(button) {
	let modal = document.getElementById("user_roles");

	openModal(modal);
}