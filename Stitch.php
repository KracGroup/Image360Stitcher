<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="icon" href="img/favicon.png" type="image/png">
        <title>IMAGE360</title>
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="css/bootstrap.css">
        <link rel="stylesheet" href="vendors/linericon/style.css">
        <link rel="stylesheet" href="css/font-awesome.min.css">
        <link rel="stylesheet" href="vendors/owl-carousel/owl.carousel.min.css">
        <link rel="stylesheet" href="vendors/lightbox/simpleLightbox.css">
        <link rel="stylesheet" href="vendors/nice-select/css/nice-select.css">
        <link rel="stylesheet" href="vendors/animate-css/animate.css">
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <!-- main css -->
        <link rel="stylesheet" href="css/style.css">
        <link rel="stylesheet" href="css/responsive.css">
    </head>
<style>
.button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

.button2 {background-color: #008CBA;} /* Blue */
.button3 {background-color: #f44336;} /* Red */ 
.button4 {background-color: #e7e7e7; color: black;} /* Gray */ 
.button5 {background-color: #555555;} /* Black */
</style>
<body>

<?php
if(is_uploaded_file($_FILES['file1']['tmp_name']) && is_uploaded_file($_FILES['file2']['tmp_name']) && is_uploaded_file($_FILES['file3']['tmp_name'])){
$file01=$_FILES['file1']['name'];
$file02=$_FILES['file2']['name'];
$file03=$_FILES['file3']['name'];
#$file04=$_FILES['file4']['name'];
$filestore1="C:/xampp/htdocs/Project/Python-Multiple-Image-Stitching-master/images/".$file01;
$filestore2="C:/xampp/htdocs/Project/Python-Multiple-Image-Stitching-master/images/".$file02;
$filestore3="C:/xampp/htdocs/Project/Python-Multiple-Image-Stitching-master/images/".$file03;
#$filestore4="C:/xampp/htdocs/Project/Python-Multiple-Image-Stitching-master/images/".$file04;
$file_tem_loc1=$_FILES['file1']['tmp_name'];
$file_tem_loc2=$_FILES['file2']['tmp_name'];
$file_tem_loc3=$_FILES['file3']['tmp_name'];
#$file_tem_loc4=$_FILES['file4']['tmp_name'];
move_uploaded_file($file_tem_loc1,$filestore1);
move_uploaded_file($file_tem_loc2,$filestore2);
move_uploaded_file($file_tem_loc3,$filestore3);
#move_uploaded_file($file_tem_loc4,$filestore4);
$filename="C:/xampp/htdocs/Project/Python-Multiple-Image-Stitching-master/code/txtlists/Files1.txt";
file_put_contents($filename, "../images/".$file01."\r\n../images/".$file02."\r\n../images/".$file03);
}
if(is_uploaded_file($_FILES['file1']['tmp_name']) && is_uploaded_file($_FILES['file2']['tmp_name']) && !is_uploaded_file($_FILES['file3']['tmp_name']))
{
$file01=$_FILES['file1']['name'];
$file02=$_FILES['file2']['name'];
$filestore1="C:/xampp/htdocs/Project/Python-Multiple-Image-Stitching-master/images/".$file01;
$filestore2="C:/xampp/htdocs/Project/Python-Multiple-Image-Stitching-master/images/".$file02;
$file_tem_loc1=$_FILES['file1']['tmp_name'];
$file_tem_loc2=$_FILES['file2']['tmp_name'];
move_uploaded_file($file_tem_loc1,$filestore1);
move_uploaded_file($file_tem_loc2,$filestore2);
$filename="C:/xampp/htdocs/Project/Python-Multiple-Image-Stitching-master/code/txtlists/Files1.txt";
file_put_contents($filename, "../images/".$file01."\r\n../images/".$file02);	
}
?>

<header class="header_area">
            <nav class="navbar navbar-expand-lg navbar-light">
                <div class="container box_1620">
                    <!-- Brand and toggle get grouped for better mobile display -->
                    <a class="navbar-brand logo_h" href="http://localhost/Project/Image360/"><i class="fa fa-camera" style="font-size:25px;color:white" align="right" style><font style="font-family:Cursive;" >Image360</font></i>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <!-- Collect the nav links, forms, and other content for toggling -->
                    <div class="collapse navbar-collapse offset" id="navbarSupportedContent">
                        <ul class="nav navbar-nav menu_nav ml-auto">
                            <li class="nav-item active"><a class="nav-link" href="http://localhost/Project/Image360/">Home</a></li> 
                            
                            <li class="nav-item"><a class="nav-link" href="http://localhost/Project/Image360/service.html">Services</a></li>
                            <li class="nav-item"><a class="nav-link" href="http://localhost/Project/Image360/about-us.html">About</a></li>
                           
                            
                            
          
                     </ul>
                        <ul class="nav navbar-nav navbar-right">
                            <li class="nav-item"><a href="#" class="search"><i class="lnr lnr-magnifier"></i></a></li>
                        </ul>
                    </div> 
                </div>
            </nav>
        </header>
<section class="testimonials_area p_120">
        	<div class="container">
        		<div class="row testimonials_inner">
        			<div class="col-lg-6">
        				<div class="c_feedback_text">
        					<h2>Are You Sure?</h2>
        					<button class="button"><a href="http://localhost/Project/Python-Multiple-Image-Stitching-master/code/pano.py"  style="color:white" >Stitch</a></button>
							<button class="button button3"> <a href="http://localhost/Project/Image360/service.html"  style="color:white" >Go Back</a></button>
							
        				</div>
        			</div>
        			
        		</div>
        	</div>
        </section>
		<footer class="footer_area p_120">
        	<div class="container">
        		<div class="row footer_inner">
        			<div class="col-lg-5 col-sm-6">
        				<aside class="f_widget ab_widget">
        					<div class="f_title">
        						<h3>About US</h3>
        					</div>
        					<p>Free Website to Upload & Download your different images covering different aspects into single image</p>
        					<p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This Website is made with <i class="fa fa-heart-o" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">KRAC</a>
<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
        				</aside>
        			</div>
        			<div class="col-lg-5 col-sm-6">
        				<aside class="f_widget news_widget">
        					<div class="f_title">
        						<h3>Newsletter</h3>
        					</div>
        					<p>Stay updated with our latest trends</p>
        					<div id="mc_embed_signup">
                                <form target="_blank" action="https://spondonit.us12.list-manage.com/subscribe/post?u=1462626880ade1ac87bd9c93a&amp;id=92a4423d01" method="get" class="subscribe_form relative">
                                	<div class="input-group d-flex flex-row">
                                        <input name="EMAIL" placeholder="Enter email address" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Email Address '" required="" type="email">
                                        <button class="btn sub-btn"><span class="lnr lnr-arrow-right"></span></button>		
                                    </div>				
                                    <div class="mt-10 info"></div>
                                </form>
                            </div>
        				</aside>
        			</div>
        			<div class="col-lg-2">
        				<aside class="f_widget social_widget">
        					<div class="f_title">
        						<h3>Follow US</h3>
        					</div>
        					<p>Let us be social</p>
        					<ul class="list">
        						<li><a href="#"><i class="fa fa-facebook"></i></a></li>
        						<li><a href="#"><i class="fa fa-twitter"></i></a></li>
        						<li><a href="#"><i class="fa fa-dribbble"></i></a></li>
        						<li><a href="#"><i class="fa fa-behance"></i></a></li>
        					</ul>
        				</aside>
        			</div>
        		</div>
        	</div>
        </footer>
		</body>
		</html>