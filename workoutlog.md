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
<form class="box"> 
  <label for="fname">First name:</label><br>
  <input type="fname" id="fnamework" name="fname" value="John" id="firstinput"><br>
  <label for="lname">Last name:</label><br>
  <input type="lname" id="lnamework" name="lname" value="Doe"><br><br>
  <label for="workout">Type of Workout:</label><br>
  <input type="workout" id="workoutwork" name="workout" value="Swimming"><br>
  <label for="date">Date of Completion:</label><br>
  <input type="date" id="datework" name="date" value="1/8"><br>
  <label for="numhours">Duration of workout (hours):</label><br>
  <input type="hours" id="hourswork" name="hours" value="10"><br><br>
  <input type="submit" value="Submit">
</form> 

</body>

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

<br>
<br>
<br>


<!--<script src="myscripts.js"></script>-->
<!---form action="/action_page.php"--->

<h2 style="text-align:center">Workout Log</h2>

<table>
  <tr>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Type of Workout</th>
    <th>Date of Completion</th>
    <th>Duration of Workout (hours)</th>
  </tr>
  <tr>
    <td>Lydia</td>
    <td>Cho</td>
    <td>Climbing</td>
    <td>2/13</td>
    <td>3</td>
  </tr>
  <tr>
    <td></td>
  
  </tr>
</table>


<table>
  <thead>
  <tr>
   <th>First Name</th>
    <th>Last Name</th>
    <th>Type of Workout</th>
    <th>Date of Completion</th>
    <th>Duration of Workout (hours)</th>
  </tr>
  </thead>
  <tbody id="table">
    <!-- javascript generated data -->
  </tbody>
</table>

<script>
  function create_User(){
    // extract data from inputs
    const first_name = document.getElementById("fnamework").value;
    const last_name = document.getElementById("lnamework").value;
    const workout = document.getElementById("workoutwork").value;
    const date = document.getElementById("datework").value;
    const numhours = document.getElementById("hourswork").value;
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer my-token',
        },
    };
    //url for Create API
    const url='/crud_api/create/' + first_name + '/' + last_name+ '/' + workout + '/' + date + '/' + numhours;
    //Async fetch API call to the database to create a new user
    fetch(url, requestOptions).then(response => {
        // prepare HTML search result container for new output
        const resultContainer = document.getElementById("result");
        // trap error response from Web API
        if (response.status !== 200) {
            const errorMsg = 'Database response error: ' + response.status;
            console.log(errorMsg);
            // Email must be unique, no duplicates allowed
            document.getElementById("pswError").innerHTML =
                "Email already exists in the table";
            return;
        }
        // response contains valid result
        response.json().then(data => {
            console.log(data);
            //add a table row for the new/created userId
            const tr = document.createElement("tr");
            for (let key in data) {
                if (key !== 'query') {
                    //create a DOM element for the data(cells) in table rows
                    const td = document.createElement("td");
                    console.log(data[key]);
                    //truncate the displayed password to length 20
                    if (key === 'password'){
                        td.innerHTML = data[key].substring(0,17)+"...";
                    }
                    else{
                        td.innerHTML = data[key];}
                    //add the DOM data element to the row
                    tr.appendChild(td);
                }
            }
            //append the DOM row to the table
            table.appendChild(tr);
        })
    })
}
</script>

<script>
  
// Static json, this can be used to test data prior to API and Model being ready
const json = '[{"_name": "Thomas Edison", "_uid": "toby"}, {"_name": "Nicholas Tesla", "_uid": "nick"}, {"_name": "John Mortensen", "_uid": "jm1021"}, {"_name": "Eli Whitney", "_uid": "eli"}, {"_name": "Hedy Lemarr", "_uid": "hedy"}]';

// Convert JSON string to JSON object
const data = JSON.parse(json);

// prepare HTML result container for new output
const table = document.getElementById("table");
data.forEach(user => {
    // build a row for each user
    const tr = document.createElement("tr");

    // td's to build out each column of data
    const first_name = document.createElement("td");
    const last_name = document.createElement("td");
    const workout = document.createElement("td");
    const date = document.createElement("td");
    const numhours = document.createElement("td");
           
    // add content from user data          
    first_name.innerHTML = user._firstname; 
    last_name.innerHTML = user._lastname; 
    workout.innerHTML = user._workout; 
    date.innerHTML = user._date; 
    numhours.innerHTML = user._numhours; 

    // add action for update button
    var updateBtn = document.createElement('input');
    updateBtn.type = "button";
    updateBtn.className = "button";
    updateBtn.value = "Update";
    updateBtn.style = "margin-right:16px";
    updateBtn.onclick = function () {
      alert("Update: " + user._uid);
    };
    action.appendChild(updateBtn);

    // add action for delete button
    var deleteBtn = document.createElement('input');
    deleteBtn.type = "button";
    deleteBtn.className = "button";
    deleteBtn.value = "Delete";
    deleteBtn.style = "margin-right:16px"
    deleteBtn.onclick = function () {
      alert("Delete: " + user._uid);
    };
    action.appendChild(deleteBtn);  

    // add data to row
    tr.appendChild(first_name);
    tr.appendChild(last_name);
    tr.appendChild(workout);
    tr.appendChild(date);
    tr.appendChild(numhours);

    // add row to table
    table.appendChild(tr);
});
</script> 

<!-->
<script>
  // prepare HTML result container for new output
  const resultContainer = document.getElementById("result");

  // prepare fetch options
  const url = "https://csa.nighthawkcodingsociety.com/api/person/all";
  const options = {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'omit', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
  };

  // fetch the API
  fetch(url, options)
      // response is a RESTful "promise" on any successful fetch
    .then(response => {
      // check for response errors
      if (response.status !== 200) {
          const errorMsg = 'Database response error: ' + response.status;
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
            // tr and td build out for each row
            const tr = document.createElement("tr");
            const name = document.createElement("td");
            const id = document.createElement("td");
            // data is specific to the API
            name.innerHTML = data[row].name; 
            id.innerHTML = data[row].email; 
            // add HTML to container
            tr.appendChild(name);
            tr.appendChild(id);
            resultContainer.appendChild(tr);
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
</script>


