let ready = false;
window.addEventListener('pywebviewready', function() {
    ready = true;;
})

export const checkText = async (v) => {
    if (ready) {
        await pywebview.api.checkText(v);
    }
}