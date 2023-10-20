document.addEventListener("DOMContentLoaded", () => {
	const inputInstitutionSelect = document.getElementById("inputInstitution");
	const inputRoleSelect = document.getElementById("inputRole");
	const addRoleButton = document.getElementById("addRoleButton");

	// Initialize the button state
	updateButtonState();

	// Function to update the button state
	function updateButtonState() {
		if (inputInstitutionSelect.value !== "" && inputRoleSelect.value !== "") {
			addRoleButton.disabled = false;
		} else {
			addRoleButton.disabled = true;
		}
	}

	// Event listeners for select elements
	inputInstitutionSelect.addEventListener("change", updateButtonState);
	inputRoleSelect.addEventListener("change", updateButtonState);
});

function deleteRole(button) {
	let modal = document.getElementById("role_delete");
	const data = JSON.parse(button.getAttribute("data-element").replace(/'/g, '"')); // Parse the JSON data

	modal.querySelector("#role_id").value = data.id_role;
	modal.querySelector("#institution_id").value = data.id_institution;

	openModal(modal);
}
