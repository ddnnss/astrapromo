function getCaseInfo(c_id) {
    console.log(c_id);
    caseId = c_id;
    csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        $.ajax({
            type:"POST",
            url:'/caseinfo/',
            dataType: "json",
            data:{
                'csrfmiddlewaretoken': csrfmiddlewaretoken,
                'caseId':caseId,
            },
            success : function(data){
                console.log(data);
                $('.modal-title').html(data.caseName);
                $('#caseInfo').html(data.caseInfo);
                $('#caseImg').attr('src',data.caseImg)
                $('#showCase').modal('show');

            }
        });

}