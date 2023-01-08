{% include ispetable.html %}

## Grades for ISPE
> grades sweetie

<html>
<body>

<h2 style="text-align:center">Input the Duration of Your Workout Below</h2>
<style>
    form {
            display: block;
            margin-left: auto;
            margin-right: auto;
            background-color: #4682B4;
            border: white;
            color: white;
            padding: 15px 32px;
            text-align: center;
        }
</style>
<form class="box">
  <label for="fname">First name:</label><br>
  <input type="text" id="fnamegrades" name="fname" value="John" id="firstinput"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lnamegrades" name="lname" value="Doe"><br><br>
  <label for="date">Date of Completion:</label><br>
  <input type="text" id="dategrades" name="date" value="4/11"><br>
  <label for="numhours">Number of Hours Completed:</label><br>
  <input type="text" id="hoursgrades" name="hours" value="3"><br><br>
  <input type="submit" value="Submit">
</form> 

</body>


<head>
<style>
    table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
    }
    tr:nth-child(even) {
    background-color: #4F4B4C;
    }
</style>
</head>
<body>

<br>
<br>
<br>

<h2 style="text-align:center">Grades</h2>

<table>
  <tr>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Total Hours</th>
    <th>Grade</th>
  </tr>
  <tr>
    <td>Alexa</td>
    <td>Carlson</td>
    <td>5</td>
    <td>B</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>
<style>
 button {
            background-color: #128ca7;
            color: black;
            text-align: center;
            font-size: 15px;
            height: 75;
            width: 500;
            margin-left: auto;
            margin-right: auto;
            padding: 15px 32px;
            display: flex;
            justify-content: center;
         }

</style>

<br>
<br>
<button type="button" onclick="window.print();" class>Click here to print your report</button>
</body>

</html>



