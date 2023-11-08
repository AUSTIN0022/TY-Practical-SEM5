<?php
// Connect to the PostgreSQL database
$db = pg_connect("host=localhost port=5432 dbname=doctor user=postgres password=makasare0031");

if (!$db) {
    die("Error in database connection: " );
}
// Get the hospital name from the user
$hospitalName = $_POST['hospitalName']; // Assuming you're using a POST request
// Prepare and execute the SQL query to fetch doctors visiting the specified hospital
$query = "SELECT d.dname, d.address, d.city, d.area
          FROM doctor d
          JOIN hospital h ON d.hosp_no = h.hosp_no
          WHERE h.hname = '$hospitalName'";

$result = pg_query($db, $query);

if (!$result) {
    die("Error in SQL query: ");
}

// Print the results in tabular format
echo "<table border=1>";
echo "<tr><th>Doctor Name</th><th>Address</th><th>City</th><th>Area</th></tr>";

while ($row = pg_fetch_assoc($result)) {
    echo "<tr>";
    echo "<td>" . $row['dname'] . "</td>";
    echo "<td>" . $row['address'] . "</td>";
    echo "<td>" . $row['city'] . "</td>";
    echo "<td>" . $row['area'] . "</td>";
    echo "</tr>";
}

echo "</table>";

// Close the database connection
pg_close($db);
?>
