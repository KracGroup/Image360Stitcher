#!C:\Python27\python.exe
print "Content-Type: text/html\r\n"
import numpy as np
import cv2
import sys
from matchers import matchers
import time
import random
import string
class Stitch:
	def __init__(self, args):
		self.path = args
		fp = open(self.path, 'r')
		filenames = [each.rstrip('\r\n') for each in  fp.readlines()]
		#print filenames
		self.images = [cv2.resize(cv2.imread(each),(480, 320)) for each in filenames]
		self.count = len(self.images)
		self.left_list, self.right_list, self.center_im = [], [],None
		self.matcher_obj = matchers()
		self.prepare_lists()

	def prepare_lists(self):
		#print "Number of images : %d"%self.count
		self.centerIdx = self.count/2 
		#print "Center index image : %d"%self.centerIdx
		self.center_im = self.images[int(self.centerIdx)]
		for i in range(self.count):
			if(i<=self.centerIdx):
				self.left_list.append(self.images[i])
			else:
				self.right_list.append(self.images[i])
		#print "Image lists prepared"

	def leftshift(self):
		# self.left_list = reversed(self.left_list)
		a = self.left_list[0]
		for b in self.left_list[1:]:
			H = self.matcher_obj.match(a, b, 'left')
			#print "Homography is : ", H
			xh = np.linalg.inv(H)
			#print "Inverse Homography :", xh
			ds = np.dot(xh, np.array([a.shape[1], a.shape[0], 1]));
			ds = ds/ds[-1]
			#print "final ds=>", ds
			f1 = np.dot(xh, np.array([0,0,1]))
			f1 = f1/f1[-1]
			xh[0][-1] += abs(f1[0])
			xh[1][-1] += abs(f1[1])
			ds = np.dot(xh, np.array([a.shape[1], a.shape[0], 1]))
			offsety = abs(int(f1[1]))
			offsetx = abs(int(f1[0]))
			dsize = (int(ds[0])+offsetx, int(ds[1]) + offsety)
			#print "image dsize =>", dsize
			tmp = cv2.warpPerspective(a, xh, dsize)
			# cv2.imshow("warped", tmp)
			# cv2.waitKey()
			tmp[offsety:b.shape[0]+offsety, offsetx:b.shape[1]+offsetx] = b
			a = tmp

		self.leftImage = tmp

		
	def rightshift(self):
		for each in self.right_list:
			H = self.matcher_obj.match(self.leftImage, each, 'right')
			#print "Homography :", H
			txyz = np.dot(H, np.array([each.shape[1], each.shape[0], 1]))
			txyz = txyz/txyz[-1]
			dsize = (int(txyz[0])+self.leftImage.shape[1], int(txyz[1])+self.leftImage.shape[0])
			tmp = cv2.warpPerspective(each, H, dsize)
			cv2.imshow("tp", tmp)
			cv2.waitKey()
			# tmp[:self.leftImage.shape[0], :self.leftImage.shape[1]]=self.leftImage
			tmp = self.mix_and_match(self.leftImage, tmp)
			#print "tmp shape",tmp.shape
			#print "self.leftimage shape=", self.leftImage.shape
			self.leftImage = tmp
		# self.showImage('left')



	def mix_and_match(self, leftImage, warpedImage):
		i1y, i1x = leftImage.shape[:2]
		i2y, i2x = warpedImage.shape[:2]
		#print leftImage[-1,-1]

		t = time.time()
		black_l = np.where(leftImage == np.array([0,0,0]))
		black_wi = np.where(warpedImage == np.array([0,0,0]))
		#print time.time() - t
		#print black_l[-1]

		for i in range(0, i1x):
			for j in range(0, i1y):
				try:
					if(np.array_equal(leftImage[j,i],np.array([0,0,0])) and  np.array_equal(warpedImage[j,i],np.array([0,0,0]))):
						# print "BLACK"
						# instead of just putting it with black, 
						# take average of all nearby values and avg it.
						warpedImage[j,i] = [0, 0, 0]
					else:
						if(np.array_equal(warpedImage[j,i],[0,0,0])):
							# print "PIXEL"
							warpedImage[j,i] = leftImage[j,i]
						else:
							if not np.array_equal(leftImage[j,i], [0,0,0]):
								bw, gw, rw = warpedImage[j,i]
								bl,gl,rl = leftImage[j,i]
								# b = (bl+bw)/2
								# g = (gl+gw)/2
								# r = (rl+rw)/2
								warpedImage[j, i] = [bl,gl,rl]
				except:
					pass
		# cv2.imshow("waRPED mix", warpedImage)
		# cv2.waitKey()
		return warpedImage




	def trim_left(self):
		pass

	def showImage(self, string=None):
		if string == 'left':
			cv2.imshow("left image", self.leftImage)
			# cv2.imshow("left image", cv2.resize(self.leftImage, (400,400)))
		elif string == "right":
			cv2.imshow("right Image", self.rightImage)
		cv2.waitKey()


