function Logout() {
  document.querySelectorAll(".logout_js").forEach(function (logoutButton) {
      logoutButton.addEventListener("click", function () {
          var confirmed = confirm("Вы действительно хотите выйти?");
          if (confirmed) {
              var url = "/accounts/logout/";
              window.location.href = url;
          }
      });
  });

  // Добавляем обработчик для кнопки "Отменить"
  var cancelButton = document.querySelector(".cancel-js");
  if (cancelButton) {
      cancelButton.addEventListener("click", function () {
          goBack();
      });
  }

  function goBack() {

function Logout() {
    document.querySelectorAll(".logout_js").forEach(function (logoutButton) {
        logoutButton.addEventListener("click", function () {
            var confirmed = confirm("Вы действительно хотите выйти?");
            if (confirmed) {
                var url = "/accounts/logout/";
                window.location.href = url;
            }
        });
    });

    // Добавляем обработчик для кнопки "Отменить"
    var cancelButton = document.querySelector(".cancel-js");
    if (cancelButton) {
        cancelButton.addEventListener("click", function () {
            goBack();
        });
    }

    function goBack() {
        window.history.back();
    }
}

Logout();

      window.history.back();
  }
}

Logout();
