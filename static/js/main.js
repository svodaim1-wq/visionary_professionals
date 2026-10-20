document.addEventListener('DOMContentLoaded', function () {
    initNavbar();
    initReveal();
    initFaq();
    initCarousel();
    initCounters();
    initBackToTop();
    initDrawer();
    initCalculator();
    initEquipmentFilter();
    initFormLoading();
    initHelpSearch();
});

function initEquipmentFilter() {
    const buttons = document.querySelectorAll('.filter-btn');
    const items = document.querySelectorAll('#equipmentGrid .card');
    if (!buttons.length || !items.length) return;
    buttons.forEach(function (btn) {
        btn.addEventListener('click', function () {
            buttons.forEach(function (b) { b.classList.remove('active'); });
            btn.classList.add('active');
            const filter = btn.getAttribute('data-filter');
            items.forEach(function (item) {
                const match = filter === 'all' || item.getAttribute('data-category') === filter;
                item.style.display = match ? '' : 'none';
            });
        });
    });
}

function initFormLoading() {
    document.querySelectorAll('form').forEach(function (form) {
        form.addEventListener('submit', function () {
            const btn = form.querySelector('button[type="submit"], button:not([type])');
            if (!btn || btn.disabled) return;
            btn.dataset.originalText = btn.innerHTML;
            btn.disabled = true;
            btn.innerHTML = '<span class="spinner"></span> Submitting...';
        });
    });
}

function initHelpSearch() {
    const input = document.getElementById('helpSearchInput');
    if (!input) return;
    input.addEventListener('input', function () {
        const term = input.value.toLowerCase();
        document.querySelectorAll('#helpCategories .help-category').forEach(function (card) {
            const text = card.textContent.toLowerCase();
            card.style.display = !term || text.includes(term) ? '' : 'none';
        });
    });
}

function initNavbar() {
    const navbar = document.getElementById('navbar');
    const progress = document.getElementById('scrollProgress');
    window.addEventListener('scroll', function () {
        if (navbar) navbar.classList.toggle('scrolled', window.scrollY > 10);
        if (progress) {
            const h = document.documentElement.scrollHeight - window.innerHeight;
            progress.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + '%';
        }
    });
}

function initDrawer() {
    const toggle = document.getElementById('navToggle');
    const drawer = document.getElementById('mobileDrawer');
    const overlay = document.getElementById('drawerOverlay');
    const close = document.getElementById('drawerClose');
    if (!toggle || !drawer) return;
    const open = () => { drawer.classList.add('open'); overlay.classList.add('open'); document.body.style.overflow = 'hidden'; };
    const shut = () => { drawer.classList.remove('open'); overlay.classList.remove('open'); document.body.style.overflow = ''; };
    toggle.addEventListener('click', open);
    if (overlay) overlay.addEventListener('click', shut);
    if (close) close.addEventListener('click', shut);
}

function initReveal() {
    const els = document.querySelectorAll('.reveal');
    if (!els.length) return;
    const obs = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
    }, { threshold: 0.12 });
    els.forEach(function (el) { obs.observe(el); });
}

function initFaq() {
    document.querySelectorAll('.faq-question').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const item = btn.closest('.faq-item');
            const isOpen = item.classList.contains('open');
            document.querySelectorAll('.faq-item.open').forEach(function (o) { o.classList.remove('open'); });
            if (!isOpen) item.classList.add('open');
        });
    });
}

function initCarousel() {
    const track = document.querySelector('.testimonial-track');
    if (!track) return;
    const slides = track.querySelectorAll('.testimonial-slide');
    const dotsWrap = document.getElementById('carouselDots');
    let index = 0;
    if (dotsWrap) {
        slides.forEach(function (_, i) {
            const dot = document.createElement('button');
            dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
            dot.setAttribute('aria-label', 'Go to testimonial ' + (i + 1));
            dot.addEventListener('click', function () { go(i); });
            dotsWrap.appendChild(dot);
        });
    }
    function go(i) {
        index = i;
        track.style.transform = 'translateX(-' + i * 100 + '%)';
        document.querySelectorAll('.carousel-dot').forEach(function (d, j) { d.classList.toggle('active', j === i); });
    }
    setInterval(function () { go((index + 1) % slides.length); }, 6000);
}

function initCounters() {
    const counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;
    const obs = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (!entry.isIntersecting) return;
            const el = entry.target;
            const target = parseInt(el.getAttribute('data-count'), 10);
            const suffix = el.getAttribute('data-suffix') || '';
            let current = 0;
            const step = Math.max(1, Math.ceil(target / 60));
            const timer = setInterval(function () {
                current += step;
                if (current >= target) { current = target; clearInterval(timer); }
                el.textContent = current.toLocaleString() + suffix;
            }, 20);
            obs.unobserve(el);
        });
    }, { threshold: 0.5 });
    counters.forEach(function (c) { obs.observe(c); });
}

function initBackToTop() {
    const btn = document.getElementById('backToTop');
    if (!btn) return;
    window.addEventListener('scroll', function () {
        btn.classList.toggle('visible', window.scrollY > 400);
    });
    btn.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
}

function initCalculator() {
    const btn = document.getElementById('calcBtn');
    if (!btn) return;
    btn.addEventListener('click', calculateRate);
}

async function calculateRate() {
    const origin = document.getElementById('origin').value;
    const destination = document.getElementById('destination').value;
    const vehicle = document.getElementById('vehicle').value;
    const distance = parseFloat(document.getElementById('distance').value);
    const resultBox = document.getElementById('result');
    const resultText = document.getElementById('result-text');

    if (!origin || !destination || !vehicle || !distance || distance <= 0) {
        alert('Please fill in all fields with valid values.');
        return;
    }

    try {
        const response = await fetch('/services/api/corridor-rate/?origin=' + origin + '&destination=' + destination + '&vehicle=' + vehicle + '&distance=' + distance);
        const data = await response.json();

        if (!response.ok) {
            alert(data.error || 'Rate not available for this corridor yet. Contact dispatch for a quote.');
            return;
        }

        const minTotal = data.total_estimate.min.toLocaleString('en-ZA', { style: 'currency', currency: 'ZAR' });
        const maxTotal = data.total_estimate.max.toLocaleString('en-ZA', { style: 'currency', currency: 'ZAR' });
        const dispatchMin = (data.total_estimate.min * data.dispatch_fee_percent.min / 100).toLocaleString('en-ZA', { style: 'currency', currency: 'ZAR' });
        const dispatchMax = (data.total_estimate.max * data.dispatch_fee_percent.max / 100).toLocaleString('en-ZA', { style: 'currency', currency: 'ZAR' });
        const netMin = (data.total_estimate.min * 0.92).toLocaleString('en-ZA', { style: 'currency', currency: 'ZAR' });
        const netMax = (data.total_estimate.max * 0.95).toLocaleString('en-ZA', { style: 'currency', currency: 'ZAR' });

        resultText.innerHTML = '<strong>Estimated Gross Revenue:</strong> ' + minTotal + ' - ' + maxTotal + '<br>' +
            '<strong>Est. Dispatch Fee (' + data.dispatch_fee_percent.min + '% - ' + data.dispatch_fee_percent.max + '%):</strong> ' + dispatchMin + ' - ' + dispatchMax + '<br>' +
            '<strong>Net Estimate:</strong> ' + netMin + ' - ' + netMax;
        resultBox.style.display = 'block';
    } catch (error) {
        alert('Error calculating rate. Please try again.');
    }
}
