/**
 * Retrieves institution information and displays it in a modal.
 *
 * @param {HTMLElement} button - The button element that triggers the function.
 * @return {void} This function does not return a value.
 */
var map;

function viewInstitution(button) {
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"'));

	const modal = document.getElementById("institution_view");

	function setInnerHTML(elementId, value) {
		const element = modal.querySelector(elementId);
		element.innerHTML = value === undefined || value === null || value === "" ? "No hay datos ingresados" : value;
	}

	setInnerHTML("#institution-name", data.name);
	setInnerHTML("#institution-info", data.info);
	setInnerHTML("#institution-address", data.address);
	setInnerHTML("#institution-location", data.location);
	setInnerHTML("#institution-website", data.website);
	setInnerHTML("#institution-keywords", data.search_keywords);
	setInnerHTML("#institution-days-hours", data.days_and_hours);
	setInnerHTML("#institution-contact", data.contact_info);

	if (data.enabled === "True") {
		modal.querySelector("#institution-state").innerHTML = "Habilitada";
	} else {
		modal.querySelector("#institution-state").innerHTML = "Deshabilitada";
	}

	// Passing element to edit button
	const editButton = modal.querySelector("#edit-button");
	editButton.setAttribute("data-element", JSON.stringify(data));
	editButton.setAttribute("data-url", button.getAttribute("data-url"));

	openModal(modal);
	if (data.coordinates) {
		document.getElementById("viewMapContainer").style.display = "block";

		document.addEventListener("DOMContentLoaded", loadMap(data.coordinates));
	} else {
		document.getElementById("viewMapContainer").style.display = "none";
	}
}

/**
 * Edit an institution based on the button clicked.
 *
 * @param {HTMLElement} button - The button element that was clicked.
 * @return {void} This function does not return a value.
 */
function editInstitution(button) {
	document.getElementById("institution_view").style.display = "none";
	let modal = document.getElementById("institution_edit");
	const data = JSON.parse(button.getAttribute("data-element"));
	let checkboxEnabled = document.querySelector("#inputEnabledEdit");
	const form = modal.querySelector("#edit-form");

	function setInputValue(inputId, value) {
		const input = modal.querySelector(inputId);
		input.value = value || ""; // Set value to an empty string if value is falsy
	}

	setInputValue("#inputNameEdit", data.name);
	setInputValue("#inputInfoEdit", data.info);
	setInputValue("#inputAddressEdit", data.address);
	setInputValue("#inputLocationEdit", data.location);
	setInputValue("#inputWebsiteEdit", data.website);
	setInputValue("#inputKeywordsEdit", data.search_keywords);
	setInputValue("#inputDaysHoursEdit", data.days_and_hours);
	setInputValue("#inputContactEdit", data.contact_info);

	if (data.enabled.toLowerCase() === "true") {
		checkboxEnabled.checked = true;
	}

	form.action = button.getAttribute("data-url");

	openModal(modal);
	document.addEventListener("DOMContentLoaded", viewEditMap(data.coordinates));
}

/**
 * Deletes an institution.
 *
 * @param {Element} button - The button element that triggered the delete action.
 * @return {undefined} This function does not return a value.
 */
function deleteInstitution(button) {
	let modal = document.getElementById("institution_delete");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data
	modal.querySelector("#institution_id").value = data.id;
	openModal(modal);
}

/**
 * Adds an institution by opening a modal window.
 *
 * @param {HTMLElement} modal - The HTML element representing the modal window.
 */
function addInstitution() {
	let modal = document.getElementById("institution_add");
	openModal(modal);
}
