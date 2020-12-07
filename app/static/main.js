

function toggle(source) {
    checkboxes = document.getElementsByName('checked_words');
    for (var checkbox in checkboxes) {
        checkbox.checked = source.checked;
    }
}