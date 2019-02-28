var WildRydes = window.WildRydes || {};

(function scopeWrapper($) {
    function register(email, onSuccess, onFailure) {
        var dataEmail = {
            Name: 'email',
            Value: email
        };
    }

    $(function onDocReady() {
        $('#registrationForm').submit(handleRegister);
    });

    function handleRegister(event) {
        var email = $('#emailInputRegister').val();
        window.location.href = "http://hatters.hubofallthings.com/signup/partner?application_id=maven&email=" + email + "&redirect_url=http://markandmaven.com.s3-website.eu-west-2.amazonaws.com/verify.html";
        var onFailure = function registerFailure(err) {
            alert(err);
        };
        event.preventDefault();
    }
}(jQuery));
