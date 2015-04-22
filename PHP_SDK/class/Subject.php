<?php

require_once("MyAPI.php");

class Subject extends MyAPI {
    /* Represent an unique person.
     * Constructor: take the UID of the DB
     */

    private $uid;

    function __construct ($uid) {
        $this->uid = $uid;
    }

    public function getUID () {
        return $this->uid;
    }    
    
    public function getFeatures() {
        return $this->get("features/user/".$this->uid);
    }

    public function getAttributes() {
        return $this->get("attributes/user/".$this->uid);
    }
}