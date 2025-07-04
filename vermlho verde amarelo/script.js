const colors = [
    'radial-gradient(circle, rgba(20, 160, 120, 1) 0%, rgba(12, 225, 187, 1) 15%, rgba(54, 221, 158, 1) 30%, rgba(87, 199, 133, 1) 45%, rgba(100, 255, 200, 1) 60%, rgba(8, 196, 151, 1) 75%, rgba(10, 80, 60, 1) 100%)',
    'radial-gradient(circle, rgba(160, 20, 20, 1) 0%, rgba(225, 60, 60, 1) 15%, rgba(221, 80, 54, 1) 30%, rgba(199, 87, 87, 1) 45%, rgba(255, 120, 120, 1) 60%, rgba(196, 40, 40, 1) 75%, rgba(80, 10, 10, 1) 100%)',
    'radial-gradient(circle, rgba(160, 140, 20, 1) 0%, rgba(225, 200, 12, 1) 15%, rgba(221, 190, 54, 1) 30%, rgba(199, 180, 87, 1) 45%, rgba(255, 230, 100, 1) 60%, rgba(196, 170, 8, 1) 75%, rgba(80, 70, 3, 1) 100%)'
];

let currentIndex = 0;
const container = document.getElementById('colorContainer');
const button = document.getElementById('changeColorBtn');

button.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % colors.length;
    container.style.background = colors[currentIndex];
    
    // Opcional: Mudar o texto do botão
    button.textContent = currentIndex === colors.length - 1 ? 'REINICIAR' : 'PRÓXIMA COR';
});