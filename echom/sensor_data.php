<?php
// Database configuration
$host = 'localhost'; // Your database host
$username = 'root'; // Your database username
$password = ''; // Your database password
$database = 'RH'; // Your database name

// Create a connection to the database
$connection = new mysqli($host, $username, $password, $database);

// Check the connection
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

// Function to generate random pressure data
function generateRandomPressure() {
    // Generate a random pressure reading between 10 and 100
    return number_format(mt_rand(100, 1000) / 10.0, 2); // 10-100
}

// Insert random pressure data into the database
$pressure = generateRandomPressure();

$insertQuery = "INSERT INTO pressure_readings (pressure) VALUES ($pressure)";
if ($connection->query($insertQuery) === TRUE) {
    echo "New record created successfully!<br>";

    // Check if the pressure exceeds 70
    // Check if the pressure exceeds 70
if ($pressure > 70) {
    // Execute the Python script
    // Execute the Python script and redirect stderr to a log file
$command = "C:/Path/To/Python3.12/python.exe C:/Users/SNEGA/Desktop/echom/app.py";
$output = shell_exec($command);

file_put_contents('python_error.log', $output, FILE_APPEND); // Append output to log file

// Display output for debugging purposes
echo "message sent: $output<br>";

}

} else {
    echo "Error: " . $insertQuery . "<br>" . $connection->error . "<br>";
}

// Display the last 10 records from the database
$selectQuery = "SELECT * FROM pressure_readings ORDER BY timestamp DESC LIMIT 10";
$result = $connection->query($selectQuery);

if ($result->num_rows > 0) {
    echo "<table border='1'>";
    echo "<tr><th>ID</th><th>Pressure (hPa)</th><th>Timestamp</th></tr>";

    while ($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["id"] . "</td><td>" . $row["pressure"] . "</td><td>" . $row["timestamp"] . "</td></tr>";
    }
    echo "</table>";
} else {
    echo "No data found.";
}

// Close the database connection
$connection->close();
?>
