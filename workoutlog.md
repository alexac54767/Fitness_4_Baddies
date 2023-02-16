## Workout Log
> Log your workouts below!

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
<form action="javascript:create_workout()">
    <p><label>
        First Name:
        <input type="text" name="fname" id="fname" required>
    </label></p>
    <p><label>
        Last Name:
        <input type="text" name="lname" id="lname" required>
    </label></p>
    <p><label>
        Type of Workout:
        <input type="text" name="workout" id="workout" required>
    </label></p>
    <p><label>
        Date of Completion:
        <input type="date" name="date" id="date" required>
    </label></p>
    <p><label>
        Duration of Workout (hours):
        <input type="integer" name="hours" id="hours">
    </label></p>
    <p>
        <button>Submit</button>
    </p>
</form>

</body>


<br>
<br>
<br>


<!--<script src="myscripts.js"></script>-->
<!---form action="/action_page.php"--->

<h2 style="text-align:center">Workout Log</h2>

<table>
  <thead>
  <tr>
    <th> First Name</th>
    <th>Last Name</th>
    <th>Type of Workout</th>
    <th>Date of Completion</th>
    <th>Duruation of Workout (hours)</th>
  </tr>
  </thead>
  <tbody id="result">
    <!-- javascript generated data -->
  </tbody>
</table>





<script>
  // prepare HTML result container for new output
  const resultContainer = document.getElementById("result");
  // prepare URL's to allow easy switch from deployment and localhost
  const url = "http://172.22.186.118:8086/api/workout"
  //const url = "https://flask.nighthawkcodingsociety.com/api/users"
  const create_fetch = url + '/create';
  const read_fetch = url + '/';

  // Load users on page entry
  read_workout();


  // Display User Table, data is fetched from Backend Database
  function read_workout() {
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

  function create_workout(){
    //Validate Password (must be 6-20 characters in len)
    //verifyPassword("click");
    const body = {
        fname: document.getElementById("fname").value,
        lname: document.getElementById("lname").value,
        workout: document.getElementById("workout").value,
        date: document.getElementById("date").value,
        hours: document.getElementById("hours").value
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
    const fname = document.createElement("td");
    const lname = document.createElement("td");
    const workout = document.createElement("td")
    const date = document.createElement("td");
    const hours = document.createElement("td");
  

    // obtain data that is specific to the API
    fname.innerHTML = data.fname; 
    lname.innerHTML = data.lname; 
    workout.innerHTML = data.workout;
    date.innerHTML = data.date; 
    hours.innerHTML = data.hours; 

    // add HTML to container
    tr.appendChild(fname);
    tr.appendChild(lname);
    tr.appendChild(workout);
    tr.appendChild(date);
    tr.appendChild(hours);

    resultContainer.appendChild(tr);
  }

</script>



