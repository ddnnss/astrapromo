function modalCallback() {
    client_name = document.getElementById("callBack_name").value;
    client_phone = document.getElementById("callBack_phone").value;
    $('#modalSubmit').addClass('is-loading');
    $('.nameError').css('display','none');
    $('.phoneError').css('display','none');
    if (client_name == ''){
        console.log('name empty');
        $('#modalSubmit').removeClass('is-loading');
        $('.nameError').css('display','block');

        return;
    }
     if (client_phone == ''){
        console.log('phone empty');
         $('#modalSubmit').removeClass('is-loading');
          $('.phoneError').css('display','block');
        return;
    }
    csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

        $.ajax({
            type:"POST",
            url:'/user/callback/',
            data:{
                'csrfmiddlewaretoken': csrfmiddlewaretoken,
                'client_name':client_name,
                'client_phone':client_phone,
            },
            success : function(data){
                console.log(data);
                $('#callBack_send').css('display','none');
                $('#callBack_done').css('display','block');
            }
        });
}

function callBack_home(e) {
    e.preventDefault();
    client_name = document.getElementById("callBackHome_name").value;
    client_phone = document.getElementById("callBackHome_phone").value;
    client_email = document.getElementById("callBackHome_email").value;
    $('#homeSubmit').addClass('is-loading');
    csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

        $.ajax({
            type:"POST",
            url:'/user/callback/',
            data:{
                'csrfmiddlewaretoken': csrfmiddlewaretoken,
                'client_name':client_name,
                'client_phone':client_phone,
                'client_email':client_email,
            },
            success : function(data){
                console.log(data);
                $('#callBackForm').css('display','none');
                $('#callBackHome_done').css('display','block');
            }
        });

}