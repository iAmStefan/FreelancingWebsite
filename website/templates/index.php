{% load staticfiles %}
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="{% static 'css/indexStyle.css' %}" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
    <link rel="shortcut icon" type="image/x-icon" href="{% static 'images/favicon.ico' %}">
    <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lines of Code</title>
  </head>
  <body>
    <div class="start">
      <div class="container">
        <br></br><br></br>
        <p>Here you can have a look at my programming skills, portfolio recently created projects, and my offered services.</p>
        <p1>If you you want to contact me you can do it <a href="{% url 'contact'%}">here</a>.</p1>
        <a href="{% url 'home' %}"><p2>See my website</p2></a>
      </div>
    </div>
  </body>
</html>
