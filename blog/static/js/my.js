////alert('Hellow JS!');
//
//
//var button = document.querySelector("#btn-joke");
////console.log(button);
//
//function foo()
//{
//    alert('Hellow JS!');
//}
//
//button.addEventListener('click', foo, false);



//alert('Hello Js!');
//
//
//var button = document.querySelector("#btn-joke");
////console.log(button);
//
//function foo(event)
//{
//    element = event.target;
//
//    if ( element.classList.contains('btn-info') )
//    {
//        var new_class = 'btn-danger';
//        var old_class = 'btn-info';
//    }
//    else {
//        var new_class = 'btn-info';
//        var old_class = 'btn-danger';
//    }
//
//    element.classList.remove(old_class);
//    element.classList.add(new_class);
//}
//
//button.addEventListener('click', foo, false);
//
//// ajax
//$( document ).on('click', '#ajax-btn', function(event) {
//    console.log('Step 1');
//    $.ajax({
//                url: '/users/update-token-ajax/',
//                success: function (data) {
//                    // data - ответ от сервера
//                    console.log('Step 3')
//                    console.log(data);
//                    $('#token').html(data.key);
//                },
//            });
//});
//

//$( document ).on('click', '#categories', function(event) {
//    $.ajax({
//                url: '/api/v0/categories/',
//                success: function (data) {
//                    // data - ответ от сервера
//                    console.log('Step 3')
//                    //console.log(data);
//                    for (i = 0; i < data.length; i++) {
//                        // словарь
//                       item = data[i];
//                       name = item.name;
//                       console.log(name);
//                       $('#div_categories').append('<li>' + name + '</li>' );
//                    }
//                    //$('#wrapper').append('<a href="http://google.com">Гугли!</a>');
//                    //$('#div_categories').html(data);
//                },
//            });
//});
//
//
//$( document ).on('click', '#posts', function(event) {
//    $.ajax({
//                url: '/api/v0/posts/',
//                success: function (data) {
//                    // data - ответ от сервера
//                    //console.log(data);
//                    for (i = 0; i < data.length; i++) {
//                        // словарь
//                       item = data[i];
//                       name = item.name;
//                       console.log(name);
//                       $('#div_posts').append('<li>' + name + '</li>' );
//                    }
//                    //$('#wrapper').append('<a href="http://google.com">Гугли!</a>');
//                    //$('#div_categories').html(data);
//                },
//            });
//});
//
//
//$( document ).on('click', '#all', function(event) {
//$.ajax({
//                url: '/api/v0/categories/',
//                success: function (data) {
//                    // data - ответ от сервера
//                    console.log('Step 3')
//                    //console.log(data);
//                    for (i = 0; i < data.length; i++) {
//                        // словарь
//                       item = data[i];
//                       name = item.name;
//                       console.log(name);
//                       $('#div_categories').append('<li>' + name + '</li>' );
//                    }
//                    //$('#wrapper').append('<a href="http://google.com">Гугли!</a>');
//                    //$('#div_categories').html(data);
//                },
//            });
//    $.ajax({
//                url: '/api/v0/posts/',
//                success: function (data) {
//                    // data - ответ от сервера
//                    //console.log(data);
//                    for (i = 0; i < data.length; i++) {
//                        // словарь
//                       item = data[i];
//                       name = item.name;
//                       console.log(name);
//                       $('#div_posts').append('<li>' + name + '</li>' );
//                    }
//                    //$('#wrapper').append('<a href="http://google.com">Гугли!</a>');
//                    //$('#div_categories').html(data);
//                },
//            });
//});


//alert('Hello Js!');
//
//var button = document.querySelector("#btn-joke");
//
//function foo(event) {
//    var element = event.target;
//    var new_class, old_class;
//
//    if (element.classList.contains('btn-info')) {
//        new_class = 'btn-danger';
//        old_class = 'btn-info';
//    } else {
//        new_class = 'btn-info';
//        old_class = 'btn-danger';
//    }
//
//    element.classList.remove(old_class);
//    element.classList.add(new_class);
//}
//
//if (button) {
//    button.addEventListener('click', foo, false);
//}
//
//// AJAX
//$(document).on('click', '#ajax-btn', function(event) {
//    console.log('Step 1');
//    $.ajax({
//        url: '/users/update-token-ajax/',
//        success: function(data) {
//            // data - ответ от сервера
//            console.log('Step 3');
//            console.log(data);
//            $('#token').html(data.key);
//        },
//        error: function(xhr, status, error) {
//            console.log('Error: ' + error);
//            alert('An error occurred while updating the token.');
//        }
//    });
//});






// Простой пример JavaScript
alert('Hello Js!');

// JavaScript для переключения класса кнопки
var button = document.querySelector("#btn-joke");

function toggleButtonClass(event) {
    var element = event.target;
    element.classList.toggle('btn-info');
    element.classList.toggle('btn-danger');
}

if (button) {
    button.addEventListener('click', toggleButtonClass);
}

// AJAX запрос через jQuery
$(document).on('click', '#ajax-btn', function(event) {
//    console.log('AJAX request started');
//    $.ajax({
//        url: 'update_token_ajax/',  // Проверьте, что URL правильный
//        success: function(data) {
//            console.log('AJAX request successful');
//            console.log(data);
//            $('#token').text(data.key);  // Обновление содержимого элемента с id token
//        },
//        error: function(xhr, status, error) {
//            console.error('AJAX request error: ' + error);
//            alert('An error occurred while updating the token.');
//        }
//    });
//});

    console.log('Step 1');
    $.ajax({
                url: 'users/update-token-ajax/',
                success: function (data) {
                    $('.details').html(data.result);
                },
             });
});