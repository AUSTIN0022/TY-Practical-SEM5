<!DOCTYPE html>
<html>
<head>
    <title>Student Data</title>
</head>
<body>
    <h1>Student Data</h1>

    <table border="1">
        <tr>
            <th>Roll No</th>
            <th>Name</th>
            <th>OS</th>
            <th>WT</th>
            <th>DS</th>
            <th>Python</th>
            <th>Java</th>
            <th>CN</th>
            <th>Percentage</th>
        </tr>

        <?php
        // Open the student.dat file for reading
        $file = fopen("student.dat", "r");

        if ($file) {
            while (!feof($file)) {
                $line = fgets($file);
                $data = explode(",", $line);
                if (count($data) == 8) {
                    list($rollno, $name, $os, $wt, $ds, $python, $java, $cn) = $data;

                    // Calculate the percentage
                    $total = $os + $wt + $ds + $python + $java + $cn;
                    $percentage = ($total / 600) * 100;

                    echo "<tr>";
                    echo "<td>$rollno</td>";
                    echo "<td>$name</td>";
                    echo "<td>$os</td>";
                    echo "<td>$wt</td>";
                    echo "<td>$ds</td>";
                    echo "<td>$python</td>";
                    echo "<td>$java</td>";
                    echo "<td>$cn</td>";
                    echo "<td>$percentage%</td>";
                    echo "</tr>";
                }
            }
            fclose($file);
        } else {
            echo "Unable to open the file.";
        }
        ?>
    </table>
</body>
</html>
