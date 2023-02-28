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

<form action="javascript:create_inputworkout()">
    <p><label>
        Exercise Type:
        <input type="text" name="exerciseType" id=
        "exerciseType" required>
    </label></p>
    <p><label>
        Number of Sets:
        <input type="number" name="sets" id="sets" required>
    </label></p>
    <p><label>
        Number of Repetitions:
        <input type="number" name="reps" id="reps" required>
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
  const url = "http://192.168.0.117:8081/api/Inputworkout"
  //const url = "https://teambaddieflask.duckdns.org/api/Inputworkout 
  const create_fetch = url + '/create';
  const read_fetch = url + '/';
  // Load users on page entry
  read_inputworkout();
  // Display User Table, data is fetched from Backend Database
  function read_inputworkout() {
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
        if (response.status == 210) {
          alert('Exercise is not inputted, please refresh and enter an exercise')
        }
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









