var step_0 = true
var step_1 = true

$('#next_btn').click(function(e) {
    e.preventDefault();
    step_val =$(this).data('step');
     console.log('step val=', step_val);
    $('.step-'+$(this).data('step')).css('display','none');
    $(this).data('step',parseInt($(this).data('step')) + 1);
    console.log($(this).data('step'));
    $('.step-'+$(this).data('step')).css('display','block');
    $('#prev_img').css('opacity','1');
  });


$('#prev_btn').click(function(e) {
    step_val = parseInt($('#next_btn').data('step'));
    console.log('step val=', step_val);
    e.preventDefault();
    if (step_val - 1 > 0 ) {
        $('.step-'+$(this).data('step')).css('display','none');
        $('#next_btn').data('step', step_val - 1);
        $('.step-'+$(this).data('step')).css('display','block');
        console.log($('#next_btn').data('step'));

    }
    else{
        $('#next_btn').data('step',0);
        $('#prev_img').css('opacity','.5');
        $('.step-0').css('display','block');
        $('.step-1').css('display','none');
    }


  });

$('.step-0').click(function () {
    console.log(step_0);
    if (step_0){
        discount = parseInt($('#discount').html());
    $('#discount').html(discount + 2);
    step_0 = false;
    }


})

$('.step-1').click(function () {
    console.log(step_0);
    if (step_1){
        discount = parseInt($('#discount').html());
    $('#discount').html(discount + 2);
    step_1 = false;
    }


})


//$("#step-0-form").find("input[name=radio]:checked").attr('value');