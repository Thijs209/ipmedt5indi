<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="/js/main.js"></script>
    <title>Document</title>
</head>
<body>
    <h1>
        Counter: {{$count}}
    </h1>
    <a href="http://127.0.0.1:8000/led">
        <button>Licht knop {{$led}}</button>
    </a>
</body>
</html>