export const getVariableFromDjango = function (variableId) {
    const element = document.querySelector(`#${variableId}`);
    if (element) {
        return JSON.parse(element.innerText);
    }
}