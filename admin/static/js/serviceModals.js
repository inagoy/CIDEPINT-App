/**
 * Retrieves user information and displays it in a modal.
 *
 * @param {HTMLElement} button - The button element that triggers the function.
 * @return {void} This function does not return a value.
 */
function viewService(button) {
	let modal = document.getElementById("service_view");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data


	modal.querySelector("#service-name").innerHTML = data.name;
	modal.querySelector("#service-description").innerHTML = data.description;
	modal.querySelector("#service-keywords").innerHTML = data.keywords;
	modal.querySelector("#service-type").innerHTML = data.service_type;    
	
	if (data.enabled === "True") {
        modal.querySelector("#service-enabled").innerHTML = "Habilitado";
    } else {
        modal.querySelector("#service-enabled").innerHTML = "Deshabilitado";
    }


    const editButton = modal.querySelector("#edit-button");
	if (editButton !== null) {
		editButton.setAttribute('data-element', JSON.stringify(data));
		editButton.setAttribute('data-url', button.getAttribute("data-url")); 
	}
	openModal(modal);
}

/**
 * Adds a service by opening a modal.
 *
 * @param {type} paramName - description of parameter
 * @return {type} description of return value
 */
function addService() {
	let modal = document.getElementById("service_add");
	openModal(modal);
}

/**
 * Deletes a service.
 *
 * @param {HTMLElement} button - The button element that triggered the delete.
 * @return {void} This function does not return a value.
 */
function deleteService(button) {
	let modal = document.getElementById("service_delete");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data


	modal.querySelector("#service-id").value = data.id;
	openModal(modal);
}

function editService(button) {
	document.getElementById("service_view").style.display = "none";
	let modal = document.getElementById("service_edit");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data


	modal.querySelector("#inputName").value = data.name;
	modal.querySelector("#inputDescription").value = data.description;
	modal.querySelector("#inputEditKeywords").value = data.keywords;

	const selectDocument = document.querySelector("#inputServiceType2");

	// ARREGLAR ESTO
	for (let i = 0; i < selectDocument.options.length; i++) {
		const option = selectDocument.options[i];
		const valor = option.value.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
		if (valor == data.service_type) {
			option.selected = true;
			break;
		}
	}

	const checkboxActive = document.querySelector("#inputEnabled2");
	checkboxActive.checked = data.enabled == "True" ? true : false;
	
	const form = modal.querySelector("#edit-form");
	form.action = button.getAttribute("data-url")


	openModal(modal);
}
