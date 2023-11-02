<!DOCTYPE html>
<html>
<head>
    <title>Schedule an Appointment</title>
</head>
<body>
    <h1>Schedule an Appointment</h1>
    <form action="schedule_appointment.php" method="post">
        <label for="doctor">Select Doctor:</label>
        <select name="doctor" required>
            <?php
            // Connect to the database
            $db = new mysqli('localhost', 'username', 'password', 'your_database_name');
            
            if ($db->connect_error) {
                die("Connection failed: " . $db->connect_error);
            }
            
            // Retrieve the list of doctors and their specialties from the database
            $sql = "SELECT doctor_id, name, specialty FROM doctors";
            $result = $db->query($sql);
            
            // Generate select options based on the doctor data, including both name and specialty
            if ($result->num_rows > 0) {
                while ($row = $result->fetch_assoc()) {
                    $doctor_option = $row['name'] . " (" . $row['specialty'] . ")";
                    echo "<option value='" . htmlspecialchars($doctor_option) . "'>" . htmlspecialchars($doctor_option) . "</option>";
                }
            }
            ?>
        </select>
        
        <label for="date">Appointment Date:</label>
        <input type="date" name="date" required>
        
        <label for="time">Appointment Time:</label>
        <input type="time" name="time" required>
        
        <label for="comments">Additional Comments (optional):</label>
        <textarea name="comments" rows="4" cols="50"></textarea>
        
        <input type="submit" value="Schedule Appointment">
    </form>
</body>
</html>
