console.log('Loading lists.js');

const initialize = (inputSelector) => {
    // console.log('initialize called');
    const textInput = document.querySelector(inputSelector);
    textInput.oninput = () => {
        textInput.classList.remove('is-invalid');
    };
};