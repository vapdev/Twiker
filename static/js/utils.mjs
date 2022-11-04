export const getVariableFromDjango = function (variableId) {
    console.log("variableId", variableId);
    const element = document.querySelector(`#${variableId}`);
    if (element) {
        console.log("element", element.textContent);
        return JSON.parse(element.innerText);
    }
}