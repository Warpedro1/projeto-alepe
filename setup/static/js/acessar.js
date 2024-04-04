function changeImage2() {
  var input = document.getElementById("passwordInput");
  var button = document.getElementById("eyeButton");
  if (input.type == "password"){
    input.type = "text";
    button.style.backgroundImage = "url('assets/images/acessar/blue_circular_icon.png')";
  } else if (input.type == "text") {
    input.type = "password";
    button.style.backgroundImage = "url('assets/images/acessar/blue_diagonal_line_icon.png'), url('assets/images/acessar/blue_circular_icon.png')";
  }
}


  function limparCampo2() {
    document.getElementById("emailInput").value = "";
  }

  function changeTypePasswordOnSubmit2() {
    var input = document.getElementById("passwordInput");
    var button = document.getElementById("eyeButton");
    if (input.type == "text") {
      input.type = "password";
      button.style.backgroundImage = "url('assets/images/acessar/blue_diagonal_line_icon.png'), url('assets/images/acessar/blue_circular_icon.png')";
  }

  }