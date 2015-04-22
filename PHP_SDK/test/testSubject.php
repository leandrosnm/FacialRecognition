<?php

require_once("../class/Subject.php");

$id = "627575";

$mySubject = new Subject($id);

echo $mySubject->getUID()."\n";
print_r($mySubject->getFeatures());
print_r($mySubject->getAttributes());

?>