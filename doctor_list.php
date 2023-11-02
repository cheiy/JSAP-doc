<!DOCTYPE html>
<html>
<head>
    <title>List of Doctors</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #3498db;
            color: #fff;
            text-align: center;
            padding: 20px;
        }
        h1 {
            margin: 20px 0;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background-color: #fff;
            margin: 10px;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <header>
        <h1>List of Doctors</h1>
    </header>
    <div class="container">
        <ul>
            <?php
            // Connect to the database
            $db = new mysqli('localhost', 'username', 'password', 'your_database_name');

            if ($db->connect_error) {
                die("Connection failed: " . $db->connect_error);
            }

            // Retrieve the list of doctors from the database
            $sql = "SELECT name, specialty, contact FROM doctors";
            $result = $db->query($sql);

            // Check if there are any doctors
            if ($result->num_rows > 0) {
                while ($row = $result->fetch_assoc()) {
                    echo "<li>";
                    echo "<h2>" . htmlspecialchars($row['name']) . "</h2>";
                    echo "<p>Specialty: " . htmlspecialchars($row['specialty']) . "</p>";
                    echo "<p>Contact: " . htmlspecialchars($row['contact']) . "</p>";
                    echo "</li>";
                }
            } else {
                echo "No doctors found in the database.";
            }

            // Close the database connection
            $db->close();
            ?>
        </ul>
    </div>
</body>
</html>
