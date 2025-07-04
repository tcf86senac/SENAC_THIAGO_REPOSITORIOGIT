const container = document.querySelector('.container')
const botao = document.querySelector('#botao')
let botao_bool = false


function on_off(){
    container.classList.toggle('on')

    if (botao_bool) {
        botao.textContent = "Ligar"
        botao_bool = false
    } else {
        botao.textContent = "Desligar"
        botao_bool = true
    }
}


