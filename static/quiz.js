
$(document).ready(() => {
  local_time = localStorage.getItem("time_left");

  if(local_time == "" || local_time == null ) {
  local_time = 10;
  localStorage.setItem("time_left", local_time);
  }
   $('#time').html(localStorage.getItem("time_left")+":" + 00);
   startTimer();
});

function startTimer() {
  var presentTime = document.getElementById('time').innerHTML;
  var timeArray = presentTime.split(/[:]+/);
  var m = timeArray[0];
  var s = checkSecond((timeArray[1] - 1));
  if(s==59) { m=m-1 }
  if(m < 0) {
    window.location.href = "/test-result";
  }

  document.getElementById('time').innerHTML =
    m + ":" + s;
   localStorage.setItem("time_left", m + ":" + s);
  setTimeout(startTimer, 1000);
}

function checkSecond(sec) {
  if (sec < 10 && sec >= 0) {sec = "0" + sec}; // add zero in front of numbers < 10
  if (sec < 0) {sec = "59"};
  return sec;
}

function checkans(val, id, option_no)
{
   if(localStorage.getItem("question"+id) !="" && !localStorage.getItem("question"+id))
   {
        $.ajax({
         url: '/checkans',
         dataType: 'json',
         method: 'POST',
         headers: {
                    "X-CSRFToken": '{{csrf_token }}'
                },
          data: {option_no: option_no, opt: val, q: id},
          success:(res) => {
               if(res.c == 1)
               {
                    $('#ans_'+id).attr({ 'class':'alert alert-success'});
                    $('#ans_'+id).html("Correct Answer: "+res.c_option);
                    $('#ans_'+id).show();
               }
               else
               {
                    $('#ans_'+id).attr({ 'class':'alert alert-danger'});
                    $('#ans_'+id).html("Your Answer: "+option_no+". "+val+"<br /> Correct Answer is: "+res.c_option);
                    $('#ans_'+id).show();
               }

               localStorage.setItem("question"+id, id);
          }
       });
   } else {
   alert("Your answer already recorded");
   }
}

 function endTest()
 {
    var ack = confirm("Are you sure to submit this test");
    if(ack)
    {
        window.location.href = "/test-result";

    }
 }