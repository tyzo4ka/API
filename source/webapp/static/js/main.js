function hello() {
    console.log('Tratata')
}

function addition() {
     var b = document.getElementById('B').value;
     console.log(b)
     var a = document.getElementById('A').value;
     console.log(a)
     $.ajax({
     url: "http://127.0.0.1:5000/add/",
     method: 'POST',
     dataType: "json",
     contentType: "application/json",
     data: JSON.stringify({"A": a, "B": b}),
     success: function(response) { console.log(response); },
     error: function(response) { console.log(response); }
 });
 }

function subtraction() {
     var b = document.getElementById('B').value;
     console.log(b)
     var a = document.getElementById('A').value;
     console.log(a)
     $.ajax({
     url: "http://127.0.0.1:5000/subtract/",
     method: 'POST',
     dataType: "json",
     contentType: "application/json",
     data: JSON.stringify({"A": a, "B": b}),
     success: function(response) { console.log(response); },
     error: function(response) { console.log(response); }
 });
 }

 function multiply() {
     var b = document.getElementById('B').value;
     console.log(b)
     var a = document.getElementById('A').value;
     console.log(a)
     $.ajax({
     url: "http://127.0.0.1:5000/multiply/",
     method: 'POST',
     dataType: "json",
     contentType: "application/json",
     data: JSON.stringify({"A": a, "B": b}),
     success: function(response) { console.log(response); },
     error: function(response) { console.log(response); }
 });
 }

 function divide() {
     var b = document.getElementById('B').value;
     console.log(b)
     var a = document.getElementById('A').value;
     console.log(a)
     $.ajax({
     url: "http://127.0.0.1:5000/divide/",
     method: 'POST',
     dataType: "json",
     contentType: "application/json",
     data: JSON.stringify({"A": a, "B": b}),
     success: function(response) { console.log(response); },
     error: function(response) { console.log(response); }
 });
 }