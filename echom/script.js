document.addEventListener("DOMContentLoaded", function() {
    const signInBtn = document.getElementById("signinBtn");

    const enableSignIn = () => {
        signInBtn.removeAttribute("disabled");
        signInBtn.classList.add("enabled");
        signInBtn.innerText = "Sign In";
    };

    const getlocation = () => {
        if (navigator.geolocation){
            navigator.geolocation.getCurrentPosition(showPosition, showError);
        } else {
            alert("Geolocation is not supported by this browser");
        }
    };

    const showPosition = (position) => {
        let lat = position.coords.latitude;
        let long = position.coords.longitude;
        const des = document.querySelector("p");
        des.innerHTML = `Latitude: ${lat}<br>Longitude: ${long}`;
        enableSignIn();
    };

    const showError = (error) => {
        switch (error.code) {
            case error.PERMISSION_DENIED:
                alert("User denied the request for geolocation.");
                break;
            case error.POSITION_UNAVAILABLE:
                alert("Location information is unavailable.");
                break;
            case error.TIMEOUT:
                alert("The request to get user location timed out.");
                break;
            default:
                alert("An Unknown Error occurred");
        }
    };

    getlocation();
});
