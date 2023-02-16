{% include workouts.html %}

# Workouts by you guys!


<body>

<h2 style="text-align:center">Input Your Workout Below</h2>
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

<!--
<form class="box"> 
  <label for="workout">Workout:</label><br>
  <input type="workout" id="workout2" name="workout" value="Burpees"><br>
  <label for="Exercise">Type of Exercise:</label><br>
  <input type="exercise" id="exercise" name="exercise" value="Endurance"><br>
  <label for="Time">Duration of workout:</label><br>
  <input type="hours" id="hours" name="hours" value="2"><br>
  <label for="sets">Number of sets/reps:</label><br>
  <input type="sets" id="sets" name="sets" value="12"><br><br>
  <input type="submit" value="Submit">
</form> 

</body>


<h2 style="text-align:center">Workouts from You!</h2>

<table>
  <tr>
    <th>Type of Workout</th>
    <th>Exercise</th>
    <th>Time</th>
    <th>Sets/Reps</th>
    <th> </th>
    <th> </th>
  </tr>
  <tr>
    <td>Climbing</td>
    <td>Endurance</td>
    <td>4 minutes</td>
    <td>4 climbs</td>
    <td>Edit</td>
    <td>Delete</td>
  </tr>
  <tr>
    <td></td>
  
  </tr>
</table>
-->

<!-- UPDATES WITH NEW API-->

<table>
  <thead>
  <tr>
    <th>Exercise</th>
    <th>Number of Sets</th>
    <th>Number of Repetitions</th>
  </tr>
  </thead>
  <tbody id="result">
    <!-- javascript generated data -->
  </tbody>
</table>


<form action="javascript:create_user()">
    <p><label>
        Exercise Type:
        <input type="exerciseType" name="exerciseType" id=
        "exerciseType" required>
    </label></p>
    <p><label>
        Number of Sets:
        <input type="sets" name="sets" id="sets" required>
    </label></p>
    <p><label>
        Number of Repetitions:
        <input type="integer" name="reps" id="reps" required>
    </label></p>
    <p>
        <button>Submit</button>
    </p>
</form>

<!-- Fetch data from backend api-->

<script>
  // prepare HTML result container for new output
  const resultContainer = document.getElementById("result");
  // prepare URL's to allow easy switch from deployment and localhost
  const url = "http://10.8.140.23:8086/api/Inputworkout"
  //const url = "https://flask.nighthawkcodingsociety.com/api/users"
  const create_fetch = url + '/create';
  const read_fetch = url + '/';

  // Load users on page entry
  read_inputworkouts();


  // Display User Table, data is fetched from Backend Database
  function read_inputworkouts() {
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

  function create_inputworkout(){
    const body = {
        exerciseType: document.getElementById("exerciseType").value,
        sets: document.getElementById("sets").value,
        reps: document.getElementById("reps").value,
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
    const exerciseType = document.createElement("td");
    const reps = document.createElement("td");
    const sets = document.createElement("td");

    // obtain data that is specific to the API
    exerciseType.innerHTML = data.exerciseType; 
    sets.innerHTML = data.sets; 
    reps.innerHTML = data.reps; 

    // add HTML to container
    tr.appendChild(exerciseType);
    tr.appendChild(sets);
    tr.appendChild(reps);

    resultContainer.appendChild(tr);
  }

</script>

<!-- END OF NEW -->
