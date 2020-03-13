<?php
$artistError = $titleError = $formatError = $releaseDateError = $uploadError = $referenceError = " ";
$artist = $title = $format = $catalogNo = $releaseDate = $upload = $reference = " ";

//define variables per the HTML form
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $artist = $_POST['artist'];
  $title = $_POST['title'];
  $format = $_POST['format'];
  $catalogNo = $_POST['catalog-no'];
  $releaseDate = $_POST['release-date'];
  $source = $_POST['source'];
  $upload = $_POST['upload'];
  $reference = $_POST['reference'];
}

//protects against SQL injections and $_SERVER["PHP_SELF"] exploits
function sanitize_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

//required fields
if (empty($_POST["artist"])) {
  $artistError = "Required field";
} else {
  $artist = sanitize_input($_POST["artist"]);
}

if (empty($_POST["title"])) {
  $titleError = "Required field";
} else {
  $title = sanitize_input($_POST["title"]);
}

if (empty($_POST["format"])) {
  $formatError = "Must choose a format";

  if (empty($_POST["reference"])) {
    $referenceError = "Required field";
  } else {
    $title = sanitize_input($_POST["title"]);
    // check if URL address syntax is valid (this regular expression also allows dashes in the URL)
    if (!preg_match("/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i",$website)) {
      $websiteErr = "Invalid URL";
    }
  }
?>
