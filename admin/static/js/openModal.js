/**
 * Opens a modal and returns a promise that resolves to a boolean value.
 *
 * @return {Promise<boolean>} A promise that resolves to `true` if the "Confirm" button is clicked, and `false` if the "Cancel" button is clicked.
 */
function openModal(modal_id) {
	const confirmationModal = document.getElementById(modal_id);
	confirmationModal.style.display = "block";

	const confirmButton = confirmationModal.querySelector(".confirm-button");
	const cancelButton = confirmationModal.querySelector(".close-button");

	// Add event listener to the "Confirm" button
	if (confirmButton) {
		confirmButton.addEventListener("click", () => {
			confirmationModal.style.display = "none";
		});
	}

	// Add event listener to the "Cancel" button
	cancelButton.addEventListener("click", () => {
		confirmationModal.style.display = "none";
	});
}

function openModal(modal) {
	modal.style.display = "block";

	const confirmButton = modal.querySelector(".confirm-button");
	const cancelButton = modal.querySelector(".close-button");

	// Add event listener to the "Confirm" button
	if (confirmButton) {
		confirmButton.addEventListener("click", () => {
			clearForm(modal);
			modal.style.display = "none";
		});
	}

	// Add event listener to the "Cancel" button
	cancelButton.addEventListener("click", () => {
		clearForm(modal);
		modal.style.display = "none";
	});
}

function clearForm(modal) {
	const form = modal.querySelector("form");
	if (form) {
		form.reset();
	}
}
function viewInstitution() {
	openModal("institution_view");
}

function editInstitution() {
	openModal("institution_edit");
}

function deleteInstitution() {
	openModal("confirm_modal");
}
