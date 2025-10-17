// Esperamos a que todo el contenido de la página esté listo
document.addEventListener('DOMContentLoaded', function() {

    // 1. Seleccionamos el botón específico que queremos que tenga el scroll suave.
    const scrollLink = document.querySelector('a.btn-primary[href="#productos-destacados"]');

    // 2. Si el botón existe en la página, continuamos.
    if (scrollLink) {
        // 3. Añadimos un "escuchador" para el evento 'click'.
        scrollLink.addEventListener('click', function(e) {
            // 4. Prevenimos el salto brusco que el navegador haría por defecto.
            e.preventDefault();

            // 5. Obtenemos el ID de la sección de destino (en este caso, "#productos-destacados").
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                // 6. Usamos una función especial para hacer el scroll suave.
                smoothScrollTo(targetElement, 1500); // 1500 milisegundos = 1.5 segundos
            }
        });
    }
});


/**
 * Función que realiza un scroll suave a un elemento específico.
 * @param {HTMLElement} targetElement - El elemento al que queremos desplazarnos.
 * @param {number} duration - La duración de la animación en milisegundos.
 */
function smoothScrollTo(targetElement, duration) {
    const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;
    const startPosition = window.pageYOffset;
    const distance = targetPosition - startPosition;
    let startTime = null;

    function animation(currentTime) {
        if (startTime === null) {
            startTime = currentTime;
        }
        const timeElapsed = currentTime - startTime;
        const run = easeInOutQuad(timeElapsed, startPosition, distance, duration);
        window.scrollTo(0, run);
        if (timeElapsed < duration) {
            requestAnimationFrame(animation);
        }
    }

    // Función de 'easing' para que el scroll sea más natural (acelera y desacelera)
    function easeInOutQuad(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
    }

    requestAnimationFrame(animation);
}

/**
 * Función para preparar el modal de compra.
 * Rellena automáticamente el nombre del producto en el formulario.
 * @param {string} productName - El nombre del producto en el que se hizo clic.
 */
function prepareModal(productName) {
    // Seleccionamos el campo de texto del producto dentro del modal
    const productInput = document.querySelector('#modal-compra #producto');

    // Si el campo de texto existe, actualizamos su valor con el nombre del producto
    if (productInput) {
        productInput.value = productName;
    }
}