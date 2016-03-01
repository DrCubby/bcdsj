function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getFragment(url,theForm,theID) {
    /*
       get/post django fragment request
       url: the django response url
       theForm: the form data being sent.  supports file uploads using FormData
       theID:  the idea (if any) of the get object being requested
     */
    var method = theForm == 'token'? 'GET':'POST';
    var csrftoken = $('#token').find("input[name='csrfmiddlewaretoken']").val()
    var formData = new FormData(document.getElementById(theForm));

    // setup ajax by submitting csrf token if required
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // clear the retainer
    // go get it
    $('#content-fragment').html('');
    $.ajax({
        url: url,
        type: method,
        data: formData,
        processData: false,
        contentType: false,
        success: function (data, textStatus, jqXHR) {
            $('#content-fragment').html(data);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log('ERROR: ' + errorThrown);
        }
    });
}

function menuSwitch(menu) {
    $('.pure-menu-item').removeClass('pure-menu-selected');
    $('#menu' + menu).addClass('pure-menu-selected');
}
