<?php
$artistError = $titleError = $formatError = $catalogNoError = $releaseDateError = $uploadError = " ";
$artist = $title = $format = $catalogNo = $releaseDate = $upload = " ";

//define variables per the HTML form
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $artist = $_POST['artist'];
  $title = $_POST['title'];
  $format = $_POST['format'];
  $catalogNo = $_POST['catalog-no'];
  $releaseDate = $_POST['release-date'];
  $source = $_POST['source'];
  $upload = $_POST['upload'];
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
  $artist = test_input($_POST["artist"]);
}

if (empty($_POST["title"])) {
  $titleError = "Required field";
} else {
  $title = test_input($_POST["title"]);
}

if (empty($_POST["format"])) {
  $formatError = "Must choose a format";
