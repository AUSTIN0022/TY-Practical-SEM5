<?php
    // Connect to the PostgreSQL database
    $conn = pg_connect("host=localhost port=5432 dbname=event_committee user=postgres password=makasare0031");

    if (!$conn) {
        die("Failed to connect to the database");
    }

    $eventName = $_POST['event_name'];
    // Task 1: Fetch and display event details from the committee table
    $query1 = "SELECT * FROM committee WHERE name = '$eventName'";
    $result1 = pg_query($conn, $query1);
   
    echo "<h2>Event Details</h2>";
    if (pg_num_rows($result1) > 0) {
        echo "<table border='1'>";
        echo "<tr><th>Committee Name</th><th>Committee Head</th><th>From Time</th><th>To Time</th><th>Status</th></tr>";

        while ($row = pg_fetch_assoc($result1)) {
            echo "<tr>";
            echo "<td>" . $row['name'] . "</td>";
            echo "<td>" . $row['head'] . "</td>";
            echo "<td>" . $row['from_time'] . "</td>";
            echo "<td>" . $row['to_time'] . "</td>";
            echo "<td>" . $row['status'] . "</td>";
            echo "</tr>";
        }

        echo "</table>";
    } else {
        echo "Event not found in the committee table.";
    }
    // Task 2: Update the committee status to "working"
    $query2 = "UPDATE committee SET status = 'working' WHERE name = '$eventName'";
    $result2 = pg_query($conn, $query2);
 
    // Task 3: Fetch and display updated event details
    $query3 = "SELECT * FROM committee WHERE name = '$eventName'";
    $result3 = pg_query($conn, $query3);
    
    echo "<h2>Updated Event Details</h2>";
    if (pg_num_rows($result3) > 0) {
        echo "<table border='1'>";
        echo "<tr><th>Committee Name</th><th>Committee Head</th><th>From Time</th><th>To Time</th><th>Status</th></tr>";

        while ($row = pg_fetch_assoc($result3)) {
            echo "<tr>";
            echo "<td>" . $row['name'] . "</td>";
            echo "<td>" . $row['head'] . "</td>";
            echo "<td>" . $row['from_time'] . "</td>";
            echo "<td>" . $row['to_time'] . "</td>";
            echo "<td>" . $row['status'] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "Event not found in the committee table after update.";
    }
    pg_close($conn);// Close the database connection
?>