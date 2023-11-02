<!DOCTYPE html>
<html>
<head>
    <title>User Profile</title>
</head>
<body>
    <?php
    session_start(); // Start the session
    if (!isset($_SESSION['user_id'])) {
        header("Location: login.php"); // Redirect to login page if not logged in
        exit();
    }
    
    // Connect to the database
    $db = new mysqli('localhost', 'username', 'password', 'your_database_name');
    
    if ($db->connect_error) {
        die("Connection failed: " . $db->connect_error);
    }
    
    // Get the user's data from the database based on their user ID
    $user_id = $_SESSION['user_id'];
    $sql = "SELECT * FROM users WHERE id = ?";
    
    // Use a prepared statement to prevent SQL injection
    $stmt = $db->prepare($sql);
    $stmt->bind_param("i", $user_id);
    $stmt->execute();
    
    $result = $stmt->get_result();
    
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
    ?>
    
    <h1>Welcome, <?php echo htmlspecialchars($row['username']); ?></h1>
    
    <!-- Display user information -->
    <p><strong>Email:</strong> <?php echo htmlspecialchars($row['email']); ?></p>
    <p><strong>Name:</strong> <?php echo htmlspecialchars($row['name']); ?></p>
    
    <!-- Edit user information form -->
    <h2>Edit Profile</h2>
    <form action="update_profile.php" method="post">
        <label for="email">Email:</label>
        <input type="email" name="email" value="<?php echo htmlspecialchars($row['email']); ?>" required>
        
        <label for="name">Name:</label>
        <input type="text" name="name" value="<?php echo htmlspecialchars($row['name']); ?>" required>
        
        <input type="submit" value="Save Changes">
    </form>
    
    <?php
    } else {
        echo "User not found.";
    }
    
    // Close the database connection
    $stmt->close();
    $db->close();
    ?>
</body>
</html>
