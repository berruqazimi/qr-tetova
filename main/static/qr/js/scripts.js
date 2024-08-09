function replaceSpacesWithUnderscores() {
    var inputField = document.getElementById('textInput');
    inputField.value = inputField.value.replace(/\s+/g, '_');
}