$(document).ready(function() {
	'use strict';
	/*-----------------------------------------------------------------------------------*/
	/*	STICKY HEADER
	/*-----------------------------------------------------------------------------------*/
	if ($(".navbar").length) {
		var options = {
			offset: 350,
			offsetSide: 'top',
			classes: {
				clone: 'banner--clone fixed',
				stick: 'banner--stick',
				unstick: 'banner--unstick'
			},
			onStick: function() {
				$($.SmartMenus.Bootstrap.init);
				var $language_dropdown = $('.navbar:not(.fixed) .language-select .dropdown-menu');
				$language_dropdown.removeClass('show');
			},
			onUnstick: function() {
				var $language_sticky_dropdown = $('.navbar.fixed .language-select .dropdown-menu');
				$language_sticky_dropdown.removeClass('show');
			}
		};
		var banner = new Headhesive('.navbar', options);
	}
	$(function() {
		$('.navbar .navbar-nav:not(.navbar-nav-other)').bind({
			'show.smapi': function(e, menu) {
				$(menu).removeClass('hide-animation').addClass('show-animation');
			},
			'hide.smapi': function(e, menu) {
				$(menu).removeClass('show-animation').addClass('hide-animation');
			}
		}).on('animationend webkitAnimationEnd oanimationend MSAnimationEnd', 'ul', function(e) {
			$(this).removeClass('show-animation hide-animation');
			e.stopPropagation();
		});
	});
	/*-----------------------------------------------------------------------------------*/
	/*	HEADER BUTTONS
	/*-----------------------------------------------------------------------------------*/
	var $header_hamburger = $('.hamburger.animate');
	var $language_select = $('.language-select .dropdown-menu');
	var $header_cart = $('.cart-dropdown .dropdown-menu');
	var $navbar_offcanvas = $('.offcanvas-nav');
	var $navbar_offcanvas_toggle = $('[data-toggle="offcanvas-nav"]');
	var $navbar_offcanvas_close = $('.offcanvas-nav-close');
	var $info_offcanvas = $('.offcanvas-info');
	var $info_offcanvas_close = $('.offcanvas-info-close');
	var $info_offcanvas_toggle = $('[data-toggle="offcanvas-info"]');
	$header_hamburger.on("click", function() {
		$header_hamburger.toggleClass("active");
	});
	$navbar_offcanvas_toggle.on("click", function(e) {
		e.stopPropagation();
		$navbar_offcanvas.toggleClass('open');
	});
	$navbar_offcanvas.on("click", function(e) {
		e.stopPropagation();
	});
	$header_cart.on('click', function(e) {
		e.stopPropagation();
	});
	$navbar_offcanvas_close.on("click", function(e) {
		$navbar_offcanvas.removeClass('open');
		$header_hamburger.removeClass('active');
	});
	$info_offcanvas_toggle.on("click", function(e) {
		e.stopPropagation();
		$info_offcanvas.toggleClass('open');
	});
	$info_offcanvas.on("click", function(e) {
		e.stopPropagation();
	});
	$(document).on('click', function() {
		$navbar_offcanvas.removeClass('open');
		/*$language_select.collapse('hide');*/
		$info_offcanvas.removeClass('open');
		$header_hamburger.removeClass('active');
	});
	$info_offcanvas_close.on("click", function(e) {
		$info_offcanvas.removeClass('open');
	});
	$('.onepage .navbar li a.scroll').on('click', function() {
		$navbar_offcanvas.removeClass('open');
		$header_hamburger.removeClass('active');
	});
	/*-----------------------------------------------------------------------------------*/
	/*	ONEPAGE HEADER OFFSET
	/*-----------------------------------------------------------------------------------*/
	var header_height = $('.navbar:not(.banner--clone)').outerHeight();
	var shrinked_header_height = 75;
	var firstStyle = {
		'padding-top': '' + shrinked_header_height + 'px',
		'margin-top': '-' + shrinked_header_height + 'px'
	};
	$('.onepage section').css(firstStyle);
	var secondStyle = {
		'padding-top': '' + header_height + 'px',
		'margin-top': '-' + header_height + 'px'
	};
	$('.onepage section:first-of-type').css(secondStyle);
	/*-----------------------------------------------------------------------------------*/
	/*	ONEPAGE NAV LINKS
	/*-----------------------------------------------------------------------------------*/
	var empty_a = $('.onepage .navbar ul.navbar-nav a[href="#"]');
	empty_a.on('click', function(e) {
		e.preventDefault();
	});
	/*-----------------------------------------------------------------------------------*/
	/*	ONEPAGE SMOOTH SCROLL
	/*-----------------------------------------------------------------------------------*/
	$(function() {
		setTimeout(function() {
			if (location.hash) {
				window.scrollTo(0, 0);
				var target = location.hash.split('#');
				smoothScrollTo($('#' + target[1]));
			}
		}, 1);
		$('a.scroll[href*="#"]:not([href="#"])').on('click', function() {
			if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
				smoothScrollTo($(this.hash));
				return false;
			}
		});

		function smoothScrollTo(target) {
			var target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
			if (target.length) {
				$('html,body').animate({
					scrollTop: target.offset().top
				}, 1500, 'easeInOutExpo');
			}
		}
	});
	/*-----------------------------------------------------------------------------------*/
	/*	SVG INJECT
	/*-----------------------------------------------------------------------------------*/
	SVGInject(document.querySelectorAll("img.svg-inject"));
	/*-----------------------------------------------------------------------------------*/
	/*	BACKGROUND IMAGE
	/*-----------------------------------------------------------------------------------*/
	$(".bg-image").css('background-image', function() {
		var bg = ('url(' + $(this).data("image-src") + ')');
		return bg;
	});
	/*-----------------------------------------------------------------------------------*/
	/*	IMAGE ICON HOVER
	/*-----------------------------------------------------------------------------------*/
	$('.overlay:not(.caption) > a, .overlay:not(.caption) > span').prepend('<span class="bg"></span>');
	/*-----------------------------------------------------------------------------------*/
	/*	RELLAX
	/*-----------------------------------------------------------------------------------*/
	function enableRellax() {
		if ($(".rellax").length) {
			var rellax = new Rellax('.rellax', {
				speed: 2,
				center: true,
				breakpoints: [576, 992, 1201]
			});
			$('.projects-overflow').imagesLoaded(function() {
				rellax.refresh();
			});
		}
	};
	enableRellax();
	/*-----------------------------------------------------------------------------------*/
	/*	SCROLLCUE
	/*-----------------------------------------------------------------------------------*/
	function enableScrollCue() {
		scrollCue.init({
			interval: -400,
			duration: 700,
			percentage: 0.8
		});
	};
	enableScrollCue();
	scrollCue.update();
	/*-----------------------------------------------------------------------------------*/
	/*	ISOTOPE GRID
	/*-----------------------------------------------------------------------------------*/
	function enableIsotope() {
		// for each container
		$('.grid').each(function(i, gridContainer) {
			var $gridContainer = $(gridContainer);
			// init isotope for container
			var $grid = $gridContainer.find('.isotope').imagesLoaded(function() {
				$grid.isotope({
					itemSelector: '.item',
					layoutMode: 'masonry',
					percentPosition: true,
					masonry: {
						columnWidth: $grid.width() / 12
					},
					transitionDuration: '0.7s'
				})
			});
			$(window).resize(function() {
				$grid.isotope({
					masonry: {
						columnWidth: $grid.width() / 12
					}
				});
			});
			$(window).on("load", function() {
				$grid.isotope({
					masonry: {
						columnWidth: $grid.width() / 12
					}
				});
			});
			// initi filters for container
			$gridContainer.find('.isotope-filter').on('click', 'a', function() {
				var filterValue = $(this).attr('data-filter');
				$grid.isotope({
					filter: filterValue
				});
			});
		});
		$('.isotope-filter').each(function(i, buttonGroup) {
			var $buttonGroup = $(buttonGroup);
			$buttonGroup.on('click', 'a', function() {
				$buttonGroup.find('.active').removeClass('active');
				$(this).addClass('active');
			});
		});
	};
	enableIsotope();
	/*-----------------------------------------------------------------------------------*/
	/*	SHOW MORE ITEMS
	/*-----------------------------------------------------------------------------------*/
	function enableShowMoreItems() {
		$('.show-more').each(function() {
			var $showmore = $(this);
			$showmore.showMoreItems({
				startNum: $showmore.data("showstart"),
				afterNum: $showmore.data("showafter"),
				moreText: 'Show More',
				after: function() {
					enableIsotope();
					enableRellax();
					enableScrollCue();
				}
			});
		});
	};
	enableShowMoreItems();
	/*-----------------------------------------------------------------------------------*/
	/*	OWL CAROUSEL
	/*-----------------------------------------------------------------------------------*/
	$('.basic-slider').each(function() {
		var $bslider = $(this);
		$bslider.owlCarousel({
			items: 1,
			nav: $bslider.data("nav"),
			navText: ["<i class='uil-arrow-left'></i>", "<i class='uil-arrow-right'></i>"],
			dots: true,
			dotsEach: true,
			autoHeight: true,
			loop: true,
			margin: $bslider.data("margin")
		});
	});
	$('.carousel').each(function() {
		var $carousel = $(this);
		$carousel.owlCarousel({
			autoHeight: false,
			nav: $carousel.data("nav"),
			navText: ["<i class='uil-arrow-left'></i>", "<i class='uil-arrow-right'></i>"],
			dots: $carousel.data("dots"),
			dotsEach: true,
			loop: $carousel.data("loop"),
			margin: $carousel.data("margin"),
			autoplay: $carousel.data("autoplay"),
			autoplayTimeout: $carousel.data("autoplay-timeout"),
			responsive: $carousel.data("responsive")
		});
	});
	/*-----------------------------------------------------------------------------------*/
	/*	HERO SLIDER
	/*-----------------------------------------------------------------------------------*/
	$('.hero-slider').each(function() {
		var $hslider = $(this);
		$hslider.owlCarousel({
			items: 1,
			nav: $(this).data("nav"),
			navText: ["<i class='uil-arrow-left'></i>", "<i class='uil-arrow-right'></i>"],
			dots: $(this).data("dots"),
			dotsEach: true,
			autoHeight: true,
			loop: true,
			autoplay: $hslider.data("autoplay"),
			autoplayTimeout: 5000,
			onInitialized: function() { 
				$hslider.trigger('stop.owl.autoplay');
					setTimeout(function() {$hslider.trigger('play.owl.autoplay')}, 3000)   
			},
			autoplayHoverPause: true,
			margin: 0,
			animateIn: 'fadeIn',
			animateOut: 'fadeOut'
		});
		$hslider.on("changed.owl.carousel", e => {
			$(".owl-item.active").find(".animated-caption").each(function(index, value) {
				$(this).removeClass("animate__animated").removeClass($(this).data("anim"));
			});
			var $currentOwlItem = $(".owl-item").eq(e.item.index);
			$currentOwlItem.find(".animated-caption").each(function(index, value) {
				var a = $(this).data("anim-delay");
				var b = $(this).data("anim-duration");
				$(this).addClass("animate__animated").addClass($(this).data("anim")).css({
					"animation-delay": a + "ms",
					"animation-duration": b + "ms"
				});
			});
		});
		$hslider.trigger("refresh.owl.carousel");
	});
	/*-----------------------------------------------------------------------------------*/
	/*	ANIMATED CAPTION
	/*-----------------------------------------------------------------------------------*/
	var $animatedCaptions = $(".animated-captions");
	$animatedCaptions.find(".animated-caption").each(function() {
		var a = $(this).data("anim-delay");
		var b = $(this).data("anim-duration");
		$(this).addClass("animate__animated").addClass($(this).data("anim")).css({
			"animation-delay": a + "ms",
			"animation-duration": b + "ms"
		});
	});
	/*-----------------------------------------------------------------------------------*/
	/*	LIGHTGALLERY
	/*-----------------------------------------------------------------------------------*/
	function enablelightGallery() {
		var $lg = $('.light-gallery-wrapper');
		$lg.lightGallery({
			thumbnail: false,
			selector: '.lightbox',
			mode: 'lg-fade',
			download: false,
			autoplayControls: false,
			zoom: false,
			fullScreen: false,
			videoMaxWidth: '1000px',
			loop: false,
			counter: false,
			hash: false,
			closable: true,
			mousewheel: true,
			videojs: true,
			videoAutoplay: true,
			share: false
		});
	}
	enablelightGallery();
	/*-----------------------------------------------------------------------------------*/
	/*	PLYR
	/*-----------------------------------------------------------------------------------*/
	const players = Plyr.setup('.player', {
		loadSprite: true,
	});
	/*-----------------------------------------------------------------------------------*/
	/*	PROGRESSBAR
	/*-----------------------------------------------------------------------------------*/
	var $pline = $('.progressbar.line');
	$pline.each(function(i) {
		var line = new ProgressBar.Line(this, {
			strokeWidth: 3,
			trailWidth: 3,
			duration: 3000,
			easing: 'easeInOut',
			text: {
				style: {
					color: 'inherit',
					position: 'absolute',
					right: '0',
					top: '-30px',
					padding: 0,
					margin: 0,
					transform: null
				},
				autoStyleContainer: false
			},
			step: function(state, line, attachment) {
				line.setText(Math.round(line.value() * 100) + ' %');
			}
		});
		var value = ($(this).attr('data-value') / 100);
		$pline.waypoint(function() {
			line.animate(value);
		}, {
			offset: '100%'
		})
	});
	/*-----------------------------------------------------------------------------------*/
	/*	PAGE PROGRESS
	/*-----------------------------------------------------------------------------------*/
	if ($(".progress-wrap").length) {
		var progressPath = document.querySelector('.progress-wrap path');
		var pathLength = progressPath.getTotalLength();
		progressPath.style.transition = progressPath.style.WebkitTransition = 'none';
		progressPath.style.strokeDasharray = pathLength + ' ' + pathLength;
		progressPath.style.strokeDashoffset = pathLength;
		progressPath.getBoundingClientRect();
		progressPath.style.transition = progressPath.style.WebkitTransition = 'stroke-dashoffset 10ms linear';
		var updateProgress = function() {
			var scroll = $(window).scrollTop();
			var height = $(document).height() - $(window).height();
			var progress = pathLength - (scroll * pathLength / height);
			progressPath.style.strokeDashoffset = progress;
		}
		updateProgress();
		$(window).scroll(updateProgress);
		var offset = 50;
		var duration = 550;
		jQuery(window).on('scroll', function() {
			if (jQuery(this).scrollTop() > offset) {
				jQuery('.progress-wrap').addClass('active-progress');
			} else {
				jQuery('.progress-wrap').removeClass('active-progress');
			}
		});
		jQuery('.progress-wrap').on('click', function(event) {
			event.preventDefault();
			jQuery('html, body').animate({
				scrollTop: 0
			}, duration);
			return false;
		})
	}
	/*-----------------------------------------------------------------------------------*/
	/*	COUNTER UP
	/*-----------------------------------------------------------------------------------*/
	jQuery(function($) {
		"use strict";
		var counterUp = window.counterUp["default"]; // import counterUp from "counterup2"	
		var $counters = $(".counter");
		/* Start counting, do this on DOM ready or with Waypoints. */
		$counters.each(function(ignore, counter) {
			var waypoint = new Waypoint({
				element: $(this),
				handler: function() {
					counterUp(counter, {
						duration: 1000,
						delay: 50
					});
					this.destroy();
				},
				offset: 'bottom-in-view',
			});
		});
	});
	/*-----------------------------------------------------------------------------------*/
	/*	TOOLTIP & POPOVER
	/*-----------------------------------------------------------------------------------*/
	var tooltipTriggerList = [].slice.call(document.querySelectorAll('.has-tooltip'))
	var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
		return new bootstrap.Tooltip(tooltipTriggerEl)
	})
	var popoverTriggerList = [].slice.call(document.querySelectorAll('.has-popover'), {
		trigger: 'focus'
	})
	var popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
		return new bootstrap.Popover(popoverTriggerEl)
	})
	/*-----------------------------------------------------------------------------------*/
	/*	ITOOLTIP
	/*-----------------------------------------------------------------------------------*/
	var tooltip = new iTooltip('.itooltip')
	tooltip.init({
		className: 'itooltip-inner',
		indentX: 15,
		indentY: 15,
		positionX: 'right',
		positionY: 'bottom'
	})
	/*-----------------------------------------------------------------------------------*/
	/*	VIDEO WRAPPER
	/*-----------------------------------------------------------------------------------*/
	$('.video-wrapper video').backgroundVideo({
		$outerWrap: $('.video-wrapper'),
		pauseVideoOnViewLoss: false,
		parallaxOptions: {
			effect: 6
		}
	});
	/*-----------------------------------------------------------------------------------*/
	/*	IMAGE WRAPPER MOBILE
	/*-----------------------------------------------------------------------------------*/
	var isMobile = (navigator.userAgent.match(/Android/i) || navigator.userAgent.match(/webOS/i) || navigator.userAgent.match(/iPhone/i) || navigator.userAgent.match(/iPad/i) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1) || navigator.userAgent.match(/iPod/i) || navigator.userAgent.match(/BlackBerry/i)) ? true : false;
	if (isMobile) {
		$('.image-wrapper').addClass('mobile');
	}
	/*-----------------------------------------------------------------------------------*/
	/*	CONTACT FORM
	/*-----------------------------------------------------------------------------------*/
	function enableContactForm() {
		$('.contact-form').validator({
			disable: false,
			focus: false
		});
		// when the form is submitted
		$('.contact-form').on('submit', function(e) {
			// if the validator does not prevent form submit
			if (!e.isDefaultPrevented()) {
				var url = "contact/contact.php";
				// POST values in the background the the script URL
				$.ajax({
					type: "POST",
					url: url,
					data: $(this).serialize(),
					success: function(data) {
						// data = JSON object that contact.php returns
						// we recieve the type of the message: success x danger and apply it to the
						var messageAlert = 'alert-' + data.type;
						var messageText = data.message;
						// let's compose Bootstrap alert box HTML
						var alertBox = '<div class="alert ' + messageAlert + ' alert-dismissible fade show"><button type="button" class="btn-close" data-dismiss="alert" aria-label="Close"></button>' + messageText + '</div>';
						// If we have messageAlert and messageText
						if (messageAlert && messageText) {
							// inject the alert to .messages div in our form
							$('.contact-form').find('.messages').html(alertBox);
							// empty the form
							$('.contact-form')[0].reset();
						}
					}
				});
				return false;
			}
		})
	}
	enableContactForm();
	/*-----------------------------------------------------------------------------------*/
	/*	MODAL
	/*-----------------------------------------------------------------------------------*/
	var scr_size = window.innerWidth;
	var scr_avail = $('body').innerWidth();
	var pad_right = scr_size - scr_avail;
	var myModalEl = document.querySelectorAll('.modal');
	myModalEl.forEach(myModalEl => {
		myModalEl.addEventListener('show.bs.modal', function(e) {
			$('.navbar.fixed').css('padding-right', pad_right);
			$('.progress-wrap').css('margin-right', pad_right);
		})
		myModalEl.addEventListener('hidden.bs.modal', function(e) {
			$('.navbar.fixed').css('padding-right', '');
			$('.progress-wrap').css('margin-right', '');
		})
	});
	if ($('.modal-popup').length > 0) {
		var myModalPopup = new bootstrap.Modal(document.querySelector('.modal-popup'));
		var myModalEl2 = document.querySelector('.modal-popup');
		setTimeout(function() {
			myModalPopup.show();
		}, 200);
	}
	/*-----------------------------------------------------------------------------------*/
	/*	PAGE LOADING
	/*-----------------------------------------------------------------------------------*/
	$('.page-loading').delay(350).fadeOut('slow');
	$('.page-loading .status').fadeOut('slow');
	/*-----------------------------------------------------------------------------------*/
	/*	PRICING
	/*-----------------------------------------------------------------------------------*/
	$('.pricing-wrapper').each(function(i, container) {
		var $container = $(container);
		$container.find(".pricing-switcher").on('click', function() {
			$container.find(".pricing-switcher").toggleClass('pricing-switcher-active');
			$container.find(".price").removeClass('price-hidden');
			$container.find(".price").toggleClass('price-show price-hide');
		});
	});
});