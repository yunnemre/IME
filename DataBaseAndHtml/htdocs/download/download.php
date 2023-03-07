<?php
#İndirilenler yönlendirilidiğine  database baglantı kurup öncelikle 30 gün önceki verileri siler
$mysqli = new mysqli("127.0.0.1", "root", "", "web");
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
$exec = $mysqli->query("DELETE FROM download WHERE DTarih <=  DATE_SUB(NOW(), INTERVAL 30 DAY) ");
?>
<!doctype html>
<html lang="tr" >
<head>
    <meta charset="utf-8">
    <title>İndirlenler</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<style>

    body{
        background-color:#eee;

    }
    .head{
        position:fixed;

        height:50px;
        width:200px;
        border:2px solid;
        border-color:transparent transparent black transparent;
        color:black;
        text-align:center;
        padding:10px;
        padding-left:30px;
        font-size:20px;

    }
    .icon{
        position: fixed;
        width: 30px;
        height:30px;
        top:7px;
        left:15px;
        background-image: url('../login/icons/tarayicilogo4.png');
        background-position:center;
        border-color:red;
        background-repeat: no-repeat;
        background-attachment: inherit;
        background-size: 30px;
        background-color: transparent;
    }
    <?php
        #Yuksekliğinni vermek için count ile hesap yapılır
        $date=date('Y-m-d');

        $exec = $mysqli->query("SELECT Count(*) FROM download WHERE DTarih ");
        $data=mysqli_fetch_assoc($exec);
        $count = $data["Count(*)"];

        $dctheigt= ($count*75)+75;

    ?>
    .mct{


        box-shadow: 0px -1px 2px 2px #444444;
        position: relative;
        width: 1017px;
        height:<?php echo $dctheigt ?>px;



        overflow-y:visible;

        border:1px solid;

        border-radius:15px;
        color:black;
        background-color: #eee;
        border-color: #eee  ;
    }


    .maindiv{
        position: relative;
        width: 1015px;
        height:75px;
        background-color: transparent;
        border:1px solid ;
        border-color: transparent transparent black transparent;
    }

    .mtime{
        position: relative;
        text-align:center;
        width: 150px;
        height:75px;
        top:22px;
        left:25px;
        background-color: transparent;
        color:black;
        text-decoration:none;

    }
    .mtime:hover{
        color:black;
    }

    .mdata{
        position: relative;
        float:right;
        width: 660px;
        height:75px;
        padding-top:22px;

        background-color: transparent;
        text-align:left;
        text-decoration:none;
        color:black;
    }

    .headertoday{

        position: relative;
        width: 1017px;
        height:52px;


    }

    .mct4{

        position: relative;
        width: 1017px;
        height:<?php echo $dctheigt ?>px;
        margin-bottom:200px;
        top:70px;
        left:250px;
        overflow-y:visible;
        border:1px solid;
        border-color: transparent;
        border-radius:15px;
        color:white;
        background-color: transparent;

    }

</style>
<body>
<!--İcon ve indirilenler tasarımı olustugu yer -->
<a href="download.php">
    <div class="head fw-bold " >İndirlenler
        <div class="icon"></div>

    </div>
</a>
<!--Hepsini içine kapsayak div -->
    <div class="mct4 vertical-menu">
        <!--İndirilenleri while döngüsüyle gösterilecegi yer -->
        <div class="mct vertical-menu">
            <div class="headertoday fw-bold" style="text-align:center;padding-top:12px;border:1px solid;
    border-top-left-radius:15px;
    border-top-right-radius:15px;
    border-color: #eee #eee black  #eee;">İndirilenler</div>
            <?php

            $sorgu = $mysqli->query("SELECT * FROM download WHERE DTarih ORDER BY DTarih DESC");
            while ($dcek=mysqli_fetch_assoc($sorgu)){

                ?>
                <a href="#" >
                    <div class="maindiv">

                        <a class="mtime" ><?php echo $dcek['DTarih'] ?> </a>
                        <a class="mdata"  href="C:/Users/Yunn/Downloads/"><?php echo $dcek['DName'] ?></a>

                    </div>
                </a>

            <?php }
            ?>
        </div>

        </div>


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</body>
</html>


