<!DOCTYPE html>
<html>
<head>
    <title>Your Appointments</title>
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
        <h1>Your Appointments</h1>
    </header>
    <div class="container">
        <ul>
            <?php
            // Connect to the database
            $db = new mysqli('localhost', 'username', 'password', 'your_database_name');

            if ($db->connect_error) {
                die("Connection failed: " . $db->connect_error);
            }

            // Retrieve the user's scheduled appointments from the database
            session_start();
            $user_id = $_SESSION['user_id'];
            $sql = "SELECT a.appointment_date, d.name, d.specialty FROM appointments a
                    JOIN doctors d ON a.doctor_id = d.doctor_id
                    WHERE a.user_id = $user_id";
            $result = $db->query($sql);

            // Check if there are any appointments
            if ($result->num_rows > 0) {
                while ($row = $result->fetch_assoc()) {
                    echo "<li>";
                    echo "<h2>Doctor: " . htmlspecialchars($row['name']) . "</h2>";
                    echo "<p>Specialty: " . htmlspecialchars($row['specialty']) . "</p>";
                    echo "<p>Appointment Date: " . htmlspecialchars($row['appointment_date']) . "</p>";
                    echo "</li>";
                }
            } else {
                echo "You have no scheduled appointments.";
            }

            // Close the database connection
            $db->close();
            ?>
        </ul>
    </div>
</body>
</html>
