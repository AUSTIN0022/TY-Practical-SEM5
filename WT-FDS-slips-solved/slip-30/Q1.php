<?php
// Connect to the PostgreSQL database
$conn = pg_connect("host=localhost port=5432 dbname=students user=postgres password=makasare0031");

if (!$conn) {
    die("Failed to connect to the database");
}
// Get the competition name from the user
$comp_Name = $_POST['cname'];

// Query to retrieve the student with 1st rank in the specified competition
$query = "SELECT s.name, s.class, r.year
          FROM Student s
          JOIN Rank r ON s.Stud_id = r.stud_id
          pJOIN Competition c ON r.c_no = c.c_no
          WHERE c.c_name = '$comp_Name' AND r.rank = 1";

$result = pg_query($conn, $query);

if (!$result) {
    die("Query failed");
}
// Display the results
while ($row = pg_fetch_array($result)) {
    echo "Student Name: " . $row['name'] . "<br>";
    echo "Student Class: " . $row['class'] . "<br>";
    echo "Year: " . $row['year'] . "<br><br>";
}
// Close the database connection
pg_close($conn);
?>