

<table>
  <thead>
  <tr>
    <th>Name</th>
    <th>Date Completed</th>
    <th>Total Hours</th>
    <th>Type of Workout</th>
  </tr>
  </thead>
  <tbody id="result">
    <!-- javascript generated data -->
  </tbody>
</table>


<form action="javascript:create_workout()">
    <p><label>
        Name:
        <input type="text" name="name3" id="name3" required>
    </label></p>
    <p><label>
        Date of Completion:
        <input type="date" name="date" id="date" required>
    </label></p>
    <p><label>
        Number of Hours Completed:
        <input type="integer" name="duration" id="duration" required>
    </label></p>
    <p><label>
        Type of Workout:
        <input type="text" name="type" id="type" required>
    </label></p>
    <p>
        <button>Submit</button>
    </p>
</form>

<script>
  // prepare HTML result container for new output
  const resultContainer = document.getElementById("result");
  // prepare URL's to allow easy switch from deployment and localhost
  //const url = "http://172.31.51.55:8081/api/workout"
  const url = "https://teambaddieflask.duckdns.org"
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
    const body = {
        name3: document.getElementById("name3").value,
        date: document.getElementById("date").value,
        duration: document.getElementById("duration").value,
        type: document.getElementById("type").value
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
    const name3 = document.createElement("td");
    const date = document.createElement("td");
    const duration = document.createElement("td");
    const type = document.createElement("td");

    // obtain data that is specific to the API
    name3.innerHTML = data.name3; 
    date.innerHTML = data.date; 
    duration.innerHTML = data.duration; 
    type.innerHTML = data.type; 

    // add HTML to container
    tr.appendChild(name3);
    tr.appendChild(date);
    tr.appendChild(duration);
    tr.appendChild(type);

    resultContainer.appendChild(tr);
  }

</script>

<!-- END OF NEW CODE-->

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



