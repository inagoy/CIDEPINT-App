/**
 * Opens a modal and returns a promise that resolves to a boolean value.
 *
 * @return {Promise<boolean>} A promise that resolves to `true` if the "Confirm" button is clicked, and `false` if the "Cancel" button is clicked.
 */
function openModal(modal_id) {
	return new Promise((resolve) => {
		const confirmationModal = document.getElementById(modal_id);
		confirmationModal.style.display = "block";

		const confirmButton = confirmationModal.querySelector(".confirm-button");
		const cancelButton = confirmationModal.querySelector(".close-button");

		// Add event listener to the "Confirm" button
		if (confirmButton) {
			confirmButton.addEventListener("click", () => {
				confirmationModal.style.display = "none";
				resolve(true); // Resolve the promise with true
			});
		}

		// Add event listener to the "Cancel" button
		cancelButton.addEventListener("click", () => {
			confirmationModal.style.display = "none";
			resolve(false); // Resolve the promise with false
		});
	});
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

function deleteUser() {
	openModal("confirm_modal");
}

function viewUser() {
	openModal("user_view");
}

function editUser() {
	openModal("user_edit");
}
