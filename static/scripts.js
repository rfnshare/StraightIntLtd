// Checkbox selete all work in customer list
function toggle(source) {
    checkboxes = document.getElementsByName('foo');
    for (var i = 0, n = checkboxes.length; i < n; i++) {
        checkboxes[i].checked = source.checked;
    }
}

function random(select) {
    var e = document.getElementById("ddlViewBy");
    var strUser = e.options[e.selectedIndex].text;
    alert(strUser)
}


$(document).ready(function () {
    var maxField = 10; //Input fields increment limitation
    var addButton = $('.add_button'); //Add button selector
    var wrapper = $('.field_wrapper'); //Input field wrapper
    var fieldHTML = '<div><input class="form-control" type="text" name="field_name[]" value=""/><a href="javascript:void(0);" class="remove_button"><i class="fas fa-minus-circle"></i> </a></div>'; //New input field html
    var x = 1; //Initial field counter is 1

    //Once add button is clicked
    $(addButton).click(function () {
        //Check maximum number of input fields
        if (x < maxField) {
            x++; //Increment field counter
            $(wrapper).append(fieldHTML); //Add field html
        }
    });

    //Once remove button is clicked
    $(wrapper).on('click', '.remove_button', function (e) {
        e.preventDefault();
        $(this).parent('div').remove(); //Remove field html
        x--; //Decrement field counter
    });
});
