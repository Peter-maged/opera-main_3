
document.getElementById("loginForm").onsubmit = function (event) {
    event.preventDefault();
    (async () => {
  
      let response = await fetch("http://127.0.0.1:5000/admin_login", {
        method: "POST",
        
        headers: {
          "Content-Type": "application/json",
  
        },
        body: JSON.stringify({
         email:document.getElementById('email').value.toString(),
         password:document.getElementById('password').value.toString()
        }),
      });
      const result = await response.json();
  
      if(result.success){
        window.location.href = "./home.html";
      }else{
          alert('Please check you email and password')
      }
    })();
  };