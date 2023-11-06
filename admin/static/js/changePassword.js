/**
 * Validates that the new password and confirm password fields are completely filled.
 *
 * @return {void} This function does not return anything.
 */

function validateChangePassword() {
    const newPassword = document.getElementById('inputNewPassword');
    const newPasswordError = document.getElementById('newPasswordError');
    const confirmNewPassword = document.getElementById('inputConfirmPassword');
    const confirmNewPasswordError = document.getElementById('confirmPasswordError');

    let newPasswordNotEmpty = newPassword.value.trim().length > 0;
    let confirmPasswordNotEmpty = confirmNewPassword.value.trim().length > 0;

    const currentPassword = document.getElementById('inputCurrentPassword');
    if (currentPassword != null) {
        if (currentPassword.value.trim() == "") {
            currentPasswordError.textContent = "Este campo es obligatorio.";
            isNewPasswordValid = false;
        } else {
            currentPasswordError.textContent = "";
        }
    }

    if (!newPasswordNotEmpty) {
        newPasswordError.textContent = "Este campo es obligatorio.";
    }
    if (!confirmPasswordNotEmpty) {
        confirmNewPasswordError.textContent = "Este campo es obligatorio.";
    } else {
        confirmNewPasswordError.textContent = "";
    }

    let isValid = newPasswordNotEmpty && confirmPasswordNotEmpty;
    const button = document.querySelector("button[type=submit]");
    button.disabled = !isValid;
    return isValid;
}
