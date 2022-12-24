document.getElementById("myForm").onsubmit = function (event) {
  event.preventDefault();

  (async () => {

    let response = await fetch("http://127.0.0.1:5000/submission_artist", {
      method: "POST",

      headers: {
        "Content-Type": "application/json",

      },
      body: JSON.stringify({
        Artist_Fname: document.getElementById("Fname").value.toString(),
        Artist_Lname: document.getElementById("Lname").value.toString(),
        Artist_address: document.getElementById("ArtistAdress").value.toString(),
        Artist_image: document.getElementById("AddImage").value.toString(),
        Artist_number: document.getElementById("AddNumber").value.toString(),
        Artist_description:
          document.getElementById("AddDescreption").value.toString(),
      }),
    });
    const result = await response.json();

    if(result && result.success)
    {
         document.getElementById("Fname").value = "";
         document.getElementById("Lname").value = "";
         document.getElementById("ArtistAdress").value = "";
         document.getElementById("AddImage").value = "";
         document.getElementById("AddNumber").value = "";
         document.getElementById("AddDescreption").value = "";
    }
  })();
};

document.getElementById("theatre_button").onclick = function (event) {
  event.preventDefault();

  (async () => {

    let response = await fetch("http://127.0.0.1:5000/create_teatre", {
      method: "POST",
      
      headers: {
        "Content-Type": "application/json",

      },
      body: JSON.stringify({
        theatre_mape_image: document.getElementById("seats_image").value.toString(),
        teatre_name: document.getElementById("name").value.toString(),
        theatre_image: document.getElementById("theatre_image").value.toString(),
        teatre_capacity: document.getElementById("capacity").value.toString(),
      }),
    });
    const result = await response.json();
    if(result && result.success)
    {
         document.getElementById("seats_image").value = "";
         document.getElementById("name").value = "";
         document.getElementById("theatre_image").value = "";
         document.getElementById("capacity").value = "";
    }
  })();
};

document.getElementById("add_event").onclick = function (event) {
  event.preventDefault();

  (async () => {

    let response = await fetch("http://127.0.0.1:5000/submission_event", {
      method: "POST",
      
      headers: {
        "Content-Type": "application/json",

      },
      body: JSON.stringify({
        event_name: document.getElementById("ev_name").value.toString(),
        event_start: document.getElementById("start_time").value.toString(),
        event_end: document.getElementById("end_time").value.toString(),
        event_image: document.getElementById("image").value.toString(),
        event_price: document.getElementById("price").value.toString(),
        event_description: document.getElementById("description").value.toString(),
        artist_id: document.getElementById("artist_id").value.valueOf(),
        loc_event_id: document.getElementById("theatre_id").value.valueOf(),
        event_category: document.getElementById("category").value.valueOf(),
      }),
    });
    const result = await response.json();
    if(result && result.success)
    {
         document.getElementById("ev_name").value = "";
         document.getElementById("start_time").value = "";
         document.getElementById("end_time").value = "";
         document.getElementById("image").value = "";
         document.getElementById("price").value = "";
         document.getElementById("description").value = "";
         document.getElementById("artist_id").value = "";
         document.getElementById("theatre_id").value = "";
         document.getElementById("category").value = "";
    }
  })();
};

document.getElementById('logout').onclick = function(){
  window.location.href = "./index.html";
}
