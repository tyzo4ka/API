function addition() {
    var b = document.getElementById('B').value;
    var answer = document.getElementsByClassName("answer")
    var a = document.getElementById('A').value;
    $.ajax({
        url: "http://127.0.0.1:5000/add/",
        method: 'POST',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({"A": a, "B": b}),
        success: function (data) {
            answer[0].innerHTML += `<p style="color: green;">${data.answer}</p>`;
        },
        error: function (data) {
            answer[0].innerHTML += `<p style="color: red;">${data.responseJSON.error}</p>`;
        }
    });
}

function subtraction() {
    var b = document.getElementById('B').value;
    var a = document.getElementById('A').value;
    var answer = document.getElementsByClassName("answer")

    $.ajax({
        url: "http://127.0.0.1:5000/subtract/",
        method: 'POST',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({"A": a, "B": b}),
        success: function (data) {
            answer[0].innerHTML += `<p style="color: green;">${data.answer}</p>`
        },
        error: function (data) {
            answer[0].innerHTML += `<p style="color: red;">${data.responseJSON.error}</p>`;
        }
    });
}

function multiply() {
    var b = document.getElementById('B').value;
    var a = document.getElementById('A').value;
    var answer = document.getElementsByClassName("answer")
    $.ajax({
        url: "http://127.0.0.1:5000/multiply/",
        method: 'POST',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({"A": a, "B": b}),
        success: function (data) {
            answer[0].innerHTML += `<p style="color: green;">${data.answer}</p>`
        },
        error: function (data) {
            answer[0].innerHTML += `<p style="color: red;">${data.responseJSON.error}</p>`;
        }
    });
}

function divide() {
    var b = document.getElementById('B').value;
    var a = document.getElementById('A').value;
    var answer = document.getElementsByClassName("answer")

    $.ajax({
        url: "http://127.0.0.1:5000/divide/",
        method: 'POST',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({"A": a, "B": b}),
        success: function (data) {
            answer[0].innerHTML += `<p style="color: green;">${data.answer}</p>`
        },
        error: function (data) {
            answer[0].innerHTML += `<p style="color: red;">${data.responseJSON.error}</p>`;
        }
    });
}

function calculate(action) {
    var b = document.getElementById('B').value;
    var a = document.getElementById('A').value;
    var answer = document.getElementsByClassName("answer")

    $.ajax({
        url: "http://127.0.0.1:5000/" + $(action).data('id') + "/",
        method: 'POST',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({"A": a, "B": b}),
        success: function (data) {
            answer[0].innerHTML += `<p style="color: green;">${data.answer}</p>`
        },
        error: function (data) {
            answer[0].innerHTML += `<p style="color: red;">${data.responseJSON.error}</p>`;
        }
    });
}