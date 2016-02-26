function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getFragment(url,theForm,theID) {
    var method = 'POST';
    // If we're loading just an empty form change method to GET
    if(theForm == 'token') { method = 'GET'; } else { method = 'POST'; }
    if(theID != undefined) {
        document.getElementById('pk').value = theID;
        method = 'GET';
    }

    //var csrftoken = $.cookie('csrftoken');
    //var csrftoken = getCookie('csrftoken');
    var csrftoken = $('#token').find("input[name='csrfmiddlewaretoken']").val()

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var fd = new FormData(document.getElementById(theForm));
    //$('#content-fragment').html('');
    $.ajax({
        url: url,
        type: method,
        data: fd,
        processData: false,
        contentType: false,
        success: function (data, textStatus, jqXHR) {
            $('#content-fragment').html(data);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            //alert('ERROR: ' + errorThrown);
        }
    });
}