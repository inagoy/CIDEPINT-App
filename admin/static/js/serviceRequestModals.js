/**
 * Retrieves user information and displays it in a modal.
 *
 * @param {HTMLElement} button - The button element that triggers the function.
 * @return {void} This function does not return a value.
 */
function viewServiceRequest(button) {
	let modal = document.getElementById("request_view");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data

	modal.querySelector("#request-title").innerHTML = data.title;
	modal.querySelector("#request-description").innerHTML = data.description;
	modal.querySelector("#request-observations").innerHTML = data.observations;
	modal.querySelector("#request-status").innerHTML = data.status;
	modal.querySelector("#request-service").innerHTML = data.service;
	modal.querySelector("#request-requester").innerHTML = data.requester;

	openModal(modal);
}

function deleteServiceRequest(button) {
	let modal = document.getElementById("request_delete");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data

	modal.querySelector("#request_id").value = data.id;
	openModal(modal);
}

function changeStatusServiceRequest(button) {
	let modal = document.getElementById("request_edit");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); 

	modal.querySelector("#inputObservations").value = data.observations;
	const selectDocument = document.querySelector("#inputStatus");

	for (let i = 0; i < selectDocument.options.length; i++) {
		const option = selectDocument.options[i];
		if (option.value == data.status) {
			option.selected = true; // Select the matching option
			break; // Exit the loop once found
		}
	}

	for (let i = 0; i < selectDocument.options.length; i++) {
		const option = selectDocument.options[i];
		const valor = option.value.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
		if (valor == data.status) {
			option.selected = true;
			break;
		}
	}
	console.log(button.getAttribute("data-url"))
	const form = modal.querySelector("#edit-form");
	form.action = button.getAttribute("data-url")


	
	openModal(modal);
}
