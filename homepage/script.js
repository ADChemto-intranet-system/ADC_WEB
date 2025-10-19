// ISP 디자인을 참고한 ADChemto 홈페이지 JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // 모바일 메뉴 토글
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav = document.querySelector('.main-nav');
    
    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', function() {
            mainNav.classList.toggle('active');
            const isActive = mainNav.classList.contains('active');
            menuToggle.textContent = isActive ? '메뉴닫기' : '전체메뉴열기';
        });
    }

    // 히어로 슬라이드
    const heroSlides = document.querySelectorAll('.hero-slide');
    const indicators = document.querySelectorAll('.indicator');
    let currentSlide = 0;

    function showSlide(index) {
        heroSlides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
        });
        indicators.forEach((indicator, i) => {
            indicator.classList.toggle('active', i === index);
        });
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % heroSlides.length;
        showSlide(currentSlide);
    }

    // 자동 슬라이드 (5초마다)
    setInterval(nextSlide, 5000);

    // 인디케이터 클릭 이벤트
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', function() {
            currentSlide = index;
            showSlide(currentSlide);
        });
    });

    // 스무스 스크롤
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // 스크롤 시 헤더 스타일 변경
    const header = document.querySelector('.header');
    let lastScrollY = window.scrollY;

    window.addEventListener('scroll', function() {
        const currentScrollY = window.scrollY;
        
        if (currentScrollY > 100) {
            header.style.backgroundColor = 'rgba(212, 244, 212, 0.95)';
            header.style.backdropFilter = 'blur(10px)';
        } else {
            header.style.backgroundColor = '#d4f4d4';
            header.style.backdropFilter = 'none';
        }
        
        lastScrollY = currentScrollY;
    });

    // 애니메이션 on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // 애니메이션 대상 요소들
    const animateElements = document.querySelectorAll('.product-card, .feature-item, .news-item, .partner-item');
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // 제품 카드 호버 효과
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // 뉴스 아이템 클릭 이벤트
    const newsItems = document.querySelectorAll('.news-item');
    newsItems.forEach(item => {
        item.addEventListener('click', function() {
            // 뉴스 상세 페이지로 이동하거나 모달 표시
            console.log('뉴스 아이템 클릭:', this.querySelector('.news-title').textContent);
        });
    });

    // 버튼 클릭 이벤트
    const ctaButtons = document.querySelectorAll('.hero-cta, .btn-more, .btn-catalog');
    ctaButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // 버튼 클릭 애니메이션
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
            
            // 실제 동작 (예: 모달 표시, 페이지 이동 등)
            console.log('버튼 클릭:', this.textContent);
        });
    });

    // 언어 변경 버튼
    const langBtn = document.querySelector('.lang-btn');
    if (langBtn) {
        langBtn.addEventListener('click', function() {
            const currentLang = this.textContent;
            this.textContent = currentLang === 'EN' ? 'KO' : 'EN';
            
            // 언어 변경 로직
            console.log('언어 변경:', this.textContent);
        });
    }

    // 폼 제출 이벤트 (문의하기)
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // 폼 데이터 수집
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            // 폼 제출 처리
            console.log('문의 폼 제출:', data);
            
            // 성공 메시지 표시
            alert('문의가 성공적으로 전송되었습니다.');
            this.reset();
        });
    }

    // 키보드 네비게이션
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            // ESC 키로 모바일 메뉴 닫기
            if (mainNav && mainNav.classList.contains('active')) {
                mainNav.classList.remove('active');
                menuToggle.textContent = '전체메뉴열기';
            }
        }
    });

    // 윈도우 리사이즈 이벤트
    window.addEventListener('resize', function() {
        // 모바일에서 데스크톱으로 변경 시 메뉴 상태 초기화
        if (window.innerWidth > 768 && mainNav) {
            mainNav.classList.remove('active');
            menuToggle.textContent = '전체메뉴열기';
        }
    });

    // 페이지 로드 완료 후 초기화
    console.log('ADChemto 홈페이지가 성공적으로 로드되었습니다.');
});
