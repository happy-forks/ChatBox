function input_recorded() {
  $('#submit-button').addClass("btn-primary").removeClass("btn-warning").removeClass("btn-danger");
  $('#borderedbox').animate({"scrollTop": $('#borderedbox')[0].scrollHeight}, "slow");
  $('#chat-box').val("");
}

function input_error() {
  $('#submit-button').removeClass("btn-primary").addClass("btn-danger").removeClass("btn-warning");
  $('#borderedbox').animate({"scrollTop": $('#borderedbox')[0].scrollHeight}, "slow");
  $('#chat-box').val("");
}

//window.setInterval(function(){
//  $('#borderedbox').animate({"scrollTop": $('#borderedbox')[0].scrollHeight}, "slow");
//  Sijax.request('get_latest_messages');
//}, 5000);

window.setInterval(function(){
  Sijax.request('get_latest_update', [$('tr').last().attr('id')]);
}, 5000);

$(document).ready(function(){
  $('#borderedbox').animate({"scrollTop": $('#borderedbox')[0].scrollHeight}, "slow");
  $('#chat-box').focus()
});

$(document).keypress(function(event){

	var keycode = (event.keyCode ? event.keyCode : event.which);
	if(keycode == '13'){
		Sijax.request('take_input', [$('#chat-box').val(), $('tr').last().attr('id')]);
    $('#submit-button').removeClass("btn-primary").addClass("btn-warning");
    $('#chat-box').val("");
    $('#chat-box').focus()
	}
});