if __name__ == '__main__':
	try:
		args = sys.argv[1]
	except:
		args = "txtlists/files1.txt"
	finally:
		print " "
	s = Stitch(args)
	s.leftshift()
	# s.showImage('left')
	s.rightshift()
	#print "done"
	chars = "".join( [random.choice(string.letters) for i in xrange(15)] )
	file=chars+".jpg"
	cv2.imwrite(file, s.leftImage)
	wrapper = """<html>
    <head>
    <title>IMAGE360</title>
    </head>
    <body><p>Stitched Please Download: <a href=\"%s\" download>%s</a></p>
	<p>Go Back:<a href="http://localhost/Project/Image360/">GO BACK</a></p>
	</body>
    </html>"""
	whole = wrapper % (file,'Download')
	wrapper1= """<html lang="en">
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
	#ABC {
    background-color: #800080;
    }
    </style></head>
    <body>
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
	<section class="service_area p_120" id="ABC">
	<div class="container">
	<div class="row service_inner">
    <div class="col-lg-4 col-md-6">
    <div class="service_item">
    <i class="lnr lnr-download"></i>
	<a href=\"%s\" download><h4 style="color:white">Download</h4></a>
	</div>
    </div>
    </div>
    </div>
	<br>
	<div class="container">
    <div class="row service_inner">
    <div class="col-lg-4 col-md-6">
    <div class="service_item">
    <i class="lnr lnr-arrow-left"></i>
	<a href="http://localhost/Project/Image360/"><h4 style="color:white">GoBack</h4></a>
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
    <p>Free Website to Upload & Download your different images covering different aspects into single image </p>
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
    <!--================End Footer Area =================-->
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="js/jquery-3.2.1.min.js"></script>
    <script src="js/popper.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/stellar.js"></script>
    <script src="vendors/lightbox/simpleLightbox.min.js"></script>
    <script src="vendors/nice-select/js/jquery.nice-select.min.js"></script>
    <script src="vendors/isotope/imagesloaded.pkgd.min.js"></script>
    <script src="vendors/isotope/isotope-min.js"></script>
    <script src="vendors/owl-carousel/owl.carousel.min.js"></script>
    <script src="js/jquery.ajaxchimp.min.js"></script>
    <script src="js/mail-script.js"></script>
    <script src="js/theme.js"></script>
    </body>
    </html>
	"""
	whole1 = wrapper1 % (file)
	#print "image written\n"
	#print "\nIMAGE STITCHED PLEASE DOWNLOAD BY CLICKING LINK:"
	#link = """<a href="{}" download>{}</a>""".format(file, 'Download')
	#print link
	#print """<br>"""
	#print "\nGO BACK:"
	#print """<a href="http://localhost/Project/Image360/">GO BACK</a>"""
	print whole1
	cv2.destroyAllWindows()
	
