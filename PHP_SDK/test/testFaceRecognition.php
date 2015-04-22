<?php

require_once("../class/FaceRecognition.php");

$url = "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpf1/t31.0-1/10989226_10101668300439347_4318759549674621882_o.jpg";

$face = new FaceRecognition($url);
$face->match();

echo $face->getImageUrl()."\n";
print_r($face->getCandidates());
print_r($face->getFeatures());
print_r($face->getAttributes());

?>