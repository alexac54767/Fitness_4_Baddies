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
    <img src="https://user-images.githubusercontent.com/111482658/219490933-b938f844-9f32-4ab1-a7cf-5e6c63f6fbc8.png" alt="mindset quote" style="width:100%">
  </div>
  <div class="column">
    <img src="https://user-images.githubusercontent.com/111482658/219490931-ff8620a5-687a-464b-a384-34ae24a681b3.jpg" alt="keep going quote" style="width:100%">
  </div>
</div>
<div class="row">
    <div class="column">
    <img src="https://user-images.githubusercontent.com/111482658/219490926-70c75633-ab4c-4315-9d00-26a37e67cb4c.png" alt="hard quote" style="width:100%">
  </div>
  <div class="column">
    <img src="https://user-images.githubusercontent.com/111482658/219490936-23ca6bbf-5178-403a-b096-be8fbd833233.png" alt="progress quote" style="width:100%">
  </div>
 </div> 
<div class="row"> 
  <div class="column">
    <img src="https://user-images.githubusercontent.com/111482658/219490940-66d1a950-cd2f-4c25-846b-66babdcba103.png" alt="mindset quote" style="width:100%">
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

<form action="javascript:create_quote()">
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
  //const url = "http://172.28.92.6:8081//api/Inspo"
  const url = "https://teambaddieflask.duckdns.org/api/Inspo"
  const create_fetch = url + '/create';
  const read_fetch = url + '/';

  // Load users on page entry
  read_Inspos();


  // Display User Table, data is fetched from Backend Database
  function read_Inspos() {
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

  function create_quote(){
    const body = {
        quote: document.getElementById("quote").value
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
          alert('Quote is too short, please refresh and enter a longer quote') // alert if quote is too short
        }
        if (response.status !== 200) {
          const errorMsg = 'Database adding quote error: ' + response.status;
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
            //add a table row for the new/created quote
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

