/**
 * Retrieves institution information and displays it in a modal.
 *
 * @param {HTMLElement} button - The button element that triggers the function.
 * @return {void} This function does not return a value.
 */function viewInstitution(button) {
    const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"'));
    const modal = document.getElementById("institution_view");

    function setInnerHTML(elementId, value) {
        const element = modal.querySelector(elementId);
        element.innerHTML = value === undefined ? "No hay datos ingresados" : value;
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

    openModal(modal);
}

function editInstitution(button) {
    let modal = document.getElementById("institution_edit");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data
	let checkboxEnabled = document.querySelector("#inputEnabledEdit");
	const form = modal.querySelector("#edit-form");

	function setInputValue(inputId, value) {
        const input = modal.querySelector(inputId);
        input.value = value || ''; // Set value to an empty string if value is falsy
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

	form.action = button.getAttribute("data-url")
	
	openModal(modal);
}

function deleteInstitution(button) {
	let modal = document.getElementById("institution_delete");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data
	modal.querySelector("#institution_id").value = data.id;
	openModal(modal);
}

function addInstitution() {
	let modal = document.getElementById("institution_add");
	openModal(modal);
}
