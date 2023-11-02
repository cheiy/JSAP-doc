<?php
session_start(); // Start the session
if (!isset($_SESSION['user_id'])) {
    header("Location: login.html"); // Redirect to login page if not logged in
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Connect to the database
    $db = new mysqli('localhost', 'username', 'password', 'your_database_name');
    
    if ($db->connect_error) {
        die("Connection failed: " . $db->connect_error);
    }
    
    $user_id = $_SESSION['user_id'];
    $newEmail = $_POST['email'];
    $newName = $_POST['name'];
    
    // Update the user's information in the database
    $sql = "UPDATE users SET email = ?, name = ? WHERE id = ?";
    
    // Use a prepared statement to prevent SQL injection
    $stmt = $db->prepare($sql);
    $stmt->bind_param("ssi", $newEmail, $newName, $user_id);
    
    if ($stmt->execute()) {
        header("Location: profile.php"); // Redirect to the profile page after successful update
        exit();
    } else {
        echo "Update failed: " . $db->error;
    }
    
    $stmt->close();
    $db->close();
}
