var step_0 = true
var step_1 = true
var step_2 = true
var step_3 = true
var step_4 = true


$('#next_btn').click(function(e) {
    e.preventDefault();
    step_val =$(this).data('step');
     if (step_val + 1 == 5){
          console.log('asdsad');
     //  $('#next_img').css('opacity','.5');

    }
if (step_val != 5) {
    console.log('step val=', step_val);
    $('#step-' + $(this).data('step')).css('display', 'none');
    $(this).data('step', parseInt($(this).data('step')) + 1);
    console.log($(this).data('step'));
    $('#step-' + $(this).data('step')).css('display', 'block');
 //   $('#prev_img').css('opacity', '1');

}
  });


$('#prev_btn').click(function(e) {
    step_val = parseInt($('#next_btn').data('step'));
    console.log('step val=', step_val);
    e.preventDefault();

    if (step_val - 1 > 0 ) {
        console.log('none step-=', step_val);
        // $('#step-' + step_val).css('display','none');
        document.getElementById('step-' + $('#next_btn').data('step')).style.display='none';

    $('#next_btn').data('step', step_val - 1);
        // $('#step-' + step_val-1).css('display','block');
         document.getElementById('step-' + $('#next_btn').data('step')).style.display='block';

        console.log('block step-=', step_val - 1);
        console.log($('#next_btn').data('step'));
    //     $('#next_img').css('opacity','1');

    }
    else{
        $('#next_btn').data('step',0);
     //   $('#prev_img').css('opacity','.5');
        $('#step-0').css('display','block');
        $('#step-1').css('display','none');

    }


  });

$('.step-0').click(function () {
    if (step_0){
        discount = parseInt($('#discount').html());
    $('#discount').html(discount + 2);
    step_0 = false;
    }


})

$('.step-1').click(function () {
    if (step_1){
        discount = parseInt($('#discount').html());
    $('#discount').html(discount + 2);
    step_1 = false;
    }


})

$('.step-3').click(function () {
    if (step_3){
        discount = parseInt($('#discount').html());
    $('#discount').html(discount + 2);
    step_3 = false;
    }


})

$('#site-name').on('input', function  () {
    if (step_2){
        discount = parseInt($('#discount').html());
    $('#discount').html(discount + 2);
    step_2 = false;
    }


})
$('#work-with').on('input', function  () {
    if (step_4){
        discount = parseInt($('#discount').html());
    $('#discount').html(discount + 2);
    step_4 = false;
    }


})

$('#quiz-complete').click(function (e) {
  e.preventDefault();
  step0 = $("#step-0").find("input[name=radio]:checked").attr('value');
  step1 = $("#step-1").find("input[name=radio]:checked").attr('value');
  step2 = $("#step-2").find("input").val();
  step3 = $("#step-3").find("input[name=radio]:checked").attr('value');
  step4 = $("#step-4").find("input").val();
  csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  console.log(step0,step1,step2,step3,step4);



        $.ajax({
            type:"POST",
            url:'/user/quiz/',
            data:{
                'csrfmiddlewaretoken': csrfmiddlewaretoken,
                'step0':step0,
                'step1':step1,
                'step2':step2,
                'step3':step3,
                'step4':step4,
            },
            success : function(data){
                console.log(data);

            }
        });

})


//$("#step-0-form").find("input[name=radio]:checked").attr('value');