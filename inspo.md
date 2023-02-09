<style>
    img {
            display: block;
            margin-left: auto;
            margin-right: auto;
          }
        </style>

<h1 style="text-align:center">Motivational Quotes!</h1>
<div class="row"> 
  <div class="column">
    <img src="/images/mindsetquote.png" alt="mindset quote" style="width:100%">
  </div>
  <div class="column">
    <img src="/images/keepgoingquote.jpg" alt="keep going quote" style="width:100%">
  </div>
</div>
<div class="row">
    <div class="column">
    <img src="/images/hardquote.png" alt="hard quote" style="width:100%">
  </div>
  <div class="column">
    <img src="/images/progressquote.png" alt="progress quote" style="width:100%">
  </div>
 </div> 
<div class="row"> 
  <div class="column">
    <img src="/images/riskit.png" alt="mindset quote" style="width:100%">
  </div>
 </div> 

 <br>
 <br>
 <br>

<html>
<body>
<h1 style="text-align: center"> Do you Need Some Inspiration? </h1>
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
    <button type="button" onclick="alert('You are a baddie! \nKeep Slaying <3')">Click here!</button>
</body>
</html>

<br>
<br>
<br>

<body>

<h2 style="text-align:center">We're Hyping the Baddies Up! Input Inspirational Quotes Here!</h2>
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
  <label for="quote">Quote/Inspiration:</label><br>
  <input type="quote" id="quoteinspo" name="quote" value="You got this!"><br>
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

<h2 style="text-align:center">Quotes</h2>

<table>
  <tr>
    <th>Quotes</th>
    <th> </th>
    <th> </th>
  </tr>
  <tr>
    <td>"Hard work beats talent when talent doesn't work hard"</td>
    <td>Edit</td>
    <td>Delete</td>
  </tr>
</table>

<!-- POST STEP BELOW --->
<script>
function create_User(){
    // extract data from inputs
    const quote = document.getElementById("quoteinspo").value;
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer my-token',
        },
    };
    //url for Create API
    const url='/crud_api/create/' + quote;
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
                    //if (key === 'password'){
                       // td.innerHTML = data[key].substring(0,17)+"...";
                    //}
                    //else{
                      //  td.innerHTML = data[key];}
                    //add the DOM data element to the row
                    //tr.appendChild(td);
                }
            }
            //append the DOM row to the table
            table.appendChild(tr);
        })
    })
}
</script>


<table>
  <thead>
  <tr>
    <th>Quotes</th>
    <th>Actions</th>
  </tr>
  </thead>
  <tbody id="table">
    <!-- javascript generated data -->
  </tbody>
</table>

<script>
// Static json, this can be used to test data prior to API and Model being ready
const json = '[{"_quote": "Work Hard"}, {"_quote": "You do not sweat, you sparkle"}]';

// Convert JSON string to JSON object
const data = JSON.parse(json);

// prepare HTML result container for new output
const table = document.getElementById("table");
data.forEach(user => {
    // build a row for each user
    const tr = document.createElement("tr");

    // td's to build out each column of data
    const quote = document.createElement("td");
  
           
    // add content from user data          
    quote.innerHTML = user._quote; 
  
    // add action for update button
    var updateBtn = document.createElement('input');
    updateBtn.type = "button";
    updateBtn.className = "button";
    updateBtn.value = "Update";
    updateBtn.style = "margin-right:16px";
    updateBtn.onclick = function () {
      alert("Update: " + user._quote);
    };
    action.appendChild(updateBtn);

    // add action for delete button
    var deleteBtn = document.createElement('input');
    deleteBtn.type = "button";
    deleteBtn.className = "button";
    deleteBtn.value = "Delete";
    deleteBtn.style = "margin-right:16px"
    deleteBtn.onclick = function () {
      alert("Delete: " + user._quote);
    };
    action.appendChild(deleteBtn);  

    // add data to row
    tr.appendChild(quote);
    tr.appendChild(action);

    // add row to table
    table.appendChild(tr);
});
</script>




<p> NEW THING MY DATA </p>


<table>
  <thead>
  <tr>
    <th>Quotes</th>
  </tr>
  </thead>
  <tbody id="result">
    <!-- javascript generated data -->
  </tbody>
</table>

<form action="javascript:create_user()">
    <p><label>
        Quote:
        <input type="text" name="quote" id="quote" required>
    </label></p>
    <p>
        <button>Submit</button>
    </p>
</form>

<script>
  // prepare HTML result container for new output
  const resultContainer = document.getElementById("result");
  // prepare URL's to allow easy switch from deployment and localhost
  const url = "http://172.22.184.170:4002///api/users"
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
        quote: document.getElementById("quote").value,
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
    const quote = document.createElement("td");

  

    // obtain data that is specific to the API
    quote.innerHTML = data.quote; 
  
  

    // add HTML to container
    tr.appendChild(quote);

    resultContainer.appendChild(tr);
  }

</script>

