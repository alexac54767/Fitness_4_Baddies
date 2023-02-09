{% include ispetable.html %}

## Grades for ISPE
> grades sweetie

<html>
<body>
<!--
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
  <label for="name">Name:</label><br>
  <input type="name" id="namegrades" name="name" value="John" id="firstinput"><br>
  <label for="date">Date of Completion:</label><br>
  <input type="date" id="dategrades" name="date" value="4/11"><br>
  <label for="numhours">Number of Hours Completed:</label><br>
  <input type="hours" id="hoursgrades" name="hours" value="3"><br><br>
  <input type="submit" value="Submit">
</form> 

<!-- </body> >

<!--
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
    <th>Name</th>
    <th>Total Hours</th>
    <th>Date Completed</th>
    <th>Grade</th>
    <th> </th>
    <th> </th>
  </tr>
  <tr>
    <td>Alexa Carlson</td>
    <td>5</td>
    <td>1/25/2023</td>
    <td>B</td>
    <td>Edit</td>
    <td>Delete</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>
-->
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



<!-- STARTING HERE IS MORT'S CODE-->


<table>
  <thead>
  <tr>
    <th>Name</th>
    <th>Total Hours</th>
    <th>Date Completed</th>
    <th>Grade</th>
  </tr>
  </thead>
  <tbody id="result">
    <!-- javascript generated data -->
  </tbody>
</table>


<form action="javascript:create_user()">
    <p><label>
        Name:
        <input type="text" name="name" id="name" required>
    </label></p>
    <p><label>
        Date of Completion:
        <input type="date" name="dategrades" id="dategrades" required>
    </label></p>
    <p><label>
        Number of Hours Completed:
        <input type="text" name="hoursgrades" id="hoursgrades" required>
    </label></p>
    <p><label>
        Grade:
        <input type="text" name="grade" id="grade" required>
    </label></p>
    <p>
        <button>Submit</button>
    </p>
</form>

<script>
  // prepare HTML result container for new output
  const resultContainer = document.getElementById("result");
  // prepare URL's to allow easy switch from deployment and localhost
  const url = "http://172.31.81.86:4002/api/users"
  //const url = "https://flask.nighthawkcodingsociety.com/api/users"
  const create_fetch = url + '/create';
  const read_fetch = url + '/';

  // Load users on page entry
  read_users();


  // Display User Table, data is fetched from Backend Database
  function read_users() {
    // prepare fetch options
    const read_options = {
      method: 'GET', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'omit', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
      },
    };

    // fetch the data from API
    fetch(read_fetch, read_options)
      // response is a RESTful "promise" on any successful fetch
      .then(response => {
        // check for response errors
        if (response.status !== 200) {
            const errorMsg = 'Database read error: ' + response.status;
            console.log(errorMsg);
            const tr = document.createElement("tr");
            const td = document.createElement("td");
            td.innerHTML = errorMsg;
            tr.appendChild(td);
            resultContainer.appendChild(tr);
            return;
        }
        // valid response will have json data
        response.json().then(data => {
            console.log(data);
            for (let row in data) {
              console.log(data[row]);
              add_row(data[row]);
            }
        })
    })
    // catch fetch errors (ie ACCESS to server blocked)
    .catch(err => {
      console.error(err);
      const tr = document.createElement("tr");
      const td = document.createElement("td");
      td.innerHTML = err;
      tr.appendChild(td);
      resultContainer.appendChild(tr);
    });
  }

  function create_user(){
    const body = {
        name: document.getElementById("name").value,
        dategrades: document.getElementById("dategrades").value,
        hoursgrades: document.getElementById("hoursgrades").value,
        grade: document.getElementById("grade").value
    };
    const requestOptions = {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            "content-type": "application/json",
            'Authorization': 'Bearer my-token',
        },
    };

    // URL for Create API
    // Fetch API call to the database to create a new user
    fetch(create_fetch, requestOptions)
      .then(response => {
        // trap error response from Web API
        if (response.status !== 200) {
          const errorMsg = 'Database create error: ' + response.status;
          console.log(errorMsg);
          const tr = document.createElement("tr");
          const td = document.createElement("td");
          td.innerHTML = errorMsg;
          tr.appendChild(td);
          resultContainer.appendChild(tr);
          return;
        }
        // response contains valid result
        response.json().then(data => {
            console.log(data);
            //add a table row for the new/created userid
            add_row(data);
        })
    })
  }

  function add_row(data) {
    const tr = document.createElement("tr");
    const name = document.createElement("td");
    const dategrades = document.createElement("td");
    const hoursgrades = document.createElement("td");
    const grade = document.createElement("td");

    // obtain data that is specific to the API
    name.innerHTML = data.name; 
    dategrades.innerHTML = data.dategrades; 
    hoursgrades.innerHTML = data.hoursgrades; 
    grade.innerHTML = data.grade; 

    // add HTML to container
    tr.appendChild(name);
    tr.appendChild(dategrades);
    tr.appendChild(hoursgrades);
    tr.appendChild(grade);

    resultContainer.appendChild(tr);
  }

</script>
