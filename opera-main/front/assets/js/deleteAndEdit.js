(async () => {

    let response = await fetch("http://127.0.0.1:5000/show_artist", {
        method: "GET",

        headers: {
            "Content-Type": "application/json",

        },

    });
    const result = await response.json();
    let artistCard ="";
    result.artists.map(element => {
            const name = element.fname+" " + element.lname
            const descreption = element.description
            const image = element.image_link
             const artistId = element.id
            artistCard += ` <div class="card text-center" style="margin-top: 20px;" style="width: 18rem;">
            <div class="card-body">
              <img src="${image}" alt="artist image"/>
              <h5 class="card-title">${name}</h5>
              <p class="card-text">${descreption}</p>
              <a href="#" class="btn btn-danger" id="delete-btn" onclick="artistDeleteBtn(${artistId})">Delete</a>
              <a href="home.html" class="btn btn-primary" onclick="artistEditBtn(${artistId})">Edit</a>
          
            </div>
          </div>`
    });
    document.getElementById('showArtist').innerHTML= artistCard


  


   

})();


const artistDeleteBtn = (id)=>{
    (async () => {

        let response = await fetch(`http://127.0.0.1:5000/artist/${id}`, {
          method: "DELETE",
          
          headers: {
            "Content-Type": "application/json",
    
          },
          
        });
        const result = await response.json();
    
        if(result.success){
            location.reload()
        }
      })();
}


(async () => {

    let response = await fetch("http://127.0.0.1:5000/show_theatre", {
        method: "GET",

        headers: {
            "Content-Type": "application/json",

        },

    });
    const result = await response.json();
    let theatreCard ="";
    result.theatre.map(element => {
            const name = element.name
             const theatreId = element.id
             const image = element.image_link
             theatreCard += ` <div class="card text-center" style="margin-top: 20px;" style="width: 18rem;">
            <div class="card-body">
              <img src="${image}" alt="theatre image"/>
              <h5 class="card-title">${name}</h5>
              <a href="#" class="btn btn-danger" id="delete-btn" onclick="theatreDeleteBtn(${theatreId})">Delete</a>
              <a href="#" class="btn btn-primary">Edit</a>
          
            </div>
          </div>`
    });
    document.getElementById('showTheatre').innerHTML= theatreCard


  


   

})();

const theatreDeleteBtn = (id)=>{
    (async () => {

        let response = await fetch(`http://127.0.0.1:5000/theatre/${id}`, {
          method: "DELETE",
          
          headers: {
            "Content-Type": "application/json",
    
          },
          
        });
        const result = await response.json();
    
        if(result.success){
            location.reload()
        }
      })();
}

(async () => {

    let response = await fetch("http://127.0.0.1:5000/landing", {
        method: "GET",

        headers: {
            "Content-Type": "application/json",

        },

    });
    const result = await response.json();
    let eventCard ="";
    result.events.map(element => {
            const name = element.name
            const descreption = element.description
            const image = element.image

             const eventId = element.id
            eventCard += ` <div class="card text-center" style="margin-top: 20px;" style="width: 18rem;">
            <div class="card-body">
              <img src="${image}" alt="event image"/>
              <h5 class="card-title">${name}</h5>
              <p class="card-text">${descreption}</p>
              <a href="#" class="btn btn-danger" id="delete-btn" onclick="eventeDeleteBtn(${eventId})">Delete</a>
              <a href="#" class="btn btn-primary">Edit</a>
          
            </div>
          </div>`
    });
    document.getElementById('showEvents').innerHTML= eventCard


  


   

})();
// const artistEditBtn = (id)=>{
//   (async () => {

//       let response = await fetch(`http://127.0.0.1:5000/artist/${id}`, {
//         method: "GET",
        
//         headers: {
//           "Content-Type": "application/json",
  
//         },
        
//       });
//       const result = await response.json();
  
//       if(result.success){
//          document.getElementById("Fname").value = result.fname;
//          document.getElementById("Lname").value = result.lname;
//          document.getElementById("ArtistAdress").value = result.address;
//          document.getElementById("AddImage").value = result.image_link;
//          document.getElementById("AddNumber").value = result.phone;
//          document.getElementById("AddDescreption").value = result.description;
//       }
//     })();
//   }
const eventeDeleteBtn = (id)=>{
    (async () => {

        let response = await fetch(`http://127.0.0.1:5000/event/${id}`, {
          method: "DELETE",
          
          headers: {
            "Content-Type": "application/json",
    
          },
          
        });
        const result = await response.json();
    
        if(result.success){
            location.reload()
        }
      })();
}

