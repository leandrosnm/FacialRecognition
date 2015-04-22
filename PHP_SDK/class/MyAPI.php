<?php

define ("BASE_URL","http://172.31.20.220:5000/");

class MyAPI {
    public function get($uri) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, BASE_URL.$uri);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $jsonResponse = curl_exec($ch);
        curl_close($ch);   

        return json_decode($jsonResponse,true);
    }
}

?>
