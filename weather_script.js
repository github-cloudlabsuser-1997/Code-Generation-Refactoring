const fetch = require('node-fetch');

async function getWeatherByLocation(city) {
    const apiKey = '1e97fe13f9ec69d26e055401f5e053bf'; // Replace with your API key
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }
        const weatherData = await response.json();
        console.log(`Weather in ${city}:`);
        console.log(`Temperature: ${weatherData.main.temp}°C`);
        console.log(`Description: ${weatherData.weather[0].description}`);
    } catch (error) {
        console.error('Failed to fetch weather data:', error.message);
    }
}

// Example usage
const city = 'London'; // Replace with your desired city
getWeatherByLocation(city);