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

<h2 style="text-align:center">Workout Log</h2>

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


<p>Database API</p>

<table>
  <thead>
  <tr>
    <th>Quotes (FROM API)</th>
  </tr>
  </thead>
  <tbody id="result">
    <!-- javascript generated data -->
  </tbody>
</table>

<script>
  // prepare HTML result container for new output
  const resultContainer = document.getElementById("result");

  // prepare fetch options
  const url = "http://localhost:4002/api/users";
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
            // tr and td element id's to build out for each row
            const tr = document.createElement("tr");
            const quote = document.createElement("td");
        

            // obtain data that is specific to the API
            quote.innerHTML = data[row].; 
      

            // add HTML to container
            tr.appendChild(quote);
           

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


