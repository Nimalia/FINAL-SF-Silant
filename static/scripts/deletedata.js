    // Обработчик для иконки "крестик"-удаление инфы
    var deleteIcons = document.querySelectorAll('.deletedata');
    deleteIcons.forEach(function (icon) {
        icon.addEventListener('click', function (event) {
            event.preventDefault();
            var url = icon.dataset.url;
            //  логика подтверждения удаления
            if (confirm('Вы уверены, что хотите удалить запись?')) {
                window.location.href = url;
            }
        });
    });

