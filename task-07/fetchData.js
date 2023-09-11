const API_key = 'e4f273e6c4c93188f9964501de66d735';

window.onload = function () {
    // Function to fetch weather data by coordinates
    function fetchWeatherByCoordinates(latitude, longitude) {
        fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&units=metric&appid=${API_key}`)
            .then((data) => data.json())
            .then((jsonData) => {
                if (jsonData.weather && jsonData.weather.length > 0) {
                    // Ensure that jsonData.weather is an array with at least one element

                    // You can now safely access properties of jsonData.weather[0]
                    document.getElementById("text_location").innerHTML = jsonData.name;
                    document.getElementById("text_location_country").innerHTML = jsonData.sys.country;
                    document.getElementById("text_temp").innerHTML = Math.round(jsonData.main.temp);
                    document.getElementById("text_feelslike").innerHTML = Math.round(jsonData.main.feels_like);
                    document.getElementById("text_desc").innerHTML = jsonData.weather[0].description;

                    fetch(`https://openweathermap.org/img/wn/${jsonData.weather[0].icon}.png`)
                        .then((res) => {
                            if (!res.ok) {
                                throw new Error(`Failed to fetch icon: ${res.status} ${res.statusText}`);
                            }
                            return res.blob();
                        })
                        .then((result) => {
                            const imageObjectURL = URL.createObjectURL(result);
                            document.getElementById("icon").src = imageObjectURL;
                        })
                        .catch((error) => {
                            console.error("Error fetching weather icon:", error);
                        });
                }
            })
            .catch((error) => {
                console.error("Error fetching weather data:", error);
            });
    }

    // Function to fetch weather data by city name
    function fetchWeatherByCity(cityName) {
        fetch(`https://api.openweathermap.org/data/2.5/weather?q=${cityName}&units=metric&appid=${API_key}`)
            .then((data) => data.json())
            .then((jsonData) => {
                if (jsonData.weather && jsonData.weather.length > 0) {
                    // Ensure that jsonData.weather is an array with at least one element

                    // You can now safely access properties of jsonData.weather[0]
                    document.getElementById("text_location").innerHTML = jsonData.name;
                    document.getElementById("text_location_country").innerHTML = jsonData.sys.country;
                    document.getElementById("text_temp").innerHTML = Math.round(jsonData.main.temp);
                    document.getElementById("text_feelslike").innerHTML = Math.round(jsonData.main.feels_like);
                    document.getElementById("text_desc").innerHTML = jsonData.weather[0].description;

                    fetch(`https://openweathermap.org/img/wn/${jsonData.weather[0].icon}.png`)
                        .then((res) => {
                            if (!res.ok) {
                                throw new Error(`Failed to fetch icon: ${res.status} ${res.statusText}`);
                            }
                            return res.blob();
                        })
                        .then((result) => {
                            const imageObjectURL = URL.createObjectURL(result);
                            document.getElementById("icon").src = imageObjectURL;
                        })
                        .catch((error) => {
                            console.error("Error fetching weather icon:", error);
                        });
                }
            })
            .catch((error) => {
                console.error("Error fetching weather data:", error);
            });
    }

    // Get the city input element
    const cityInput = document.getElementById("cityInput");

    // Get the Get Weather button element
    const getWeatherButton = document.getElementById("getWeatherButton");

    // Add event listener to Get Weather button
    getWeatherButton.addEventListener("click", function () {
        const cityName = cityInput.value;
        if (cityName) {
            fetchWeatherByCity(cityName);
        }
    });

    // Add event listener to the city input for pressing Enter
    cityInput.addEventListener("keyup", function (event) {
        if (event.key === "Enter") {
            const cityName = cityInput.value;
            if (cityName) {
                fetchWeatherByCity(cityName);
            }
        }
    });

    // Get the user's coordinates and fetch weather data for the user's location
    navigator.geolocation.getCurrentPosition(function (position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        fetchWeatherByCoordinates(latitude, longitude);
    });
};
