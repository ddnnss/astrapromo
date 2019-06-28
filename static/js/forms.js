jQuery(function($){
    $("#callBackHome_phone").mask("+7 (999) 999-99-99");
});
jQuery(function($){
    $("#callBack_phone").mask("+7 (999) 999-99-99");
});
jQuery(function($){
    $("#step-4-phone").mask("+7 (999) 999-99-99");
});

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})
function modalCallback() {
    client_name = document.getElementById("callBack_name").value;
    client_phone = document.getElementById("callBack_phone").value;
    $('#modalSubmit').attr('disabled','disabled');
    $('#modalSubmit').html('Отправка...');
    $('.nameError').css('display','none');
    $('.phoneError').css('display','none');
    if (client_name == ''){
        $('#modalSubmit').html('ОТПРАВИТЬ');
        $('#modalSubmit').removeAttr('disabled');
        console.log('name empty');
        $('#callBackModal').removeClass('input-error');
        $('.nameError').css('display','block');
        setTimeout(function(){
            $('#callBackModal').addClass('input-error');
        },500);

        return;
    }
    if (client_phone == ''){
        $('#modalSubmit').html('ОТПРАВИТЬ');
        $('#modalSubmit').removeAttr('disabled');
        console.log('phone empty');
        $('#callBackModal').removeClass('input-error');
        $('.phoneError').css('display','block');
        setTimeout(function(){
            $('#callBackModal').addClass('input-error');
        },500);
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
            yaCounter25221497.reachGoal('yspex');
            yaCounter25221497.reachGoal('forma_prod_send');
            $('#modalSubmit').html('ОТПРАВИТЬ');
            $('#modalSubmit').removeAttr('disabled');
            $('#callBack_send').css('display','none');
            $('#callBack_done').css('display','block');
        }
    });
}

function callBack_home(e,t) {
    e.preventDefault();
    console.log(t);
    client_name = document.getElementById("callBackHome_name").value;
    client_phone = document.getElementById("callBackHome_phone").value;
    client_email = document.getElementById("callBackHome_email").value;
    $('#homeSubmit').attr('disabled','disabled');
    $('#homeSubmit').html('Отправка...');
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
            yaCounter25221497.reachGoal('yspex');
            if (t==='contact'){
                yaCounter25221497.reachGoal('zakaz_contacts');
            }
             if (t==='big_form'){
                yaCounter25221497.reachGoal('form_footer');
            }
            $('#callBackForm').css('display','none');
            $('#callBackHome_done').css('display','block');
        }
    });

}

