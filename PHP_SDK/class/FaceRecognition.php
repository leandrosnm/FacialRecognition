<?php

require_once("MyAPI.php");

class FaceRecognition extends MyAPI {

    private $imageUrl;
    private $tempID;
    private $candidates = array();

    function __construct ($imageUrl) {
        $this->imageUrl = $imageUrl;
    }

    public function match () {
        $jsonResp = $this->get("match?imageUrl=".$this->imageUrl);
        $this->candidates = $jsonResp["candidates"];
        $this->tempID = $jsonResp["tempID"];
    }

    public function getImageUrl () {
        return $this->imageUrl;
    }

    public function getCandidates () {
        return $this->candidates;
    }    
    
    public function getFeatures() {
        return $this->get("features/temp/".$this->tempID);
    }

    public function getAttributes() {
        return $this->get("attributes/temp/".$this->tempID);
    }
}