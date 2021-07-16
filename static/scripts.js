// Checkbox selete all work in customer list
function toggle(source) {
    checkboxes = document.getElementsByName('foo');
    for (var i = 0, n = checkboxes.length; i < n; i++) {
        checkboxes[i].checked = source.checked;
    }
}

function random(select)
{
    var e = document.getElementById("ddlViewBy");
    var strUser = e.options[e.selectedIndex].text;
    alert(strUser)
}