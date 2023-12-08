function Details() {
    document.querySelectorAll(".details_js").forEach(function (detailsButton) {
        detailsButton.addEventListener("click", function () {
            var url = this.getAttribute("data-url");
            const modalId = "details_form";
            var modal = document.getElementById(modalId);
            if (modal == null) {
                modal = document.createElement("section");
                modal.id = modalId;
                modal.className = "modal"; 
                document.body.appendChild(modal);
            }

            fetch(url).then(function (response) {
                return response.text();
            }).then(function (data) {
                modal.innerHTML = data;
                modal.style.display = "block";
                ModalsWindows();

                const forms = modal.querySelectorAll("form");
                forms.forEach(function (form) {
                    form.addEventListener("submit", function (e) {
                        e.preventDefault();
                        const formData = new FormData(this);
                        var url = this.action;

                        fetch(url, {
                            method: "POST",
                            body: formData,
                        }).then(function (response) {
                            if (response.redirected) {
                                window.location.href = response.url;
                            } else {
                                response.text().then(function (data) {
                                    modal.innerHTML = data;
                                    ModalsWindows();
                                });
                            }
                        });
                    });
                });
            });
        });
    });
}

Details();
