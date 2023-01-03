window.addEventListener('scroll', () => {
    document.querySelector('nav').classList.toggle('window-scroll', window.scrollY > 0)
})

// animate on scroll

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show')
        } else {
            entry.target.classList.remove('show')
        }
    })
})

const entries = document.querySelectorAll('.hidden')
entries.forEach(entry => observer.observe(entry))

// open and close faqs

const faqs = document.querySelectorAll('.faq')

faqs.forEach(faq => {
    faq.addEventListener('click', () => {
        faq.classList.toggle('open')

        const icon = faq.querySelector('.icon i')
        if (icon.className === 'uil uil-plus') {
            icon.className = 'uil uil-minus'
        } else {
            icon.className = 'uil uil-plus'
        }
    })
})

// nav bar
const nav = document.querySelector('nav')
const menu = document.querySelector('.nav__menu')
const openMenu = document.querySelector('#open-menu')
const closeMenu = document.querySelector('#close-menu')

openMenu.addEventListener('click', () => {
    nav.style.display = 'block'
    nav.style.height = 'max-content'
    menu.style.display = 'block'
    closeMenu.style.display = 'block'
    openMenu.style.display = 'none'
})

closeMenu.addEventListener('click', () => {
    menu.style.display = 'none'
    openMenu.style.display = 'inline-block'
    closeMenu.style.display = 'none'
})