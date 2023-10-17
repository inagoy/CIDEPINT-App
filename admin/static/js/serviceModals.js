/**
 * Retrieves user information and displays it in a modal.
 *
 * @param {HTMLElement} button - The button element that triggers the function.
 * @return {void} This function does not return a value.
 */
function viewService(button) {
	let modal = document.getElementById("service_view");
	console.log(button.getAttribute("data-element"));
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data
	console.log("la data: ", data);

	modal.querySelector("#service-name").innerHTML = data.name;
	modal.querySelector("#service-description").innerHTML = data.description;
	modal.querySelector("#service-keywords").innerHTML = data.keywords;
	modal.querySelector("#service-type").innerHTML = data.service_type;
	modal.querySelector("#service-enabled").innerHTML = data.enabled;

	openModal(modal);
}

function deleteService(button) {
	let modal = document.getElementById("service_delete");
	console.log(button.getAttribute("data-element"));
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data
	console.log("la data: ", data.id);

	modal.querySelector("#service-id").value = data.id;
	openModal(modal);
}

/*
function editUser(button) {
	let modal = document.getElementById("user_edit");
	console.log(button.getAttribute("data-element"));
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data
	console.log("la data: ", data);

	modal.querySelector("#inputEmail").value = data.email;
	modal.querySelector("#inputName").value = data.first_name;
	modal.querySelector("#inputSurname").value = data.last_name;
	modal.querySelector("#inputUsername").value = data.username;
	modal.querySelector("#inputAddress").value = data.address;
	modal.querySelector("#inputPhoneNumber").value = data.phone;
	modal.querySelector("#inputDocument").value = data.document;
	modal.querySelector("#user-id").value = data.id;

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

	openModal(modal);
}

function deleteUser(button) {
	let modal = document.getElementById("user_delete");
	console.log(button.getAttribute("data-element"));
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data
	console.log("la data: ", data.id);

	modal.querySelector("#user-id").value = data.id;
	openModal(modal);
}

function addUser() {
	let modal = document.getElementById("user_add");
	openModal(modal);
}
*/
