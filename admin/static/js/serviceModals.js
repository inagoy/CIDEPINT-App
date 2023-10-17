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

function addService() {
	let modal = document.getElementById("service_add");
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

function editService(button) {
	let modal = document.getElementById("service_edit");
	console.log(button.getAttribute("data-element"));
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data
	console.log("la data: ", data);

	modal.querySelector("#inputName").value = data.name;
	modal.querySelector("#inputDescription").value = data.description;
	modal.querySelector("#inputKeywords").value = data.keywords;
	modal.querySelector("#service-id").value = data.id;
	console.log("service-id", modal.querySelector("#service-id").value, data.id);

	const selectDocument = document.querySelector("#inputServiceType2");

	// ARREGLAR ESTO
	for (let i = 0; i < selectDocument.options.length; i++) {
		const option = selectDocument.options[i];
		const valor = option.value.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
		if (valor == data.service_type) {
			option.selected = true;
			console.log(option, valor, data.service_type, "aaaaaaaaaaaaaaaA");
			break;
		}
	}

	const checkboxActive = document.querySelector("#inputEnabled2");
	checkboxActive.checked = data.enabled == "True" ? true : false;
	console.log("data.enabled", checkboxActive.checked, data.enabled);

	openModal(modal);
}
