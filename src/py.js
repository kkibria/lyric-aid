import { readable } from 'svelte/store';
export const ready = readable(false, set => 
    window.addEventListener('pywebviewready', () => set(true))
);
 
export const getapi = () => pywebview.api;

