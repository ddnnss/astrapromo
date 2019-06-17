let divs = document.getElementsByClassName('inner-circle')

for (let div in divs) {
    divs[div].addEventListener('mouseover', function () {
    let text = this.getElementsByClassName('super-text')[0].innerHTML
    $('.inner-text').html(text)
    })

}

