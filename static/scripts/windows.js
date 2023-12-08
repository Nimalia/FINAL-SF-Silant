function ModalsWindows() {
    var modals = document.querySelectorAll(".modal-area, .modal-exit, .cancel-js");

    modals.forEach(function (modal) {
        modal.addEventListener("click", function () {
            var closestSection = findClosestSection(this);
            if (closestSection) {
                closestSection.style.display = "none";
            }
        });
    });

    function findClosestSection(element) {
        while (element) {
            if (element.tagName === "SECTION") {
                return element;
            }
            element = element.parentElement;
        }
        return null;
    }
}

// Помещаем функцию createModal в глобальную область видимости
window.createModal = function (message, callback) {
    var modalContainer = document.createElement("div");
    modalContainer.className = "modal";
    modalContainer.innerHTML = '<div class="modal-content">' +
        '<p>' + message + '</p>' +
        '<button id="modal-yes">Да</button>' +
        '<button id="modal-no">Нет</button>' +
        '</div>';

    document.body.appendChild(modalContainer);

    // обработчики для кнопок
    document.getElementById("modal-yes").addEventListener("click", function () {
        modalContainer.style.display = "none";
        if (callback) {
            callback(true);
        }
    });

    document.getElementById("modal-no").addEventListener("click", function () {
        modalContainer.style.display = "none";
        if (callback) {
            callback(false);
        }
    });

    return modalContainer;
};
