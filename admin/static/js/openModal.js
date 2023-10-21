/**
 * Opens a modal and returns a promise that resolves to a boolean value.
 *
 * @return {Promise<boolean>} A promise that resolves to `true` if the "Confirm" button is clicked, and `false` if the "Cancel" button is clicked.
 */
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

/**
 * Clears the form inside a modal.
 *
 * @param {HTMLElement} modal - The modal element containing the form.
 */
function clearForm(modal) {
	const form = modal.querySelector("form");
	if (form) {
		form.reset();
	}
}
